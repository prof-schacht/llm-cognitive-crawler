"""Base classes and structures for cognitive hypotheses."""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Set
from enum import Enum
import uuid
from abc import ABC, abstractmethod

from ..core.data_models import CognitiveDomain


class HypothesisCategory(Enum):
    """Categories of cognitive hypotheses."""
    REASONING_STYLE = "reasoning_style"
    RISK_DECISION = "risk_decision"
    SOCIAL_CULTURAL = "social_cultural"
    BIAS_LIMITATION = "bias_limitation"
    DOMAIN_SPECIFIC = "domain_specific"
    META_COGNITIVE = "meta_cognitive"


@dataclass
class CognitiveHypothesis:
    """Represents a hypothesis about cognitive patterns in LLMs.
    
    This structure captures predictions about how an LLM with certain
    cognitive characteristics would respond to various scenarios.
    """
    
    hypothesis_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    category: HypothesisCategory = HypothesisCategory.REASONING_STYLE
    
    # Predicted response patterns for different scenario types
    # Format: {scenario_type: {response_pattern: probability}}
    predicted_response_patterns: Dict[str, Dict[str, float]] = field(default_factory=dict)
    
    # Cognitive attributes and their strengths (0-1)
    cognitive_attributes: Dict[str, float] = field(default_factory=dict)
    
    # Which cognitive domains this hypothesis applies to
    domain_specificity: List[CognitiveDomain] = field(default_factory=list)
    
    # Confidence intervals for predictions
    confidence_intervals: Dict[str, Tuple[float, float]] = field(default_factory=dict)
    
    # Prior probability of this hypothesis being true
    prior_probability: float = 0.1
    
    # Tags for categorization and search
    tags: List[str] = field(default_factory=list)
    
    # Contradictory hypotheses (mutually exclusive)
    contradicts: List[str] = field(default_factory=list)
    
    # Compatible hypotheses (can coexist)
    compatible_with: List[str] = field(default_factory=list)
    
    def get_prediction_for_scenario(self, scenario_type: str, response_pattern: str) -> float:
        """Get predicted probability for a specific scenario and response pattern."""
        if scenario_type in self.predicted_response_patterns:
            return self.predicted_response_patterns[scenario_type].get(response_pattern, 0.0)
        return 0.0
    
    def is_applicable_to_domain(self, domain: CognitiveDomain) -> bool:
        """Check if hypothesis applies to a given cognitive domain."""
        return not self.domain_specificity or domain in self.domain_specificity
    
    def get_confidence_interval(self, attribute: str) -> Tuple[float, float]:
        """Get confidence interval for an attribute."""
        return self.confidence_intervals.get(attribute, (0.0, 1.0))


class HypothesisGenerator(ABC):
    """Abstract base class for hypothesis generators."""
    
    def __init__(self, category: HypothesisCategory):
        self.category = category
        self.hypotheses: List[CognitiveHypothesis] = []
    
    @abstractmethod
    def generate_hypotheses(self) -> List[CognitiveHypothesis]:
        """Generate hypotheses for this category."""
        pass
    
    def add_hypothesis(self, hypothesis: CognitiveHypothesis) -> None:
        """Add a hypothesis to the collection."""
        hypothesis.category = self.category
        self.hypotheses.append(hypothesis)
    
    def get_hypotheses(self) -> List[CognitiveHypothesis]:
        """Get all generated hypotheses."""
        if not self.hypotheses:
            self.generate_hypotheses()
        return self.hypotheses
    
    def filter_by_domain(self, domain: CognitiveDomain) -> List[CognitiveHypothesis]:
        """Filter hypotheses applicable to a specific domain."""
        return [h for h in self.get_hypotheses() if h.is_applicable_to_domain(domain)]
    
    def filter_by_tags(self, tags: List[str]) -> List[CognitiveHypothesis]:
        """Filter hypotheses by tags."""
        tag_set = set(tags)
        return [h for h in self.get_hypotheses() if any(t in tag_set for t in h.tags)]


