"""Tests for main LLM Cognitive Crawler."""

import pytest
from unittest.mock import AsyncMock, Mock
from llm_cognitive_crawler.core.crawler import LLMCognitiveCrawler
from llm_cognitive_crawler.core.data_models import (
    ProbingScenario,
    CognitiveHypothesis,
    LLMResponse,
    CognitiveDomain,
    ResponseType
)
from llm_cognitive_crawler.models.base import LLMProvider


class MockLLMProvider(LLMProvider):
    """Mock LLM provider for testing."""
    
    def __init__(self, model_name="mock-model"):
        super().__init__(model_name)
        self.query_responses = {}
    
    def set_response(self, scenario_id: str, response_text: str):
        """Set a mock response for a scenario."""
        self.query_responses[scenario_id] = response_text
    
    async def query(self, scenario, **kwargs):
        response_text = self.query_responses.get(
            scenario.scenario_id, 
            "Mock response"
        )
        
        return LLMResponse(
            scenario_id=scenario.scenario_id,
            model_name=self.model_name,
            raw_response=response_text,
            response_time_ms=100.0
        )
    
    async def get_available_models(self):
        return ["mock-model"]
    
    async def health_check(self):
        return True


class TestLLMCognitiveCrawler:
    """Test main crawler functionality."""
    
    @pytest.fixture
    def mock_provider(self):
        return MockLLMProvider()
    
    @pytest.fixture
    def crawler(self, mock_provider):
        return LLMCognitiveCrawler(mock_provider)
    
    @pytest.fixture
    def sample_scenario(self):
        return ProbingScenario(
            title="Trolley Problem",
            prompt="Would you pull the lever?",
            domain=CognitiveDomain.ETHICAL_REASONING,
            response_type=ResponseType.BINARY_CHOICE
        )
    
    @pytest.fixture
    def sample_hypothesis(self):
        return CognitiveHypothesis(
            name="Utilitarian",
            description="Maximizes outcomes",
            predicted_response_patterns={
                "ethical_reasoning_binary_choice": {"yes": 0.8}
            },
            prior_probability=0.5
        )
    
    def test_add_scenario(self, crawler, sample_scenario):
        crawler.add_scenario(sample_scenario)
        
        assert sample_scenario.scenario_id in crawler.scenarios
        assert crawler.scenarios[sample_scenario.scenario_id] == sample_scenario
    
    def test_add_multiple_scenarios(self, crawler):
        scenarios = [
            ProbingScenario(title="Test 1", prompt="Test 1"),
            ProbingScenario(title="Test 2", prompt="Test 2")
        ]
        
        crawler.add_scenarios(scenarios)
        
        assert len(crawler.scenarios) == 2
        for scenario in scenarios:
            assert scenario.scenario_id in crawler.scenarios
    
    def test_add_hypothesis(self, crawler, sample_hypothesis):
        crawler.add_hypothesis(sample_hypothesis)
        
        assert sample_hypothesis.hypothesis_id in crawler.bayesian_engine.hypotheses
    
    def test_add_multiple_hypotheses(self, crawler):
        hypotheses = [
            CognitiveHypothesis(name="H1"),
            CognitiveHypothesis(name="H2")
        ]
        
        crawler.add_hypotheses(hypotheses)
        
        assert len(crawler.bayesian_engine.hypotheses) == 2
    
    @pytest.mark.asyncio
    async def test_run_scenario_success(self, crawler, mock_provider, sample_scenario):
        crawler.add_scenario(sample_scenario)
        mock_provider.set_response(sample_scenario.scenario_id, "Yes, I would pull the lever")
        
        response = await crawler.run_scenario(sample_scenario.scenario_id)
        
        assert response is not None
        assert response.scenario_id == sample_scenario.scenario_id
        assert response.raw_response == "Yes, I would pull the lever"
        assert response.response_id in crawler.responses
    
    @pytest.mark.asyncio
    async def test_run_scenario_not_found(self, crawler):
        response = await crawler.run_scenario("nonexistent-id")
        
        assert response is None
    
    @pytest.mark.asyncio
    async def test_run_scenarios_multiple(self, crawler, mock_provider):
        scenarios = [
            ProbingScenario(title="Test 1", prompt="Test 1"),
            ProbingScenario(title="Test 2", prompt="Test 2")
        ]
        
        for scenario in scenarios:
            crawler.add_scenario(scenario)
            mock_provider.set_response(scenario.scenario_id, f"Response to {scenario.title}")
        
        responses = await crawler.run_scenarios(max_concurrent=1)
        
        assert len(responses) == 2
        assert all(isinstance(r, LLMResponse) for r in responses)
    
    @pytest.mark.asyncio
    async def test_run_comprehensive_analysis(self, crawler, mock_provider, sample_scenario, sample_hypothesis):
        # Set up scenario and hypothesis
        crawler.add_scenario(sample_scenario)
        crawler.add_hypothesis(sample_hypothesis)
        mock_provider.set_response(sample_scenario.scenario_id, "Yes")
        
        results = await crawler.run_comprehensive_analysis()
        
        assert "model_info" in results
        assert "scenarios_run" in results
        assert "hypothesis_rankings" in results
        assert "convergence_metrics" in results
        assert results["scenarios_run"] == 1
    
    @pytest.mark.asyncio
    async def test_run_comprehensive_analysis_no_scenarios(self, crawler, sample_hypothesis):
        crawler.add_hypothesis(sample_hypothesis)
        
        with pytest.raises(ValueError, match="No scenarios available"):
            await crawler.run_comprehensive_analysis()
    
    @pytest.mark.asyncio
    async def test_run_comprehensive_analysis_no_hypotheses(self, crawler, sample_scenario):
        crawler.add_scenario(sample_scenario)
        
        with pytest.raises(ValueError, match="No hypotheses available"):
            await crawler.run_comprehensive_analysis()
    
    def test_generate_cognitive_profile(self, crawler, sample_hypothesis):
        crawler.add_hypothesis(sample_hypothesis)
        
        profile = crawler.generate_cognitive_profile()
        
        assert profile.model_name == "mock-model"
        assert len(profile.dominant_patterns) > 0
        assert profile.scenario_count == 0  # No responses yet
    
    def test_generate_cognitive_profile_no_hypotheses(self, crawler):
        with pytest.raises(ValueError, match="No hypotheses available"):
            crawler.generate_cognitive_profile()
    
    def test_get_scenario_by_domain(self, crawler):
        ethical_scenario = ProbingScenario(
            title="Ethical Test",
            prompt="Test",
            domain=CognitiveDomain.ETHICAL_REASONING
        )
        logical_scenario = ProbingScenario(
            title="Logical Test", 
            prompt="Test",
            domain=CognitiveDomain.LOGICAL_REASONING
        )
        
        crawler.add_scenario(ethical_scenario)
        crawler.add_scenario(logical_scenario)
        
        ethical_scenarios = crawler.get_scenario_by_domain(CognitiveDomain.ETHICAL_REASONING)
        
        assert len(ethical_scenarios) == 1
        assert ethical_scenarios[0].title == "Ethical Test"
    
    def test_get_responses_by_scenario(self, crawler, sample_scenario):
        # Add a response manually
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="Test response"
        )
        crawler.responses[response.response_id] = response
        
        responses = crawler.get_responses_by_scenario(sample_scenario.scenario_id)
        
        assert len(responses) == 1
        assert responses[0].raw_response == "Test response"
    
    def test_export_results(self, crawler, sample_scenario, sample_hypothesis):
        crawler.add_scenario(sample_scenario)
        crawler.add_hypothesis(sample_hypothesis)
        
        results = crawler.export_results()
        
        assert "scenarios" in results
        assert "hypotheses" in results
        assert "posterior_probabilities" in results
        assert "responses" in results
        assert "convergence_metrics" in results
        
        assert sample_scenario.scenario_id in results["scenarios"]
        assert sample_hypothesis.hypothesis_id in results["hypotheses"]
    
    @pytest.mark.asyncio
    async def test_close(self, crawler):
        # Mock provider with close method
        crawler.llm_provider.close = AsyncMock()
        
        await crawler.close()
        
        crawler.llm_provider.close.assert_called_once()