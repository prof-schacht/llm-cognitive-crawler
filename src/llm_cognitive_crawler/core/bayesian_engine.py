"""Bayesian inference engine for cognitive pattern analysis."""

import numpy as np
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import logging
from .data_models import CognitiveHypothesis, LLMResponse, ProbingScenario


class BayesianEngine:
    """Bayesian inference engine for updating beliefs about LLM cognitive patterns."""
    
    def __init__(self):
        self.hypotheses: Dict[str, CognitiveHypothesis] = {}
        self.posterior_probabilities: Dict[str, float] = {}
        self.evidence_log: List[Tuple[str, str, float]] = []  # (hypothesis_id, scenario_id, likelihood)
        self.logger = logging.getLogger(__name__)
    
    def add_hypothesis(self, hypothesis: CognitiveHypothesis) -> None:
        """Add a cognitive hypothesis to the engine."""
        self.hypotheses[hypothesis.hypothesis_id] = hypothesis
        self.posterior_probabilities[hypothesis.hypothesis_id] = hypothesis.prior_probability
        self.logger.info(f"Added hypothesis: {hypothesis.name}")
    
    def remove_hypothesis(self, hypothesis_id: str) -> None:
        """Remove a hypothesis from the engine."""
        if hypothesis_id in self.hypotheses:
            del self.hypotheses[hypothesis_id]
            del self.posterior_probabilities[hypothesis_id]
            self.logger.info(f"Removed hypothesis: {hypothesis_id}")
    
    def calculate_likelihood(self, hypothesis: CognitiveHypothesis, 
                           scenario: ProbingScenario, 
                           response: LLMResponse) -> float:
        """Calculate likelihood P(response | hypothesis, scenario)."""
        try:
            # Get predicted pattern for this scenario type
            scenario_key = f"{scenario.domain.value}_{scenario.response_type.value}"
            patterns = hypothesis.predicted_response_patterns.get(scenario_key, {})
            
            if not patterns:
                # No specific pattern for this scenario type, use neutral likelihood
                return 0.5
            
            # Simple pattern matching for now - can be extended
            response_text = response.raw_response.lower().strip()
            
            # Calculate likelihood based on pattern matches
            likelihood = 0.5  # Base probability
            
            for pattern, probability in patterns.items():
                if pattern.lower() in response_text:
                    likelihood = probability
                    break
            
            # Adjust for response quality indicators
            if response.confidence_score is not None:
                likelihood = likelihood * response.confidence_score + likelihood * (1 - response.confidence_score) * 0.5
            
            # Ensure likelihood is in valid range
            return max(0.001, min(0.999, likelihood))
            
        except Exception as e:
            self.logger.warning(f"Error calculating likelihood: {e}")
            return 0.5
    
    def update_beliefs(self, scenario: ProbingScenario, response: LLMResponse) -> Dict[str, float]:
        """Update posterior probabilities based on new evidence using Bayes' rule."""
        if not self.hypotheses:
            return {}
        
        # Calculate likelihoods for all hypotheses
        likelihoods = {}
        for hypothesis_id, hypothesis in self.hypotheses.items():
            likelihood = self.calculate_likelihood(hypothesis, scenario, response)
            likelihoods[hypothesis_id] = likelihood
            
            # Log evidence
            self.evidence_log.append((hypothesis_id, scenario.scenario_id, likelihood))
        
        # Apply Bayes' rule: P(H|E) = P(E|H) * P(H) / P(E)
        # where P(E) is the marginal likelihood (normalization constant)
        
        # Calculate unnormalized posteriors
        unnormalized_posteriors = {}
        for hypothesis_id in self.hypotheses:
            prior = self.posterior_probabilities[hypothesis_id]
            likelihood = likelihoods[hypothesis_id]
            unnormalized_posteriors[hypothesis_id] = likelihood * prior
        
        # Normalize to get proper probabilities
        total_evidence = sum(unnormalized_posteriors.values())
        if total_evidence > 0:
            for hypothesis_id in self.hypotheses:
                self.posterior_probabilities[hypothesis_id] = (
                    unnormalized_posteriors[hypothesis_id] / total_evidence
                )
                # Update evidence count
                self.hypotheses[hypothesis_id].evidence_count += 1
        
        self.logger.info(f"Updated beliefs after scenario {scenario.scenario_id}")
        return self.posterior_probabilities.copy()
    
    def get_most_likely_hypothesis(self) -> Optional[CognitiveHypothesis]:
        """Get the hypothesis with highest posterior probability."""
        if not self.posterior_probabilities:
            return None
        
        best_id = max(self.posterior_probabilities, key=self.posterior_probabilities.get)
        return self.hypotheses[best_id]
    
    def get_hypothesis_ranking(self) -> List[Tuple[CognitiveHypothesis, float]]:
        """Get hypotheses ranked by posterior probability."""
        ranked = sorted(
            [(self.hypotheses[h_id], prob) for h_id, prob in self.posterior_probabilities.items()],
            key=lambda x: x[1],
            reverse=True
        )
        return ranked
    
    def calculate_entropy(self) -> float:
        """Calculate entropy of current belief distribution."""
        if not self.posterior_probabilities:
            return 0.0
        
        probs = list(self.posterior_probabilities.values())
        probs = [p for p in probs if p > 0]  # Filter out zero probabilities
        
        if not probs:
            return 0.0
        
        return -sum(p * np.log2(p) for p in probs)
    
    def get_convergence_metrics(self) -> Dict[str, float]:
        """Get metrics indicating belief convergence."""
        max_posterior = max(self.posterior_probabilities.values()) if self.posterior_probabilities else 0.0
        
        return {
            "entropy": self.calculate_entropy(),
            "max_posterior": max_posterior,
            "evidence_count": len(self.evidence_log),
            "hypothesis_count": len(self.hypotheses)
        }
    
    def reset_beliefs(self) -> None:
        """Reset all beliefs to prior probabilities."""
        for hypothesis_id, hypothesis in self.hypotheses.items():
            self.posterior_probabilities[hypothesis_id] = hypothesis.prior_probability
            hypothesis.evidence_count = 0
        
        self.evidence_log.clear()
        self.logger.info("Reset all beliefs to priors")