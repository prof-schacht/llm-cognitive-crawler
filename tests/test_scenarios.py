"""Tests for scenario generation framework."""

import pytest
from llm_cognitive_crawler.scenarios import (
    ScenarioGenerator,
    ScenarioTemplate,
    EthicalScenarioGenerator,
    LogicalReasoningGenerator,
    RiskAssessmentGenerator,
    SocialCognitionGenerator,
    ScientificReasoningGenerator,
)
from llm_cognitive_crawler.scenarios.base import DifficultyLevel
from llm_cognitive_crawler.core.data_models import CognitiveDomain, ResponseType


class TestScenarioTemplate:
    """Test ScenarioTemplate functionality."""
    
    def test_template_creation(self):
        """Test creating a scenario template."""
        template = ScenarioTemplate(
            title_template="Test {variable}",
            description_template="Testing {variable} scenario",
            prompt_template="What about {variable}?",
            domain=CognitiveDomain.LOGICAL_REASONING,
            response_type=ResponseType.FREE_TEXT,
            difficulty=DifficultyLevel.BASIC,
            variables={"variable": ["A", "B", "C"]},
            expected_patterns={"test": 0.5},
            tags=["test", "example"]
        )
        
        assert template.title_template == "Test {variable}"
        assert len(template.variables["variable"]) == 3
        assert template.difficulty == DifficultyLevel.BASIC
    
    def test_scenario_generation_from_template(self):
        """Test generating concrete scenarios from template."""
        template = ScenarioTemplate(
            title_template="Trolley with {victims} people",
            prompt_template="Save {victims} by sacrificing {sacrifice}?",
            domain=CognitiveDomain.ETHICAL_REASONING,
            variables={
                "victims": ["five", "ten"],
                "sacrifice": ["one", "two"]
            }
        )
        
        # Test specific variable values
        scenario = template.generate_scenario({"victims": "five", "sacrifice": "one"})
        
        assert scenario.title == "Trolley with five people"
        assert "Save five by sacrificing one?" in scenario.prompt
        assert scenario.domain == CognitiveDomain.ETHICAL_REASONING
        assert scenario.metadata["template_id"] == template.template_id
    
    def test_all_variations_generation(self):
        """Test generating all possible variations."""
        template = ScenarioTemplate(
            title_template="Test",
            prompt_template="{var1} and {var2}",
            variables={
                "var1": ["A", "B"],
                "var2": ["X", "Y", "Z"]
            }
        )
        
        variations = template.generate_all_variations()
        
        # Should have 2 * 3 = 6 variations
        assert len(variations) == 6
        
        # Check all combinations exist
        prompts = [s.prompt for s in variations]
        assert "A and X" in prompts
        assert "B and Z" in prompts


