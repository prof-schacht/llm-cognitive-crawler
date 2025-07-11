"""Tests for Ollama provider."""

import pytest
from unittest.mock import AsyncMock, patch
import httpx
from llm_cognitive_crawler.models.ollama_provider import OllamaProvider
from llm_cognitive_crawler.core.data_models import ProbingScenario, CognitiveDomain


class TestOllamaProvider:
    """Test Ollama LLM provider."""
    
    @pytest.fixture
    def provider(self):
        return OllamaProvider("test-model")
    
    @pytest.fixture
    def sample_scenario(self):
        return ProbingScenario(
            title="Test Scenario",
            prompt="What is 2+2?",
            domain=CognitiveDomain.LOGICAL_REASONING
        )
    
    @pytest.mark.asyncio
    async def test_query_success(self, provider, sample_scenario):
        mock_response = {
            "response": "2+2 equals 4",
            "model": "test-model",
            "total_duration": 1000000000,
            "eval_count": 10
        }
        
        with patch.object(provider.client, 'post') as mock_post:
            mock_post.return_value.json.return_value = mock_response
            mock_post.return_value.raise_for_status.return_value = None
            
            response = await provider.query(sample_scenario)
            
            assert response.scenario_id == sample_scenario.scenario_id
            assert response.model_name == "test-model"
            assert response.raw_response == "2+2 equals 4"
            assert response.response_time_ms > 0
            assert "eval_count" in response.metadata
    
    @pytest.mark.asyncio
    async def test_query_error(self, provider, sample_scenario):
        with patch.object(provider.client, 'post') as mock_post:
            mock_post.side_effect = httpx.HTTPError("Connection failed")
            
            response = await provider.query(sample_scenario)
            
            assert response.scenario_id == sample_scenario.scenario_id
            assert response.model_version == "error"
            assert "Error:" in response.raw_response
            assert "error" in response.metadata
    
    @pytest.mark.asyncio
    async def test_get_available_models_success(self, provider):
        mock_response = {
            "models": [
                {"name": "llama2:7b"},
                {"name": "mistral:7b"}
            ]
        }
        
        with patch.object(provider.client, 'get') as mock_get:
            mock_get.return_value.json.return_value = mock_response
            mock_get.return_value.raise_for_status.return_value = None
            
            models = await provider.get_available_models()
            
            assert models == ["llama2:7b", "mistral:7b"]
    
    @pytest.mark.asyncio
    async def test_get_available_models_error(self, provider):
        with patch.object(provider.client, 'get') as mock_get:
            mock_get.side_effect = httpx.HTTPError("Connection failed")
            
            models = await provider.get_available_models()
            
            assert models == []
    
    @pytest.mark.asyncio
    async def test_health_check_success(self, provider):
        with patch.object(provider.client, 'get') as mock_get:
            mock_get.return_value.status_code = 200
            
            is_healthy = await provider.health_check()
            
            assert is_healthy is True
    
    @pytest.mark.asyncio
    async def test_health_check_failure(self, provider):
        with patch.object(provider.client, 'get') as mock_get:
            mock_get.side_effect = httpx.HTTPError("Connection failed")
            
            is_healthy = await provider.health_check()
            
            assert is_healthy is False
    
    def test_model_info(self, provider):
        info = provider.get_model_info()
        
        assert info["model_name"] == "test-model"
        assert info["provider"] == "OllamaProvider"
        assert "config" in info
    
    @pytest.mark.asyncio
    async def test_close(self, provider):
        with patch.object(provider.client, 'aclose') as mock_close:
            await provider.close()
            mock_close.assert_called_once()