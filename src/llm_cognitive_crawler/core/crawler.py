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
    
    async def close(self) -> None:
        """Clean up resources."""
        if hasattr(self.llm_provider, 'close'):
            await self.llm_provider.close()
        self.logger.info("Crawler closed")