class TestEthicalScenarioGenerator:
    """Test ethical reasoning scenario generation."""
    
    @pytest.fixture
    def generator(self):
        return EthicalScenarioGenerator(random_seed=42)
    
    def test_initialization(self, generator):
        """Test generator initialization."""
        assert generator.domain == CognitiveDomain.ETHICAL_REASONING
        assert len(generator.templates) == 0  # Not initialized yet
    
    def test_template_creation(self, generator):
        """Test that templates are created properly."""
        generator.initialize()
        
        assert len(generator.templates) > 0
        
        # Check template categories
        template_tags = []
        for template in generator.templates:
            template_tags.extend(template.tags)
        
        # Should have templates for each category
        assert "trolley" in template_tags
        assert "allocation" in template_tags
        assert "harm" in template_tags
        assert "rights" in template_tags
        assert "cultural" in template_tags
    
    def test_scenario_generation(self, generator):
        """Test generating scenarios."""
        scenarios = generator.generate_scenarios(count=10)
        
        assert len(scenarios) == 10
        assert all(s.domain == CognitiveDomain.ETHICAL_REASONING for s in scenarios)
        assert all(s.prompt for s in scenarios)  # All have prompts
    
    def test_difficulty_filtering(self, generator):
        """Test filtering by difficulty."""
        generator.initialize()
        
        # Get only basic scenarios
        basic_scenarios = generator.generate_scenarios(
            difficulty_filter=[DifficultyLevel.BASIC]
        )
        
        if basic_scenarios:  # Only test if we have basic scenarios
            assert all(s.difficulty_level == 1 for s in basic_scenarios)
    
    def test_tag_filtering(self, generator):
        """Test filtering by tags."""
        generator.initialize()
        
        # Get only trolley problem scenarios
        trolley_scenarios = generator.generate_scenarios(
            tag_filter=["trolley"]
        )
        
        if trolley_scenarios:  # Only test if we have trolley scenarios
            assert all("trolley" in s.tags for s in trolley_scenarios)
    
    def test_statistics(self, generator):
        """Test statistics generation."""
        scenarios = generator.generate_scenarios(count=20)
        stats = generator.get_statistics()
        
        assert stats["total_scenarios"] == 20
        assert stats["domain"] == "ethical_reasoning"
        assert "difficulty_distribution" in stats
        assert "tag_distribution" in stats


class TestLogicalReasoningGenerator:
    """Test logical reasoning scenario generation."""
    
    @pytest.fixture
    def generator(self):
        return LogicalReasoningGenerator(random_seed=42)
    
    def test_logical_categories(self, generator):
        """Test that all logical reasoning categories are covered."""
        generator.initialize()
        
        template_tags = []
        for template in generator.templates:
            template_tags.extend(template.tags)
        
        # Check for main categories
        assert "syllogism" in template_tags
        assert "probability" in template_tags
        assert "causal" in template_tags
        assert "counterfactual" in template_tags
        assert "fallacy" in template_tags
    
    def test_response_types(self, generator):
        """Test variety of response types."""
        scenarios = generator.generate_scenarios(count=30)
        
        response_types = {s.response_type for s in scenarios}
        
        # Should have multiple response types
        assert len(response_types) > 1
        assert ResponseType.FREE_TEXT in response_types


class TestRiskAssessmentGenerator:
    """Test risk assessment scenario generation."""
    
    @pytest.fixture
    def generator(self):
        return RiskAssessmentGenerator(random_seed=42)
    
    def test_risk_categories(self, generator):
        """Test risk assessment categories."""
        generator.initialize()
        
        template_tags = []
        for template in generator.templates:
            template_tags.extend(template.tags)
        
        # Check for main categories
        assert "financial" in template_tags
        assert "medical" in template_tags
        assert "safety" in template_tags
        assert "uncertainty" in template_tags
    
    def test_expected_patterns(self, generator):
        """Test that scenarios have expected patterns."""
        scenarios = generator.generate_scenarios(count=10)
        
        for scenario in scenarios:
            assert isinstance(scenario.expected_patterns, dict)
            # All scenarios should have some expected patterns
            assert len(scenario.expected_patterns) > 0
            # Values should be probabilities between 0 and 1
            for value in scenario.expected_patterns.values():
                assert 0 <= value <= 1


class TestSocialCognitionGenerator:
    """Test social cognition scenario generation."""
    
    @pytest.fixture
    def generator(self):
        return SocialCognitionGenerator(random_seed=42)
    
    def test_social_categories(self, generator):
        """Test social cognition categories."""
        generator.initialize()
        
        template_tags = []
        for template in generator.templates:
            template_tags.extend(template.tags)
        
        # Check for main categories
        assert "theory_of_mind" in template_tags
        assert "empathy" in template_tags
        assert "fairness" in template_tags
        # Check for cultural-related tags (various forms)
        assert any("cultural" in tag for tag in template_tags)


