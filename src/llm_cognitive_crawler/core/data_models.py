"""Core data models for cognitive analysis."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from enum import Enum
import uuid


class CognitiveDomain(Enum):
    """Cognitive domains for analysis."""
    ETHICAL_REASONING = "ethical_reasoning"
    LOGICAL_REASONING = "logical_reasoning"
    RISK_ASSESSMENT = "risk_assessment"
    SOCIAL_COGNITION = "social_cognition"
    CAUSAL_REASONING = "causal_reasoning"


class ResponseType(Enum):
    """Types of expected responses."""
    BINARY_CHOICE = "binary_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    LIKERT_SCALE = "likert_scale"
    FREE_TEXT = "free_text"
    NUMERICAL = "numerical"


@dataclass
class ProbingScenario:
    """A cognitive probing scenario for testing LLM reasoning patterns."""
    
    scenario_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    domain: CognitiveDomain = CognitiveDomain.LOGICAL_REASONING
    prompt: str = ""
    response_type: ResponseType = ResponseType.FREE_TEXT
    expected_patterns: Dict[str, float] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    difficulty_level: int = 1  # 1-5 scale
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validate scenario data."""
        if not self.prompt:
            raise ValueError("Prompt cannot be empty")
        if self.difficulty_level < 1 or self.difficulty_level > 5:
            raise ValueError("Difficulty level must be between 1 and 5")


@dataclass 
class CognitiveHypothesis:
    """A hypothesis about LLM cognitive patterns and reasoning style."""
    
    hypothesis_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    description: str = ""
    predicted_response_patterns: Dict[str, Dict[str, float]] = field(default_factory=dict)
    cognitive_attributes: Dict[str, float] = field(default_factory=dict)
    domain_specificity: List[CognitiveDomain] = field(default_factory=list)
    confidence_intervals: Dict[str, Tuple[float, float]] = field(default_factory=dict)
    prior_probability: float = 0.1
    evidence_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validate hypothesis data."""
        if not self.name:
            raise ValueError("Hypothesis name cannot be empty")
        if not 0 <= self.prior_probability <= 1:
            raise ValueError("Prior probability must be between 0 and 1")
        
        # Validate cognitive attributes are between 0 and 1
        for attr, value in self.cognitive_attributes.items():
            if not 0 <= value <= 1:
                raise ValueError(f"Cognitive attribute '{attr}' must be between 0 and 1")


@dataclass
class LLMResponse:
    """A response from an LLM to a probing scenario."""
    
    response_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    scenario_id: str = ""
    model_name: str = ""
    model_version: str = ""
    raw_response: str = ""
    parsed_response: Optional[Any] = None
    response_time_ms: float = 0.0
    token_count: Optional[int] = None
    confidence_score: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validate response data."""
        if not self.scenario_id:
            raise ValueError("Scenario ID cannot be empty")
        if not self.model_name:
            raise ValueError("Model name cannot be empty")
        if self.response_time_ms < 0:
            raise ValueError("Response time cannot be negative")


@dataclass
class CognitiveProfile:
    """A cognitive profile of an LLM based on analysis results."""
    
    profile_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    model_name: str = ""
    model_version: str = ""
    dominant_patterns: Dict[str, float] = field(default_factory=dict)
    cognitive_scores: Dict[str, float] = field(default_factory=dict)
    bias_indicators: Dict[str, float] = field(default_factory=dict)
    confidence_metrics: Dict[str, float] = field(default_factory=dict)
    scenario_count: int = 0
    analysis_timestamp: datetime = field(default_factory=datetime.now)
    
    @property
    def dominant_pattern(self) -> Optional[str]:
        """Get the most dominant cognitive pattern."""
        if not self.dominant_patterns:
            return None
        return max(self.dominant_patterns, key=self.dominant_patterns.get)
    
    @property
    def confidence(self) -> float:
        """Get overall confidence in the profile."""
        if not self.confidence_metrics:
            return 0.0
        return sum(self.confidence_metrics.values()) / len(self.confidence_metrics)