class HypothesisValidator:
    """Validates cognitive hypotheses for consistency and discriminative power."""
    
    def __init__(self):
        self.validation_results: Dict[str, Dict[str, any]] = {}
    
    def validate_hypothesis(self, hypothesis: CognitiveHypothesis) -> Dict[str, any]:
        """Validate a single hypothesis."""
        results = {
            "internal_consistency": self._check_internal_consistency(hypothesis),
            "prediction_coverage": self._check_prediction_coverage(hypothesis),
            "attribute_validity": self._check_attribute_validity(hypothesis),
            "confidence_interval_validity": self._check_confidence_intervals(hypothesis),
        }
        
        self.validation_results[hypothesis.hypothesis_id] = results
        return results
    
    def validate_hypothesis_set(self, hypotheses: List[CognitiveHypothesis]) -> Dict[str, any]:
        """Validate a set of hypotheses for discriminative power and coverage."""
        results = {
            "individual_validity": {h.name: self.validate_hypothesis(h) for h in hypotheses},
            "discriminative_power": self._check_discriminative_power(hypotheses),
            "coverage": self._check_coverage(hypotheses),
            "contradiction_consistency": self._check_contradictions(hypotheses),
        }
        
        return results
    
    def _check_internal_consistency(self, hypothesis: CognitiveHypothesis) -> Dict[str, any]:
        """Check if hypothesis predictions are internally consistent."""
        issues = []
        
        # Check that all probabilities sum to <= 1 for each scenario type
        for scenario_type, patterns in hypothesis.predicted_response_patterns.items():
            total_prob = sum(patterns.values())
            if total_prob > 1.001:  # Allow small floating point errors
                issues.append(f"Probabilities for {scenario_type} sum to {total_prob} > 1")
        
        # Check that cognitive attributes are in valid range
        for attr, value in hypothesis.cognitive_attributes.items():
            if not 0 <= value <= 1:
                issues.append(f"Attribute {attr} has invalid value {value}")
        
        return {
            "is_consistent": len(issues) == 0,
            "issues": issues
        }
    
    def _check_prediction_coverage(self, hypothesis: CognitiveHypothesis) -> Dict[str, any]:
        """Check if hypothesis has sufficient prediction coverage."""
        num_scenario_types = len(hypothesis.predicted_response_patterns)
        num_predictions = sum(len(patterns) for patterns in hypothesis.predicted_response_patterns.values())
        
        return {
            "scenario_types_covered": num_scenario_types,
            "total_predictions": num_predictions,
            "has_sufficient_coverage": num_scenario_types >= 3 and num_predictions >= 5
        }
    
    def _check_attribute_validity(self, hypothesis: CognitiveHypothesis) -> Dict[str, any]:
        """Check if cognitive attributes are valid."""
        num_attributes = len(hypothesis.cognitive_attributes)
        
        return {
            "num_attributes": num_attributes,
            "has_attributes": num_attributes > 0,
            "all_valid_range": all(0 <= v <= 1 for v in hypothesis.cognitive_attributes.values())
        }
    
    def _check_confidence_intervals(self, hypothesis: CognitiveHypothesis) -> Dict[str, any]:
        """Check validity of confidence intervals."""
        issues = []
        
        for attr, (lower, upper) in hypothesis.confidence_intervals.items():
            if lower > upper:
                issues.append(f"Invalid interval for {attr}: [{lower}, {upper}]")
            if not (0 <= lower <= 1 and 0 <= upper <= 1):
                issues.append(f"Interval for {attr} outside [0,1]: [{lower}, {upper}]")
        
        return {
            "all_valid": len(issues) == 0,
            "issues": issues
        }
    
    def _check_discriminative_power(self, hypotheses: List[CognitiveHypothesis]) -> Dict[str, any]:
        """Check if hypotheses make sufficiently different predictions."""
        from itertools import combinations
        
        min_difference_threshold = 0.2
        similar_pairs = []
        
        for h1, h2 in combinations(hypotheses, 2):
            # Compare predictions for common scenario types
            common_scenarios = set(h1.predicted_response_patterns.keys()) & set(h2.predicted_response_patterns.keys())
            
            if common_scenarios:
                total_diff = 0
                num_comparisons = 0
                
                for scenario in common_scenarios:
                    patterns1 = h1.predicted_response_patterns[scenario]
                    patterns2 = h2.predicted_response_patterns[scenario]
                    
                    for pattern in set(patterns1.keys()) | set(patterns2.keys()):
                        p1 = patterns1.get(pattern, 0)
                        p2 = patterns2.get(pattern, 0)
                        total_diff += abs(p1 - p2)
                        num_comparisons += 1
                
                avg_diff = total_diff / num_comparisons if num_comparisons > 0 else 0
                
                if avg_diff < min_difference_threshold:
                    similar_pairs.append((h1.name, h2.name, avg_diff))
        
        return {
            "has_sufficient_discrimination": len(similar_pairs) == 0,
            "similar_pairs": similar_pairs,
            "num_hypotheses": len(hypotheses)
        }
    
    def _check_coverage(self, hypotheses: List[CognitiveHypothesis]) -> Dict[str, any]:
        """Check coverage across domains and categories."""
        domains_covered = set()
        categories_covered = set()
        
        for h in hypotheses:
            if h.domain_specificity:
                domains_covered.update(h.domain_specificity)
            categories_covered.add(h.category)
        
        return {
            "domains_covered": [d.value for d in domains_covered],
            "categories_covered": [c.value for c in categories_covered],
            "num_domains": len(domains_covered),
            "num_categories": len(categories_covered)
        }
    
    def _check_contradictions(self, hypotheses: List[CognitiveHypothesis]) -> Dict[str, any]:
        """Check that contradictory hypotheses are properly marked."""
        issues = []
        hypothesis_dict = {h.hypothesis_id: h for h in hypotheses}
        
        for h in hypotheses:
            for contradicts_id in h.contradicts:
                if contradicts_id in hypothesis_dict:
                    other = hypothesis_dict[contradicts_id]
                    # Check bidirectional contradiction
                    if h.hypothesis_id not in other.contradicts:
                        issues.append(f"{h.name} contradicts {other.name} but not vice versa")
        
        return {
            "has_consistent_contradictions": len(issues) == 0,
            "issues": issues
        }