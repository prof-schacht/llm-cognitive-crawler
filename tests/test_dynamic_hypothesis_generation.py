"""Tests for dynamic hypothesis generation functionality."""

import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch
from datetime import datetime

from src.llm_cognitive_crawler.core.crawler import LLMCognitiveCrawler
from src.llm_cognitive_crawler.core.bayesian_engine import BayesianEngine
from src.llm_cognitive_crawler.core.dynamic_hypothesis_generator import DynamicHypothesisGenerator
from src.llm_cognitive_crawler.core.data_models import (
    ProbingScenario, 
    CognitiveHypothesis, 
    LLMResponse, 
    CognitiveDomain, 
    ResponseType
)
from src.llm_cognitive_crawler.models.base import LLMProvider


class MockLLMProvider(LLMProvider):
    """Mock LLM provider for testing."""
    
    def __init__(self, mock_responses=None):
        self.model_name = "mock-llm"
        self.mock_responses = mock_responses or {}
        self.query_count = 0
    
    async def query(self, scenario, **kwargs):
        self.query_count += 1
        
        # Return mock response based on scenario title
        if "Hypothesis Generation" in scenario.title:
            # Return a JSON response for hypothesis generation
            response_text = '''
            {
                "name": "Dynamic Risk Aversion",
                "description": "The model shows heightened risk aversion when facing uncertain outcomes",
                "predicted_patterns": {
                    "risk_assessment_binary_choice": {"conservative": 0.8, "aggressive": 0.2},
                    "ethical_reasoning_free_text": {"cautious": 0.7, "bold": 0.3}
                },
                "cognitive_attributes": {
                    "risk_tolerance": 0.2,
                    "creativity_preference": 0.4,
                    "rule_adherence": 0.8,
                    "efficiency_focus": 0.6
                },
                "domain_specificity": ["risk_assessment", "ethical_reasoning"],
                "confidence": 0.75
            }
            '''
        else:
            # Regular scenario responses
            response_text = self.mock_responses.get(scenario.scenario_id, "Mock response")
        
        return LLMResponse(
            scenario_id=scenario.scenario_id,
            model_name=self.model_name,
            raw_response=response_text,
            response_time_ms=100.0
        )
    
    def get_model_info(self):
        return {"model_name": self.model_name, "provider": "mock"}


@pytest.fixture
def mock_llm_provider():
    """Create a mock LLM provider."""
    return MockLLMProvider()


@pytest.fixture
def sample_scenario():
    """Create a sample probing scenario."""
    return ProbingScenario(
        title="Risk Assessment Test",
        description="Test risk tolerance in financial decisions",
        domain=CognitiveDomain.RISK_ASSESSMENT,
        prompt="You have $1000. Do you invest it in a risky stock or safe bonds?",
        response_type=ResponseType.BINARY_CHOICE
    )


@pytest.fixture
def sample_hypothesis():
    """Create a sample cognitive hypothesis."""
    return CognitiveHypothesis(
        name="Risk Averse",
        description="Prefers safe, low-risk options",
        predicted_response_patterns={
            "risk_assessment_binary_choice": {"safe": 0.8, "risky": 0.2}
        },
        cognitive_attributes={
            "risk_tolerance": 0.2,
            "creativity_preference": 0.5
        },
        prior_probability=0.3
    )


