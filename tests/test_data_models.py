"""Tests for core data models."""

import pytest
from datetime import datetime
from llm_cognitive_crawler.core.data_models import (
    ProbingScenario,
    CognitiveHypothesis,
    LLMResponse,
    CognitiveProfile,
    CognitiveDomain,
    ResponseType
)


class TestProbingScenario:
    """Test ProbingScenario data model."""
    
    def test_valid_scenario_creation(self):
        scenario = ProbingScenario(
            title="Test Scenario",
            description="A test scenario",
            domain=CognitiveDomain.ETHICAL_REASONING,
            prompt="What would you do?",
            response_type=ResponseType.BINARY_CHOICE,
            difficulty_level=3
        )
        
        assert scenario.title == "Test Scenario"
        assert scenario.domain == CognitiveDomain.ETHICAL_REASONING
        assert scenario.difficulty_level == 3
        assert scenario.scenario_id is not None
        assert isinstance(scenario.created_at, datetime)
    
    def test_empty_prompt_raises_error(self):
        with pytest.raises(ValueError, match="Prompt cannot be empty"):
            ProbingScenario(
                title="Test",
                prompt=""
            )
    
    def test_invalid_difficulty_level(self):
        with pytest.raises(ValueError, match="Difficulty level must be between 1 and 5"):
            ProbingScenario(
                title="Test",
                prompt="Test prompt",
                difficulty_level=6
            )


class TestCognitiveHypothesis:
    """Test CognitiveHypothesis data model."""
    
    def test_valid_hypothesis_creation(self):
        hypothesis = CognitiveHypothesis(
            name="Utilitarian Reasoner",
            description="Maximizes overall outcomes",
            cognitive_attributes={"outcome_focused": 0.9, "rule_based": 0.2},
            prior_probability=0.3
        )
        
        assert hypothesis.name == "Utilitarian Reasoner"
        assert hypothesis.cognitive_attributes["outcome_focused"] == 0.9
        assert hypothesis.prior_probability == 0.3
        assert hypothesis.hypothesis_id is not None
    
    def test_empty_name_raises_error(self):
        with pytest.raises(ValueError, match="Hypothesis name cannot be empty"):
            CognitiveHypothesis(name="")
    
    def test_invalid_prior_probability(self):
        with pytest.raises(ValueError, match="Prior probability must be between 0 and 1"):
            CognitiveHypothesis(
                name="Test",
                prior_probability=1.5
            )
    
    def test_invalid_cognitive_attribute(self):
        with pytest.raises(ValueError, match="Cognitive attribute.*must be between 0 and 1"):
            CognitiveHypothesis(
                name="Test",
                cognitive_attributes={"invalid_attr": 1.5}
            )


class TestLLMResponse:
    """Test LLMResponse data model."""
    
    def test_valid_response_creation(self):
        response = LLMResponse(
            scenario_id="test-scenario",
            model_name="test-model",
            raw_response="Test response",
            response_time_ms=150.5
        )
        
        assert response.scenario_id == "test-scenario"
        assert response.model_name == "test-model"
        assert response.raw_response == "Test response"
        assert response.response_time_ms == 150.5
        assert response.response_id is not None
    
    def test_empty_scenario_id_raises_error(self):
        with pytest.raises(ValueError, match="Scenario ID cannot be empty"):
            LLMResponse(scenario_id="", model_name="test")
    
    def test_empty_model_name_raises_error(self):
        with pytest.raises(ValueError, match="Model name cannot be empty"):
            LLMResponse(scenario_id="test", model_name="")
    
    def test_negative_response_time_raises_error(self):
        with pytest.raises(ValueError, match="Response time cannot be negative"):
            LLMResponse(
                scenario_id="test",
                model_name="test",
                response_time_ms=-10
            )


class TestCognitiveProfile:
    """Test CognitiveProfile data model."""
    
    def test_valid_profile_creation(self):
        profile = CognitiveProfile(
            model_name="test-model",
            dominant_patterns={"utilitarian": 0.7, "cautious": 0.3},
            cognitive_scores={"empathy": 0.6, "logic": 0.8},
            scenario_count=25
        )
        
        assert profile.model_name == "test-model"
        assert profile.scenario_count == 25
        assert profile.profile_id is not None
    
    def test_dominant_pattern_property(self):
        profile = CognitiveProfile(
            dominant_patterns={"utilitarian": 0.7, "cautious": 0.3, "analytical": 0.9}
        )
        
        assert profile.dominant_pattern == "analytical"
    
    def test_dominant_pattern_empty(self):
        profile = CognitiveProfile()
        assert profile.dominant_pattern is None
    
    def test_confidence_property(self):
        profile = CognitiveProfile(
            confidence_metrics={"convergence": 0.8, "stability": 0.6}
        )
        
        assert profile.confidence == 0.7  # (0.8 + 0.6) / 2
    
    def test_confidence_empty(self):
        profile = CognitiveProfile()
        assert profile.confidence == 0.0