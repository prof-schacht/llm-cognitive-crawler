"""Base classes for scenario generation."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union
from enum import Enum
import random
import uuid

from ..core.data_models import ProbingScenario, CognitiveDomain, ResponseType


class DifficultyLevel(Enum):
    """Scenario difficulty levels."""
    BASIC = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4
    RESEARCH = 5


@dataclass
class ScenarioTemplate:
    """Template for generating scenario variations."""
    
    template_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title_template: str = ""
    description_template: str = ""
    prompt_template: str = ""
    domain: CognitiveDomain = CognitiveDomain.LOGICAL_REASONING
    response_type: ResponseType = ResponseType.FREE_TEXT
    difficulty: DifficultyLevel = DifficultyLevel.BASIC
    variables: Dict[str, List[str]] = field(default_factory=dict)
    expected_patterns: Dict[str, float] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def generate_scenario(self, variable_values: Optional[Dict[str, str]] = None) -> ProbingScenario:
        """Generate a concrete scenario from this template."""
        if variable_values is None:
            # Select random values for each variable
            variable_values = {}
            for var_name, var_options in self.variables.items():
                variable_values[var_name] = random.choice(var_options)
        
        # Replace variables in templates
        title = self._replace_variables(self.title_template, variable_values)
        description = self._replace_variables(self.description_template, variable_values)
        prompt = self._replace_variables(self.prompt_template, variable_values)
        
        # Create metadata with template info
        scenario_metadata = {
            "template_id": self.template_id,
            "variable_values": variable_values,
            **self.metadata
        }
        
        return ProbingScenario(
            title=title,
            description=description,
            prompt=prompt,
            domain=self.domain,
            response_type=self.response_type,
            expected_patterns=self.expected_patterns.copy(),
            difficulty_level=self.difficulty.value,
            tags=self.tags.copy(),
            metadata=scenario_metadata
        )
    
    def _replace_variables(self, template: str, variables: Dict[str, str]) -> str:
        """Replace variable placeholders in template string."""
        result = template
        for var_name, var_value in variables.items():
            result = result.replace(f"{{{var_name}}}", var_value)
        return result
    
    def generate_all_variations(self) -> List[ProbingScenario]:
        """Generate all possible combinations of variable values."""
        if not self.variables:
            return [self.generate_scenario()]
        
        # Generate cartesian product of all variable combinations
        import itertools
        
        var_names = list(self.variables.keys())
        var_options = [self.variables[name] for name in var_names]
        
        scenarios = []
        for combination in itertools.product(*var_options):
            variable_values = dict(zip(var_names, combination))
            scenarios.append(self.generate_scenario(variable_values))
        
        return scenarios


class ScenarioGenerator(ABC):
    """Abstract base class for domain-specific scenario generators."""
    
    def __init__(self, domain: CognitiveDomain, random_seed: Optional[int] = None):
        self.domain = domain
        self.templates: List[ScenarioTemplate] = []
        self.generated_scenarios: List[ProbingScenario] = []
        
        if random_seed is not None:
            random.seed(random_seed)
    
    @abstractmethod
    def create_templates(self) -> List[ScenarioTemplate]:
        """Create scenario templates for this domain."""
        pass
    
    def initialize(self) -> None:
        """Initialize the generator with templates."""
        self.templates = self.create_templates()
    
    def generate_scenarios(self, count: Optional[int] = None, 
                         difficulty_filter: Optional[List[DifficultyLevel]] = None,
                         tag_filter: Optional[List[str]] = None) -> List[ProbingScenario]:
        """Generate scenarios based on filters."""
        if not self.templates:
            self.initialize()
        
        # Filter templates
        filtered_templates = self.templates
        
        if difficulty_filter:
            filtered_templates = [t for t in filtered_templates if t.difficulty in difficulty_filter]
        
        if tag_filter:
            filtered_templates = [
                t for t in filtered_templates 
                if any(tag in t.tags for tag in tag_filter)
            ]
        
        # Generate scenarios
        scenarios = []
        for template in filtered_templates:
            template_scenarios = template.generate_all_variations()
            scenarios.extend(template_scenarios)
        
        # Shuffle and limit if count specified
        random.shuffle(scenarios)
        if count is not None:
            scenarios = scenarios[:count]
        
        self.generated_scenarios.extend(scenarios)
        return scenarios
    
    def generate_single_scenario(self, template_id: str, 
                                variable_values: Optional[Dict[str, str]] = None) -> Optional[ProbingScenario]:
        """Generate a single scenario from a specific template."""
        template = self.get_template(template_id)
        if template is None:
            return None
        
        scenario = template.generate_scenario(variable_values)
        self.generated_scenarios.append(scenario)
        return scenario
    
    def get_template(self, template_id: str) -> Optional[ScenarioTemplate]:
        """Get a template by ID."""
        for template in self.templates:
            if template.template_id == template_id:
                return template
        return None
    
    def get_templates_by_difficulty(self, difficulty: DifficultyLevel) -> List[ScenarioTemplate]:
        """Get templates by difficulty level."""
        return [t for t in self.templates if t.difficulty == difficulty]
    
    def get_templates_by_tags(self, tags: List[str]) -> List[ScenarioTemplate]:
        """Get templates that have any of the specified tags."""
        return [
            t for t in self.templates 
            if any(tag in t.tags for tag in tags)
        ]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about generated scenarios."""
        if not self.generated_scenarios:
            return {"total_scenarios": 0}
        
        difficulty_counts = {}
        tag_counts = {}
        response_type_counts = {}
        
        for scenario in self.generated_scenarios:
            # Count by difficulty
            diff = scenario.difficulty_level
            difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1
            
            # Count by response type
            resp_type = scenario.response_type.value
            response_type_counts[resp_type] = response_type_counts.get(resp_type, 0) + 1
            
            # Count by tags
            for tag in scenario.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        return {
            "total_scenarios": len(self.generated_scenarios),
            "total_templates": len(self.templates),
            "difficulty_distribution": difficulty_counts,
            "response_type_distribution": response_type_counts,
            "tag_distribution": tag_counts,
            "domain": self.domain.value
        }
    
    def export_scenarios(self) -> List[Dict[str, Any]]:
        """Export generated scenarios as dictionaries."""
        return [
            {
                "scenario_id": s.scenario_id,
                "title": s.title,
                "description": s.description,
                "prompt": s.prompt,
                "domain": s.domain.value,
                "response_type": s.response_type.value,
                "difficulty_level": s.difficulty_level,
                "tags": s.tags,
                "expected_patterns": s.expected_patterns,
                "metadata": s.metadata
            }
            for s in self.generated_scenarios
        ]