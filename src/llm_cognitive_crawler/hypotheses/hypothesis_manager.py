"""Hypothesis management system for cognitive analysis."""

from typing import List, Dict, Optional, Set, Tuple
from dataclasses import dataclass, field
import json
from pathlib import Path
from datetime import datetime

from .base import (
    CognitiveHypothesis, 
    HypothesisCategory, 
    HypothesisGenerator,
    HypothesisValidator
)
from .reasoning_hypotheses import ReasoningStyleHypotheses
from .risk_hypotheses import RiskDecisionHypotheses
from .social_hypotheses import SocialCulturalHypotheses
from .bias_hypotheses import BiasLimitationHypotheses
from .domain_hypotheses import DomainSpecificHypotheses
from ..core.data_models import CognitiveDomain


@dataclass
class HypothesisSet:
    """Collection of related hypotheses with metadata."""
    
    name: str
    description: str
    hypotheses: List[CognitiveHypothesis] = field(default_factory=list)
    created_timestamp: str = ""
    version: str = "1.0"
    tags: List[str] = field(default_factory=list)


class HypothesisManager:
    """Manages cognitive hypotheses for LLM analysis."""
    
    def __init__(self):
        self.generators: Dict[HypothesisCategory, HypothesisGenerator] = {
            HypothesisCategory.REASONING_STYLE: ReasoningStyleHypotheses(),
            HypothesisCategory.RISK_DECISION: RiskDecisionHypotheses(),
            HypothesisCategory.SOCIAL_CULTURAL: SocialCulturalHypotheses(),
            HypothesisCategory.BIAS_LIMITATION: BiasLimitationHypotheses(),
            HypothesisCategory.DOMAIN_SPECIFIC: DomainSpecificHypotheses(),
        }
        
        self.validator = HypothesisValidator()
        self.all_hypotheses: List[CognitiveHypothesis] = []
        self.hypothesis_index: Dict[str, CognitiveHypothesis] = {}
        self._initialized = False
    
    def initialize(self) -> None:
        """Initialize all hypothesis generators and build index."""
        if self._initialized:
            return
            
        # Generate all hypotheses
        for category, generator in self.generators.items():
            hypotheses = generator.generate_hypotheses()
            self.all_hypotheses.extend(hypotheses)
        
        # Build index
        self._build_index()
        
        # Fix cross-references
        self._resolve_references()
        
        self._initialized = True
    
    def _build_index(self) -> None:
        """Build index of hypotheses by ID and name."""
        self.hypothesis_index = {}
        
        for hypothesis in self.all_hypotheses:
            # Index by ID
            self.hypothesis_index[hypothesis.hypothesis_id] = hypothesis
            
            # Also index by name (normalized)
            name_key = hypothesis.name.lower().replace(" ", "_") + "_id"
            self.hypothesis_index[name_key] = hypothesis
    
    def _resolve_references(self) -> None:
        """Resolve hypothesis cross-references (contradicts, compatible_with)."""
        for hypothesis in self.all_hypotheses:
            # Resolve contradictions
            resolved_contradicts = []
            for ref in hypothesis.contradicts:
                if ref in self.hypothesis_index:
                    resolved_contradicts.append(self.hypothesis_index[ref].hypothesis_id)
            hypothesis.contradicts = resolved_contradicts
            
            # Resolve compatibilities
            resolved_compatible = []
            for ref in hypothesis.compatible_with:
                if ref in self.hypothesis_index:
                    resolved_compatible.append(self.hypothesis_index[ref].hypothesis_id)
            hypothesis.compatible_with = resolved_compatible
    
    def get_hypothesis(self, hypothesis_id: str) -> Optional[CognitiveHypothesis]:
        """Get a specific hypothesis by ID."""
        if not self._initialized:
            self.initialize()
        return self.hypothesis_index.get(hypothesis_id)
    
    def get_hypotheses_by_category(self, category: HypothesisCategory) -> List[CognitiveHypothesis]:
        """Get all hypotheses in a specific category."""
        if not self._initialized:
            self.initialize()
        return [h for h in self.all_hypotheses if h.category == category]
    
    def get_hypotheses_by_domain(self, domain: CognitiveDomain) -> List[CognitiveHypothesis]:
        """Get all hypotheses applicable to a specific cognitive domain."""
        if not self._initialized:
            self.initialize()
        return [h for h in self.all_hypotheses if h.is_applicable_to_domain(domain)]
    
    def get_hypotheses_by_tags(self, tags: List[str]) -> List[CognitiveHypothesis]:
        """Get hypotheses matching any of the specified tags."""
        if not self._initialized:
            self.initialize()
        tag_set = set(tags)
        return [h for h in self.all_hypotheses if any(t in tag_set for t in h.tags)]
    
    def get_contradictory_hypotheses(self, hypothesis_id: str) -> List[CognitiveHypothesis]:
        """Get all hypotheses that contradict the given hypothesis."""
        if not self._initialized:
            self.initialize()
            
        hypothesis = self.get_hypothesis(hypothesis_id)
        if not hypothesis:
            return []
        
        contradictory = []
        for cont_id in hypothesis.contradicts:
            cont_hyp = self.get_hypothesis(cont_id)
            if cont_hyp:
                contradictory.append(cont_hyp)
        
        return contradictory
    
    def get_compatible_hypotheses(self, hypothesis_id: str) -> List[CognitiveHypothesis]:
        """Get all hypotheses compatible with the given hypothesis."""
        if not self._initialized:
            self.initialize()
            
        hypothesis = self.get_hypothesis(hypothesis_id)
        if not hypothesis:
            return []
        
        compatible = []
        for comp_id in hypothesis.compatible_with:
            comp_hyp = self.get_hypothesis(comp_id)
            if comp_hyp:
                compatible.append(comp_hyp)
        
        return compatible
    
    def validate_hypothesis_set(self, hypotheses: List[CognitiveHypothesis]) -> Dict[str, any]:
        """Validate a set of hypotheses for consistency and coverage."""
        return self.validator.validate_hypothesis_set(hypotheses)
    
    def create_hypothesis_set(
        self, 
        name: str, 
        description: str,
        hypothesis_ids: Optional[List[str]] = None,
        category_filter: Optional[HypothesisCategory] = None,
        domain_filter: Optional[CognitiveDomain] = None,
        tag_filter: Optional[List[str]] = None
    ) -> HypothesisSet:
        """Create a custom hypothesis set based on filters."""
        if not self._initialized:
            self.initialize()
        
        # Start with all hypotheses or specific IDs
        if hypothesis_ids:
            hypotheses = [self.get_hypothesis(hid) for hid in hypothesis_ids]
            hypotheses = [h for h in hypotheses if h is not None]
        else:
            hypotheses = self.all_hypotheses.copy()
        
        # Apply filters
        if category_filter:
            hypotheses = [h for h in hypotheses if h.category == category_filter]
        
        if domain_filter:
            hypotheses = [h for h in hypotheses if h.is_applicable_to_domain(domain_filter)]
        
        if tag_filter:
            tag_set = set(tag_filter)
            hypotheses = [h for h in hypotheses if any(t in tag_set for t in h.tags)]
        
        # Create hypothesis set
        from datetime import datetime
        hypothesis_set = HypothesisSet(
            name=name,
            description=description,
            hypotheses=hypotheses,
            created_timestamp=datetime.now().isoformat(),
            tags=tag_filter or []
        )
        
        return hypothesis_set
    
    def get_hypothesis_predictions(
        self, 
        hypothesis: CognitiveHypothesis,
        scenario_type: str
    ) -> Dict[str, float]:
        """Get all predictions a hypothesis makes for a scenario type."""
        return hypothesis.predicted_response_patterns.get(scenario_type, {})
    
    def find_discriminating_scenarios(
        self,
        hypothesis1_id: str,
        hypothesis2_id: str
    ) -> List[Tuple[str, Dict[str, float], Dict[str, float]]]:
        """Find scenarios that best discriminate between two hypotheses."""
        h1 = self.get_hypothesis(hypothesis1_id)
        h2 = self.get_hypothesis(hypothesis2_id)
        
        if not h1 or not h2:
            return []
        
        discriminating = []
        
        # Find common scenario types
        common_scenarios = set(h1.predicted_response_patterns.keys()) & \
                          set(h2.predicted_response_patterns.keys())
        
        for scenario_type in common_scenarios:
            patterns1 = h1.predicted_response_patterns[scenario_type]
            patterns2 = h2.predicted_response_patterns[scenario_type]
            
            # Calculate total difference
            all_patterns = set(patterns1.keys()) | set(patterns2.keys())
            total_diff = sum(
                abs(patterns1.get(p, 0) - patterns2.get(p, 0))
                for p in all_patterns
            )
            
            if total_diff > 0.3:  # Significant difference threshold
                discriminating.append((scenario_type, patterns1, patterns2))
        
        # Sort by total difference (descending)
        discriminating.sort(key=lambda x: sum(
            abs(x[1].get(p, 0) - x[2].get(p, 0)) 
            for p in set(x[1].keys()) | set(x[2].keys())
        ), reverse=True)
        
        return discriminating
    
    def export_hypotheses(self, filepath: Path, hypothesis_set: Optional[HypothesisSet] = None) -> None:
        """Export hypotheses to JSON file."""
        if not self._initialized:
            self.initialize()
        
        hypotheses = hypothesis_set.hypotheses if hypothesis_set else self.all_hypotheses
        
        export_data = {
            "metadata": {
                "version": "1.0",
                "total_hypotheses": len(hypotheses),
                "categories": list(set(h.category.value for h in hypotheses)),
                "export_timestamp": datetime.now().isoformat()
            },
            "hypotheses": [
                {
                    "hypothesis_id": h.hypothesis_id,
                    "name": h.name,
                    "description": h.description,
                    "category": h.category.value,
                    "predicted_response_patterns": h.predicted_response_patterns,
                    "cognitive_attributes": h.cognitive_attributes,
                    "domain_specificity": [d.value for d in h.domain_specificity],
                    "confidence_intervals": h.confidence_intervals,
                    "prior_probability": h.prior_probability,
                    "tags": h.tags,
                    "contradicts": h.contradicts,
                    "compatible_with": h.compatible_with
                }
                for h in hypotheses
            ]
        }
        
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)
    
    def get_statistics(self) -> Dict[str, any]:
        """Get statistics about the hypothesis collection."""
        if not self._initialized:
            self.initialize()
        
        from collections import Counter
        
        category_counts = Counter(h.category.value for h in self.all_hypotheses)
        
        domain_coverage = {}
        for domain in CognitiveDomain:
            applicable = [h for h in self.all_hypotheses if h.is_applicable_to_domain(domain)]
            domain_coverage[domain.value] = len(applicable)
        
        tag_frequency = Counter()
        for h in self.all_hypotheses:
            tag_frequency.update(h.tags)
        
        return {
            "total_hypotheses": len(self.all_hypotheses),
            "category_distribution": dict(category_counts),
            "domain_coverage": domain_coverage,
            "top_tags": tag_frequency.most_common(20),
            "average_predictions_per_hypothesis": sum(
                len(h.predicted_response_patterns) for h in self.all_hypotheses
            ) / len(self.all_hypotheses) if self.all_hypotheses else 0,
            "average_attributes_per_hypothesis": sum(
                len(h.cognitive_attributes) for h in self.all_hypotheses
            ) / len(self.all_hypotheses) if self.all_hypotheses else 0
        }