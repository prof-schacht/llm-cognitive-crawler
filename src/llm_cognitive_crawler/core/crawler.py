"""Main LLM Cognitive Crawler implementation."""

import asyncio
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

from .data_models import (
    ProbingScenario, 
    CognitiveHypothesis, 
    LLMResponse, 
    CognitiveProfile,
    CognitiveDomain
)
from .bayesian_engine import BayesianEngine
from .dynamic_hypothesis_generator import DynamicHypothesisGenerator
from ..models.base import LLMProvider


class LLMCognitiveCrawler:
    """Main orchestrator for LLM cognitive pattern analysis."""
    
    def __init__(self, llm_provider: LLMProvider, **kwargs):
        self.llm_provider = llm_provider
        self.bayesian_engine = BayesianEngine()
        self.scenarios: Dict[str, ProbingScenario] = {}
        self.responses: Dict[str, LLMResponse] = {}
        self.config = kwargs
        self.logger = logging.getLogger(__name__)
        
        # Dynamic hypothesis generation (Phase 1 extension)
        self.enable_dynamic_hypotheses = kwargs.get('enable_dynamic_hypotheses', True)
        self.surprise_threshold = kwargs.get('surprise_threshold', 2.0)
        self.dynamic_generator = DynamicHypothesisGenerator(llm_provider) if self.enable_dynamic_hypotheses else None
        
        # Set up logging
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)
    
    def add_scenario(self, scenario: ProbingScenario) -> None:
        """Add a probing scenario to the crawler."""
        self.scenarios[scenario.scenario_id] = scenario
        self.logger.info(f"Added scenario: {scenario.title}")
    
    def add_scenarios(self, scenarios: List[ProbingScenario]) -> None:
        """Add multiple probing scenarios."""
        for scenario in scenarios:
            self.add_scenario(scenario)
    
    def add_hypothesis(self, hypothesis: CognitiveHypothesis) -> None:
        """Add a cognitive hypothesis to the analysis."""
        self.bayesian_engine.add_hypothesis(hypothesis)
    
    def add_hypotheses(self, hypotheses: List[CognitiveHypothesis]) -> None:
        """Add multiple cognitive hypotheses."""
        for hypothesis in hypotheses:
            self.add_hypothesis(hypothesis)
    
    async def run_scenario(self, scenario_id: str, **kwargs) -> Optional[LLMResponse]:
        """Run a single probing scenario."""
        if scenario_id not in self.scenarios:
            self.logger.error(f"Scenario not found: {scenario_id}")
            return None
        
        scenario = self.scenarios[scenario_id]
        self.logger.info(f"Running scenario: {scenario.title}")
        
        try:
            response = await self.llm_provider.query(scenario, **kwargs)
            self.responses[response.response_id] = response
            
            # Check for surprises before updating beliefs (Dynamic Extension)
            if self.enable_dynamic_hypotheses and self.dynamic_generator:
                await self._handle_surprise_detection(scenario, response)
            
            # Update Bayesian beliefs
            self.bayesian_engine.update_beliefs(scenario, response)
            
            return response
            
        except Exception as e:
            self.logger.error(f"Error running scenario {scenario_id}: {e}")
            return None
    
    async def run_scenarios(self, scenario_ids: Optional[List[str]] = None, 
                          max_concurrent: int = 3, **kwargs) -> List[LLMResponse]:
        """Run multiple scenarios, potentially in parallel."""
        if scenario_ids is None:
            scenario_ids = list(self.scenarios.keys())
        
        # Filter valid scenario IDs
        valid_ids = [sid for sid in scenario_ids if sid in self.scenarios]
        
        self.logger.info(f"Running {len(valid_ids)} scenarios with max_concurrent={max_concurrent}")
        
        # Create semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def run_with_semaphore(scenario_id: str) -> Optional[LLMResponse]:
            async with semaphore:
                return await self.run_scenario(scenario_id, **kwargs)
        
        # Run scenarios concurrently
        tasks = [run_with_semaphore(sid) for sid in valid_ids]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out None and exception responses
        valid_responses = [r for r in responses if isinstance(r, LLMResponse)]
        
        self.logger.info(f"Completed {len(valid_responses)} scenarios successfully")
        return valid_responses
    
    async def run_comprehensive_analysis(self, max_concurrent: int = 3, **kwargs) -> Dict[str, Any]:
        """Run a comprehensive analysis across all scenarios and hypotheses."""
        if not self.scenarios:
            raise ValueError("No scenarios available for analysis")
        
        if not self.bayesian_engine.hypotheses:
            raise ValueError("No hypotheses available for analysis")
        
        self.logger.info("Starting comprehensive cognitive analysis")
        
        # Run all scenarios
        responses = await self.run_scenarios(max_concurrent=max_concurrent, **kwargs)
        
        # Generate analysis results
        results = {
            "model_info": self.llm_provider.get_model_info(),
            "analysis_timestamp": datetime.now(),
            "scenarios_run": len(responses),
            "total_scenarios": len(self.scenarios),
            "hypothesis_rankings": self.bayesian_engine.get_hypothesis_ranking(),
            "convergence_metrics": self.bayesian_engine.get_convergence_metrics(),
            "most_likely_hypothesis": self.bayesian_engine.get_most_likely_hypothesis(),
            "responses": responses
        }
        
        self.logger.info("Comprehensive analysis completed")
        return results
    
    def generate_cognitive_profile(self) -> CognitiveProfile:
        """Generate a cognitive profile based on current analysis."""
        if not self.bayesian_engine.hypotheses:
            raise ValueError("No hypotheses available for profile generation")
        
        # Get hypothesis rankings
        rankings = self.bayesian_engine.get_hypothesis_ranking()
        
        # Extract dominant patterns
        dominant_patterns = {
            hyp.name: prob for hyp, prob in rankings[:5]  # Top 5 patterns
        }
        
        # Calculate cognitive scores by averaging hypothesis attributes
        cognitive_scores = {}
        for hypothesis, prob in rankings:
            for attr, value in hypothesis.cognitive_attributes.items():
                if attr not in cognitive_scores:
                    cognitive_scores[attr] = 0.0
                cognitive_scores[attr] += value * prob
        
        # Get convergence metrics as confidence metrics
        confidence_metrics = self.bayesian_engine.get_convergence_metrics()
        
        return CognitiveProfile(
            model_name=self.llm_provider.model_name,
            model_version=self.llm_provider.get_model_info().get("model_name", "unknown"),
            dominant_patterns=dominant_patterns,
            cognitive_scores=cognitive_scores,
            confidence_metrics=confidence_metrics,
            scenario_count=len(self.responses)
        )
    
    def get_scenario_by_domain(self, domain: CognitiveDomain) -> List[ProbingScenario]:
        """Get all scenarios for a specific cognitive domain."""
        return [s for s in self.scenarios.values() if s.domain == domain]
    
    def get_responses_by_scenario(self, scenario_id: str) -> List[LLMResponse]:
        """Get all responses for a specific scenario."""
        return [r for r in self.responses.values() if r.scenario_id == scenario_id]
    
    def export_results(self) -> Dict[str, Any]:
        """Export all results for persistence or analysis."""
        return {
            "scenarios": {sid: {
                "title": s.title,
                "domain": s.domain.value,
                "prompt": s.prompt,
                "metadata": s.metadata
            } for sid, s in self.scenarios.items()},
            "hypotheses": {hid: {
                "name": h.name,
                "description": h.description,
                "attributes": h.cognitive_attributes,
                "prior": h.prior_probability,
                "evidence_count": h.evidence_count
            } for hid, h in self.bayesian_engine.hypotheses.items()},
            "posterior_probabilities": self.bayesian_engine.posterior_probabilities,
            "responses": {rid: {
                "scenario_id": r.scenario_id,
                "model_name": r.model_name,
                "response": r.raw_response,
                "response_time_ms": r.response_time_ms,
                "timestamp": r.timestamp.isoformat()
            } for rid, r in self.responses.items()},
            "convergence_metrics": self.bayesian_engine.get_convergence_metrics()
        }
    
    async def _handle_surprise_detection(self, scenario: ProbingScenario, response: LLMResponse) -> None:
        """Handle surprise detection and dynamic hypothesis generation (Phase 1 Extension)."""
        try:
            # Check if response is surprising
            if self.bayesian_engine.is_surprising(scenario, response, self.surprise_threshold):
                self.logger.info(f"Surprising response detected for scenario {scenario.scenario_id}")
                
                # Get surprise context for hypothesis generation
                surprise_context = self.bayesian_engine.get_surprise_context(scenario, response)
                
                # Get current top hypotheses for context
                existing_hypotheses = [hyp for hyp, _ in self.bayesian_engine.get_hypothesis_ranking()]
                
                # Generate new hypothesis
                new_hypothesis = await self.dynamic_generator.generate_hypothesis(
                    scenario, response, surprise_context, existing_hypotheses
                )
                
                if new_hypothesis:
                    # Validate hypothesis against historical data
                    historical_data = self._get_historical_data_for_validation()
                    validation_results = await self.dynamic_generator.validate_hypothesis(
                        new_hypothesis, historical_data
                    )
                    
                    # Add hypothesis if validation passes threshold
                    validation_threshold = 0.4  # Configurable threshold
                    if validation_results.get("validation_score", 0) > validation_threshold:
                        self.add_hypothesis(new_hypothesis)
                        self.logger.info(f"Added validated dynamic hypothesis: {new_hypothesis.name}")
                    else:
                        self.logger.info(f"Dynamic hypothesis rejected due to low validation score: {validation_results.get('validation_score', 0):.3f}")
                
        except Exception as e:
            self.logger.error(f"Error in surprise detection: {e}")
    
    def _get_historical_data_for_validation(self) -> List[Tuple[ProbingScenario, LLMResponse]]:
        """Get historical scenario-response pairs for hypothesis validation."""
        historical_data = []
        for response in self.responses.values():
            if response.scenario_id in self.scenarios:
                scenario = self.scenarios[response.scenario_id]
                historical_data.append((scenario, response))
        return historical_data
    
    def get_dynamic_generation_stats(self) -> Dict[str, Any]:
        """Get statistics about dynamic hypothesis generation activity."""
        if not self.enable_dynamic_hypotheses or not self.dynamic_generator:
            return {"dynamic_generation_enabled": False}
        
        stats = self.dynamic_generator.get_generation_statistics()
        stats["dynamic_generation_enabled"] = True
        stats["surprise_threshold"] = self.surprise_threshold
        return stats
    
    def set_surprise_threshold(self, threshold: float) -> None:
        """Set the surprise threshold for dynamic hypothesis generation."""
        if not 0.5 <= threshold <= 10.0:
            raise ValueError("Surprise threshold must be between 0.5 and 10.0")
        
        self.surprise_threshold = threshold
        self.logger.info(f"Updated surprise threshold to {threshold}")
    
    def get_generated_hypotheses(self) -> List[CognitiveHypothesis]:
        """Get all dynamically generated hypotheses."""
        if not self.dynamic_generator:
            return []
        
        return list(self.dynamic_generator.generated_hypotheses.values())

    async def close(self) -> None:
        """Clean up resources."""
        if hasattr(self.llm_provider, 'close'):
            await self.llm_provider.close()
        self.logger.info("Crawler closed")