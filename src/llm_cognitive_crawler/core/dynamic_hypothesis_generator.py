"""Dynamic hypothesis generation for cognitive pattern discovery."""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import json
import re

from .data_models import (
    CognitiveHypothesis, 
    ProbingScenario, 
    LLMResponse, 
    CognitiveDomain,
    ResponseType
)
from ..models.base import LLMProvider


class DynamicHypothesisGenerator:
    """Generates new cognitive hypotheses based on surprising behaviors."""
    
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider
        self.generated_hypotheses: Dict[str, CognitiveHypothesis] = {}
        self.generation_history: List[Dict[str, Any]] = []
        self.logger = logging.getLogger(__name__)
        
        # Templates for hypothesis generation prompts
        self.hypothesis_generation_prompt = """
        As a cognitive scientist analyzing AI behavior, I need help generating a new hypothesis to explain unexpected LLM behavior.

        CONTEXT:
        - Scenario Domain: {domain}
        - Scenario Description: {scenario_description}
        - LLM Response: {response}
        - Why it was surprising: {surprise_context}
        - Current leading hypotheses: {current_hypotheses}

        TASK:
        Generate a new cognitive hypothesis that could explain this unexpected behavior. The hypothesis should:
        1. Have a clear, descriptive name
        2. Include a scientific description of the proposed cognitive pattern
        3. Predict response patterns for different scenario types
        4. Specify cognitive attributes on a 0-1 scale

        FORMAT YOUR RESPONSE AS JSON:
        {{
            "name": "Clear hypothesis name",
            "description": "Scientific description of the cognitive pattern",
            "predicted_patterns": {{
                "ethical_reasoning_binary_choice": {{"utilitarian": 0.8, "deontological": 0.2}},
                "logical_reasoning_free_text": {{"formal_logic": 0.7, "heuristic": 0.3}}
            }},
            "cognitive_attributes": {{
                "risk_tolerance": 0.6,
                "creativity_preference": 0.8,
                "rule_adherence": 0.4,
                "efficiency_focus": 0.7
            }},
            "domain_specificity": ["ethical_reasoning", "social_cognition"],
            "confidence": 0.75
        }}
        """
    
    async def generate_hypothesis(self, 
                                scenario: ProbingScenario,
                                response: LLMResponse,
                                surprise_context: Dict[str, Any],
                                existing_hypotheses: List[CognitiveHypothesis]) -> Optional[CognitiveHypothesis]:
        """Generate a new hypothesis to explain surprising behavior."""
        try:
            # Prepare context for hypothesis generation
            context = self._prepare_generation_context(
                scenario, response, surprise_context, existing_hypotheses
            )
            
            # Generate hypothesis using LLM
            generated_data = await self._query_for_hypothesis(context)
            if not generated_data:
                return None
            
            # Validate and create hypothesis
            hypothesis = self._create_hypothesis_from_data(generated_data, scenario, response)
            if hypothesis:
                self.generated_hypotheses[hypothesis.hypothesis_id] = hypothesis
                self._log_generation(hypothesis, scenario, response, surprise_context)
                self.logger.info(f"Generated new hypothesis: {hypothesis.name}")
            
            return hypothesis
            
        except Exception as e:
            self.logger.error(f"Error generating hypothesis: {e}")
            return None
    
    def _prepare_generation_context(self,
                                  scenario: ProbingScenario,
                                  response: LLMResponse,
                                  surprise_context: Dict[str, Any],
                                  existing_hypotheses: List[CognitiveHypothesis]) -> Dict[str, str]:
        """Prepare context information for hypothesis generation."""
        # Summarize current hypotheses
        current_hypotheses_summary = []
        for hyp in existing_hypotheses[:5]:  # Top 5 hypotheses
            current_hypotheses_summary.append(f"- {hyp.name}: {hyp.description[:100]}...")
        
        # Create surprise explanation
        surprise_explanation = []
        if surprise_context.get("surprise_score", 0) > 2.0:
            surprise_explanation.append(f"High surprise score: {surprise_context['surprise_score']:.2f}")
        
        if surprise_context.get("hypothesis_analysis"):
            low_likelihood_hyps = [
                name for name, analysis in surprise_context["hypothesis_analysis"].items()
                if analysis["likelihood"] < 0.3
            ]
            if low_likelihood_hyps:
                surprise_explanation.append(f"Low likelihood hypotheses: {', '.join(low_likelihood_hyps[:3])}")
        
        return {
            "domain": scenario.domain.value,
            "scenario_description": f"{scenario.title}: {scenario.description}",
            "response": response.raw_response[:200] + "..." if len(response.raw_response) > 200 else response.raw_response,
            "surprise_context": "; ".join(surprise_explanation) if surprise_explanation else "Unexpected response pattern",
            "current_hypotheses": "\n".join(current_hypotheses_summary) if current_hypotheses_summary else "No current hypotheses"
        }
    
    async def _query_for_hypothesis(self, context: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """Query the LLM to generate a new hypothesis."""
        try:
            # Create a temporary scenario for the generation query
            generation_scenario = ProbingScenario(
                title="Hypothesis Generation",
                description="Generate new cognitive hypothesis",
                domain=CognitiveDomain.LOGICAL_REASONING,
                prompt=self.hypothesis_generation_prompt.format(**context),
                response_type=ResponseType.FREE_TEXT
            )
            
            # Query the LLM
            response = await self.llm_provider.query(generation_scenario)
            if not response or not response.raw_response:
                return None
            
            # Parse JSON response
            return self._parse_hypothesis_response(response.raw_response)
            
        except Exception as e:
            self.logger.error(f"Error querying LLM for hypothesis: {e}")
            return None
    
    def _parse_hypothesis_response(self, response_text: str) -> Optional[Dict[str, Any]]:
        """Parse the LLM's JSON response into structured data."""
        try:
            # Extract JSON from response (handles cases where LLM adds extra text)
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if not json_match:
                return None
            
            json_str = json_match.group()
            data = json.loads(json_str)
            
            # Validate required fields
            required_fields = ["name", "description", "cognitive_attributes"]
            if not all(field in data for field in required_fields):
                return None
            
            return data
            
        except (json.JSONDecodeError, ValueError) as e:
            self.logger.warning(f"Failed to parse hypothesis JSON: {e}")
            return None
    
    def _create_hypothesis_from_data(self, 
                                   data: Dict[str, Any], 
                                   scenario: ProbingScenario,
                                   response: LLMResponse) -> Optional[CognitiveHypothesis]:
        """Create a CognitiveHypothesis object from parsed data."""
        try:
            # Parse domain specificity
            domain_specificity = []
            if "domain_specificity" in data:
                for domain_str in data["domain_specificity"]:
                    try:
                        domain = CognitiveDomain(domain_str)
                        domain_specificity.append(domain)
                    except ValueError:
                        continue
            
            # Set prior probability based on confidence
            confidence = data.get("confidence", 0.5)
            prior_probability = max(0.05, min(0.2, confidence * 0.2))  # Scale to reasonable prior range
            
            # Create hypothesis
            hypothesis = CognitiveHypothesis(
                name=data["name"],
                description=data["description"],
                predicted_response_patterns=data.get("predicted_patterns", {}),
                cognitive_attributes=data["cognitive_attributes"],
                domain_specificity=domain_specificity,
                prior_probability=prior_probability,
                metadata={
                    "generated_dynamically": True,
                    "generation_scenario": scenario.scenario_id,
                    "generation_response": response.response_id,
                    "generation_confidence": confidence,
                    "generated_at": datetime.now().isoformat()
                }
            )
            
            return hypothesis
            
        except Exception as e:
            self.logger.error(f"Error creating hypothesis from data: {e}")
            return None
    
    def _log_generation(self, 
                       hypothesis: CognitiveHypothesis,
                       scenario: ProbingScenario,
                       response: LLMResponse,
                       surprise_context: Dict[str, Any]) -> None:
        """Log the hypothesis generation event."""
        generation_record = {
            "timestamp": datetime.now().isoformat(),
            "hypothesis_id": hypothesis.hypothesis_id,
            "hypothesis_name": hypothesis.name,
            "trigger_scenario": scenario.scenario_id,
            "trigger_response": response.response_id,
            "surprise_score": surprise_context.get("surprise_score", 0.0),
            "generation_confidence": hypothesis.metadata.get("generation_confidence", 0.0)
        }
        
        self.generation_history.append(generation_record)
    
    async def validate_hypothesis(self, 
                                hypothesis: CognitiveHypothesis,
                                historical_data: List[Tuple[ProbingScenario, LLMResponse]]) -> Dict[str, float]:
        """Validate a generated hypothesis against historical observations."""
        if not historical_data:
            return {"validation_score": 0.0, "sample_size": 0}
        
        total_likelihood = 0.0
        valid_samples = 0
        
        for scenario, response in historical_data:
            # Calculate likelihood using the hypothesis's predicted patterns
            scenario_key = f"{scenario.domain.value}_{scenario.response_type.value}"
            patterns = hypothesis.predicted_response_patterns.get(scenario_key, {})
            
            if patterns:
                # Simple pattern matching for validation
                response_text = response.raw_response.lower().strip()
                likelihood = 0.5  # Default likelihood
                
                for pattern, probability in patterns.items():
                    if pattern.lower() in response_text:
                        likelihood = probability
                        break
                
                total_likelihood += likelihood
                valid_samples += 1
        
        if valid_samples == 0:
            return {"validation_score": 0.0, "sample_size": 0}
        
        validation_score = total_likelihood / valid_samples
        
        return {
            "validation_score": validation_score,
            "sample_size": valid_samples,
            "average_likelihood": validation_score,
            "confidence_interval": self._calculate_confidence_interval(validation_score, valid_samples)
        }
    
    def _calculate_confidence_interval(self, score: float, sample_size: int) -> Tuple[float, float]:
        """Calculate simple confidence interval for validation score."""
        import math
        
        if sample_size < 2:
            return (0.0, 1.0)
        
        # Simple normal approximation
        std_error = math.sqrt(score * (1 - score) / sample_size)
        margin = 1.96 * std_error  # 95% confidence interval
        
        lower = max(0.0, score - margin)
        upper = min(1.0, score + margin)
        
        return (lower, upper)
    
    def get_generation_statistics(self) -> Dict[str, Any]:
        """Get statistics about hypothesis generation activity."""
        if not self.generation_history:
            return {"total_generated": 0}
        
        total_generated = len(self.generation_history)
        avg_surprise_score = sum(record["surprise_score"] for record in self.generation_history) / total_generated
        avg_confidence = sum(record["generation_confidence"] for record in self.generation_history) / total_generated
        
        # Count generations by domain
        domain_counts = {}
        for record in self.generation_history:
            # We'd need to look up the scenario to get domain, simplified for now
            domain_counts["unknown"] = domain_counts.get("unknown", 0) + 1
        
        return {
            "total_generated": total_generated,
            "average_surprise_score": avg_surprise_score,
            "average_confidence": avg_confidence,
            "domain_distribution": domain_counts,
            "recent_generations": self.generation_history[-5:] if self.generation_history else []
        }