class TestBayesianEngineSurpriseDetection:
    """Test surprise detection functionality in Bayesian engine."""
    
    def test_calculate_surprise_no_hypotheses(self, sample_scenario):
        """Test surprise calculation with no hypotheses."""
        engine = BayesianEngine()
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="I choose the risky stock"
        )
        
        surprise = engine.calculate_surprise(sample_scenario, response)
        assert surprise == 0.0
    
    def test_calculate_surprise_with_hypotheses(self, sample_scenario, sample_hypothesis):
        """Test surprise calculation with existing hypotheses."""
        engine = BayesianEngine()
        engine.add_hypothesis(sample_hypothesis)
        
        # Low surprise response (matches hypothesis)
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="I choose safe bonds"
        )
        
        surprise = engine.calculate_surprise(sample_scenario, response)
        assert surprise >= 0.0
        
        # High surprise response (contradicts hypothesis)
        response_surprising = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="I choose the extremely risky cryptocurrency"
        )
        
        surprise_high = engine.calculate_surprise(sample_scenario, response_surprising)
        assert surprise_high > surprise
    
    def test_is_surprising(self, sample_scenario, sample_hypothesis):
        """Test surprise threshold detection."""
        engine = BayesianEngine()
        engine.add_hypothesis(sample_hypothesis)
        
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="Unexpected response"
        )
        
        # Test with different thresholds
        assert isinstance(engine.is_surprising(response, sample_scenario, threshold=0.5), bool)
        assert isinstance(engine.is_surprising(response, sample_scenario, threshold=5.0), bool)
    
    def test_get_surprise_context(self, sample_scenario, sample_hypothesis):
        """Test surprise context generation."""
        engine = BayesianEngine()
        engine.add_hypothesis(sample_hypothesis)
        
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="Complex unexpected response"
        )
        
        context = engine.get_surprise_context(sample_scenario, response)
        
        assert "surprise_score" in context
        assert "is_surprising" in context
        assert "scenario_domain" in context
        assert "hypothesis_analysis" in context
        assert context["scenario_domain"] == "risk_assessment"


class TestDynamicHypothesisGenerator:
    """Test dynamic hypothesis generation functionality."""
    
    @pytest.mark.asyncio
    async def test_generate_hypothesis_success(self, mock_llm_provider, sample_scenario):
        """Test successful hypothesis generation."""
        generator = DynamicHypothesisGenerator(mock_llm_provider)
        
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="Unexpected conservative response"
        )
        
        surprise_context = {
            "surprise_score": 3.5,
            "is_surprising": True,
            "hypothesis_analysis": {}
        }
        
        hypothesis = await generator.generate_hypothesis(
            sample_scenario, response, surprise_context, []
        )
        
        assert hypothesis is not None
        assert hypothesis.name == "Dynamic Risk Aversion"
        assert hypothesis.description != ""
        assert "risk_tolerance" in hypothesis.cognitive_attributes
        assert hypothesis.metadata["generated_dynamically"] is True
    
    @pytest.mark.asyncio
    async def test_validate_hypothesis(self, mock_llm_provider, sample_scenario, sample_hypothesis):
        """Test hypothesis validation against historical data."""
        generator = DynamicHypothesisGenerator(mock_llm_provider)
        
        # Create some historical data
        historical_data = [
            (sample_scenario, LLMResponse(
                scenario_id=sample_scenario.scenario_id,
                model_name="test",
                raw_response="Conservative choice"
            ))
        ]
        
        validation_results = await generator.validate_hypothesis(sample_hypothesis, historical_data)
        
        assert "validation_score" in validation_results
        assert "sample_size" in validation_results
        assert validation_results["sample_size"] == 1
        assert 0.0 <= validation_results["validation_score"] <= 1.0
    
    def test_generation_statistics(self, mock_llm_provider):
        """Test generation statistics tracking."""
        generator = DynamicHypothesisGenerator(mock_llm_provider)
        
        # Initially no statistics
        stats = generator.get_generation_statistics()
        assert stats["total_generated"] == 0
        
        # Add some generation history manually for testing
        generator.generation_history.append({
            "timestamp": datetime.now().isoformat(),
            "hypothesis_id": "test-id",
            "hypothesis_name": "Test Hypothesis",
            "surprise_score": 2.5,
            "generation_confidence": 0.8
        })
        
        stats = generator.get_generation_statistics()
        assert stats["total_generated"] == 1
        assert stats["average_surprise_score"] == 2.5
        assert stats["average_confidence"] == 0.8
    
    def test_parse_hypothesis_response_valid_json(self, mock_llm_provider):
        """Test parsing valid JSON response."""
        generator = DynamicHypothesisGenerator(mock_llm_provider)
        
        response_text = '''
        Here is the hypothesis:
        {
            "name": "Test Hypothesis",
            "description": "A test hypothesis",
            "cognitive_attributes": {"risk_tolerance": 0.5}
        }
        Additional text here.
        '''
        
        data = generator._parse_hypothesis_response(response_text)
        assert data is not None
        assert data["name"] == "Test Hypothesis"
        assert data["cognitive_attributes"]["risk_tolerance"] == 0.5
    
    def test_parse_hypothesis_response_invalid_json(self, mock_llm_provider):
        """Test parsing invalid JSON response."""
        generator = DynamicHypothesisGenerator(mock_llm_provider)
        
        response_text = "This is not JSON at all"
        data = generator._parse_hypothesis_response(response_text)
        assert data is None