class TestScientificReasoningGenerator:
    """Test scientific reasoning scenario generation."""
    
    @pytest.fixture 
    def generator(self):
        return ScientificReasoningGenerator(random_seed=42)
    
    def test_scientific_categories(self, generator):
        """Test scientific reasoning categories."""
        generator.initialize()
        
        template_tags = []
        for template in generator.templates:
            template_tags.extend(template.tags)
        
        # Check for main categories
        assert "hypothesis" in template_tags
        assert "correlation" in template_tags
        assert "causation" in template_tags
        assert "experimental_design" in template_tags
    
    def test_causal_domain(self, generator):
        """Test that domain is set correctly."""
        assert generator.domain == CognitiveDomain.CAUSAL_REASONING
        
        scenarios = generator.generate_scenarios(count=5)
        assert all(s.domain == CognitiveDomain.CAUSAL_REASONING for s in scenarios)


class TestScenarioExport:
    """Test scenario export functionality."""
    
    def test_export_format(self):
        """Test exporting scenarios to dictionary format."""
        generator = EthicalScenarioGenerator()
        scenarios = generator.generate_scenarios(count=5)
        
        exported = generator.export_scenarios()
        
        assert len(exported) == 5
        
        for scenario_dict in exported:
            assert "scenario_id" in scenario_dict
            assert "title" in scenario_dict
            assert "prompt" in scenario_dict
            assert "domain" in scenario_dict
            assert "response_type" in scenario_dict
            assert "difficulty_level" in scenario_dict
            assert "tags" in scenario_dict
            assert "expected_patterns" in scenario_dict
            assert "metadata" in scenario_dict


class TestScenarioCount:
    """Test that we generate 200+ scenarios as required."""
    
    def test_total_scenario_count(self):
        """Verify we can generate 200+ scenarios across all domains."""
        generators = [
            EthicalScenarioGenerator(),
            LogicalReasoningGenerator(),
            RiskAssessmentGenerator(),
            SocialCognitionGenerator(),
            ScientificReasoningGenerator(),
        ]
        
        total_scenarios = 0
        
        for generator in generators:
            generator.initialize()
            # Count potential scenarios from templates
            for template in generator.templates:
                if template.variables:
                    # Count all possible variations
                    num_variations = 1
                    for var_options in template.variables.values():
                        num_variations *= len(var_options)
                    total_scenarios += num_variations
                else:
                    total_scenarios += 1
        
        # Should be able to generate well over 200 scenarios
        assert total_scenarios >= 200
        
        # Verify we can actually generate them
        all_scenarios = []
        for generator in generators:
            scenarios = generator.generate_scenarios(count=50)  # 50 from each
            all_scenarios.extend(scenarios)
        
        assert len(all_scenarios) >= 200  # 5 * 50 = 250


class TestScenarioQuality:
    """Test quality aspects of generated scenarios."""
    
    def test_scenario_completeness(self):
        """Test that all scenarios have required fields."""
        generator = EthicalScenarioGenerator()
        scenarios = generator.generate_scenarios(count=20)
        
        for scenario in scenarios:
            # Required fields
            assert scenario.scenario_id
            assert scenario.title
            assert scenario.prompt
            assert scenario.domain
            assert scenario.response_type
            assert 1 <= scenario.difficulty_level <= 5
            
            # Should have some expected patterns
            assert isinstance(scenario.expected_patterns, dict)
            assert len(scenario.expected_patterns) > 0
            
            # Should have metadata from template
            assert "template_id" in scenario.metadata
            assert "variable_values" in scenario.metadata
    
    def test_scenario_uniqueness(self):
        """Test that generated scenarios are unique."""
        generator = LogicalReasoningGenerator()
        scenarios = generator.generate_scenarios(count=30)
        
        # Check uniqueness of prompts
        prompts = [s.prompt for s in scenarios]
        assert len(prompts) == len(set(prompts))
        
        # Check uniqueness of IDs
        ids = [s.scenario_id for s in scenarios]
        assert len(ids) == len(set(ids))