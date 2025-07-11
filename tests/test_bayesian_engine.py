"""Tests for Bayesian inference engine."""

import pytest
from llm_cognitive_crawler.core.bayesian_engine import BayesianEngine
from llm_cognitive_crawler.core.data_models import (
    CognitiveHypothesis,
    ProbingScenario,
    LLMResponse,
    CognitiveDomain,
    ResponseType
)


class TestBayesianEngine:
    """Test Bayesian inference engine."""
    
    @pytest.fixture
    def engine(self):
        return BayesianEngine()
    
    @pytest.fixture
    def sample_hypothesis(self):
        return CognitiveHypothesis(
            name="Utilitarian Reasoner",
            description="Maximizes outcomes",
            predicted_response_patterns={
                "ethical_reasoning_binary_choice": {
                    "yes": 0.8,
                    "pull lever": 0.8,
                    "save more lives": 0.9
                }
            },
            cognitive_attributes={"outcome_focused": 0.9},
            prior_probability=0.3
        )
    
    @pytest.fixture
    def sample_scenario(self):
        return ProbingScenario(
            title="Trolley Problem",
            prompt="Would you pull the lever to save five lives?",
            domain=CognitiveDomain.ETHICAL_REASONING,
            response_type=ResponseType.BINARY_CHOICE
        )
    
    @pytest.fixture
    def sample_response(self, sample_scenario):
        return LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test-model",
            raw_response="Yes, I would pull the lever to save more lives.",
            response_time_ms=100.0
        )
    
    def test_add_hypothesis(self, engine, sample_hypothesis):
        engine.add_hypothesis(sample_hypothesis)
        
        assert sample_hypothesis.hypothesis_id in engine.hypotheses
        assert sample_hypothesis.hypothesis_id in engine.posterior_probabilities
        assert engine.posterior_probabilities[sample_hypothesis.hypothesis_id] == 0.3
    
    def test_remove_hypothesis(self, engine, sample_hypothesis):
        engine.add_hypothesis(sample_hypothesis)
        engine.remove_hypothesis(sample_hypothesis.hypothesis_id)
        
        assert sample_hypothesis.hypothesis_id not in engine.hypotheses
        assert sample_hypothesis.hypothesis_id not in engine.posterior_probabilities
    
    def test_calculate_likelihood_pattern_match(self, engine, sample_hypothesis, sample_scenario, sample_response):
        likelihood = engine.calculate_likelihood(sample_hypothesis, sample_scenario, sample_response)
        
        # Should match one of the patterns (pull lever: 0.8 or save more lives: 0.9)
        assert likelihood in [0.8, 0.9]
    
    def test_calculate_likelihood_no_pattern(self, engine, sample_scenario):
        # Hypothesis with no patterns for this scenario
        hypothesis = CognitiveHypothesis(
            name="Test",
            predicted_response_patterns={}
        )
        
        response = LLMResponse(
            scenario_id=sample_scenario.scenario_id,
            model_name="test",
            raw_response="Some response"
        )
        
        likelihood = engine.calculate_likelihood(hypothesis, sample_scenario, response)
        assert likelihood == 0.5  # Neutral likelihood
    
    def test_update_beliefs_single_hypothesis(self, engine, sample_hypothesis, sample_scenario, sample_response):
        engine.add_hypothesis(sample_hypothesis)
        
        posteriors = engine.update_beliefs(sample_scenario, sample_response)
        
        # With only one hypothesis, posterior should be 1.0
        assert posteriors[sample_hypothesis.hypothesis_id] == 1.0
        assert sample_hypothesis.evidence_count == 1
    
    def test_update_beliefs_multiple_hypotheses(self, engine, sample_scenario, sample_response):
        # Add two competing hypotheses
        h1 = CognitiveHypothesis(
            name="Utilitarian",
            predicted_response_patterns={
                "ethical_reasoning_binary_choice": {"save more lives": 0.9}
            },
            prior_probability=0.4
        )
        
        h2 = CognitiveHypothesis(
            name="Deontological", 
            predicted_response_patterns={
                "ethical_reasoning_binary_choice": {"save more lives": 0.1}
            },
            prior_probability=0.6
        )
        
        engine.add_hypothesis(h1)
        engine.add_hypothesis(h2)
        
        posteriors = engine.update_beliefs(sample_scenario, sample_response)
        
        # Utilitarian should have higher posterior due to better match
        assert posteriors[h1.hypothesis_id] > posteriors[h2.hypothesis_id]
        assert abs(sum(posteriors.values()) - 1.0) < 1e-10  # Should sum to 1
    
    def test_get_most_likely_hypothesis(self, engine, sample_hypothesis):
        engine.add_hypothesis(sample_hypothesis)
        
        most_likely = engine.get_most_likely_hypothesis()
        assert most_likely == sample_hypothesis
    
    def test_get_most_likely_hypothesis_empty(self, engine):
        assert engine.get_most_likely_hypothesis() is None
    
    def test_get_hypothesis_ranking(self, engine):
        h1 = CognitiveHypothesis(name="First", prior_probability=0.6)
        h2 = CognitiveHypothesis(name="Second", prior_probability=0.4)
        
        engine.add_hypothesis(h1)
        engine.add_hypothesis(h2)
        
        ranking = engine.get_hypothesis_ranking()
        
        assert len(ranking) == 2
        assert ranking[0][0].name == "First"  # Higher probability first
        assert ranking[0][1] == 0.6
        assert ranking[1][0].name == "Second"
        assert ranking[1][1] == 0.4
    
    def test_calculate_entropy_uniform(self, engine):
        # Add two hypotheses with equal probability
        h1 = CognitiveHypothesis(name="H1", prior_probability=0.5)
        h2 = CognitiveHypothesis(name="H2", prior_probability=0.5)
        
        engine.add_hypothesis(h1)
        engine.add_hypothesis(h2)
        
        entropy = engine.calculate_entropy()
        assert abs(entropy - 1.0) < 1e-10  # log2(2) = 1
    
    def test_calculate_entropy_certain(self, engine):
        # Single hypothesis (certainty)
        h1 = CognitiveHypothesis(name="H1", prior_probability=1.0)
        engine.add_hypothesis(h1)
        
        entropy = engine.calculate_entropy()
        assert entropy == 0.0
    
    def test_get_convergence_metrics(self, engine, sample_hypothesis):
        engine.add_hypothesis(sample_hypothesis)
        
        metrics = engine.get_convergence_metrics()
        
        assert "entropy" in metrics
        assert "max_posterior" in metrics
        assert "evidence_count" in metrics
        assert "hypothesis_count" in metrics
        assert metrics["hypothesis_count"] == 1
        assert metrics["evidence_count"] == 0
    
    def test_reset_beliefs(self, engine, sample_hypothesis, sample_scenario, sample_response):
        engine.add_hypothesis(sample_hypothesis)
        
        # Update beliefs
        engine.update_beliefs(sample_scenario, sample_response)
        assert sample_hypothesis.evidence_count == 1
        
        # Reset
        engine.reset_beliefs()
        
        assert sample_hypothesis.evidence_count == 0
        assert engine.posterior_probabilities[sample_hypothesis.hypothesis_id] == sample_hypothesis.prior_probability
        assert len(engine.evidence_log) == 0