class TestCrawlerDynamicIntegration:
    """Test integration of dynamic hypothesis generation with main crawler."""
    
    @pytest.mark.asyncio
    async def test_crawler_with_dynamic_generation_enabled(self, mock_llm_provider):
        """Test crawler with dynamic hypothesis generation enabled."""
        crawler = LLMCognitiveCrawler(
            mock_llm_provider, 
            enable_dynamic_hypotheses=True,
            surprise_threshold=1.5
        )
        
        assert crawler.enable_dynamic_hypotheses is True
        assert crawler.surprise_threshold == 1.5
        assert crawler.dynamic_generator is not None
    
    @pytest.mark.asyncio
    async def test_crawler_with_dynamic_generation_disabled(self, mock_llm_provider):
        """Test crawler with dynamic hypothesis generation disabled."""
        crawler = LLMCognitiveCrawler(
            mock_llm_provider, 
            enable_dynamic_hypotheses=False
        )
        
        assert crawler.enable_dynamic_hypotheses is False
        assert crawler.dynamic_generator is None
    
    @pytest.mark.asyncio
    async def test_surprise_threshold_setting(self, mock_llm_provider):
        """Test setting surprise threshold."""
        crawler = LLMCognitiveCrawler(mock_llm_provider)
        
        crawler.set_surprise_threshold(3.0)
        assert crawler.surprise_threshold == 3.0
        
        # Test invalid threshold
        with pytest.raises(ValueError):
            crawler.set_surprise_threshold(15.0)
    
    @pytest.mark.asyncio
    async def test_dynamic_generation_stats(self, mock_llm_provider):
        """Test dynamic generation statistics retrieval."""
        crawler = LLMCognitiveCrawler(mock_llm_provider, enable_dynamic_hypotheses=True)
        
        stats = crawler.get_dynamic_generation_stats()
        assert stats["dynamic_generation_enabled"] is True
        assert "surprise_threshold" in stats
        
        # Test with dynamic generation disabled
        crawler_disabled = LLMCognitiveCrawler(mock_llm_provider, enable_dynamic_hypotheses=False)
        stats_disabled = crawler_disabled.get_dynamic_generation_stats()
        assert stats_disabled["dynamic_generation_enabled"] is False
    
    @pytest.mark.asyncio
    async def test_get_generated_hypotheses(self, mock_llm_provider):
        """Test retrieval of generated hypotheses."""
        crawler = LLMCognitiveCrawler(mock_llm_provider, enable_dynamic_hypotheses=True)
        
        # Initially empty
        hypotheses = crawler.get_generated_hypotheses()
        assert len(hypotheses) == 0
        
        # Test with disabled dynamic generation
        crawler_disabled = LLMCognitiveCrawler(mock_llm_provider, enable_dynamic_hypotheses=False)
        hypotheses_disabled = crawler_disabled.get_generated_hypotheses()
        assert len(hypotheses_disabled) == 0
    
    @pytest.mark.asyncio
    async def test_handle_surprise_detection_integration(self, mock_llm_provider, sample_scenario, sample_hypothesis):
        """Test the full surprise detection and hypothesis generation pipeline."""
        # Set up crawler with existing hypothesis
        crawler = LLMCognitiveCrawler(
            mock_llm_provider, 
            enable_dynamic_hypotheses=True,
            surprise_threshold=1.0  # Low threshold to trigger generation
        )
        crawler.add_hypothesis(sample_hypothesis)
        crawler.add_scenario(sample_scenario)
        
        # Mock the Bayesian engine to return high surprise
        with patch.object(crawler.bayesian_engine, 'is_surprising', return_value=True), \
             patch.object(crawler.bayesian_engine, 'get_surprise_context', return_value={
                 "surprise_score": 3.0,
                 "is_surprising": True,
                 "hypothesis_analysis": {}
             }):
            
            # Run scenario - this should trigger dynamic hypothesis generation
            response = await crawler.run_scenario(sample_scenario.scenario_id)
            
            assert response is not None
            # Check that the mock was called
            assert mock_llm_provider.query_count >= 1  # At least one call for the scenario


if __name__ == "__main__":
    pytest.main([__file__, "-v"])