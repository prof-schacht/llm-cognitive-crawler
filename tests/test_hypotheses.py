"""Tests for cognitive hypothesis framework."""

import pytest
from llm_cognitive_crawler.hypotheses import (
    CognitiveHypothesis,
    HypothesisCategory,
    HypothesisValidator,
    HypothesisManager,
    HypothesisSet,
    ReasoningStyleHypotheses,
    RiskDecisionHypotheses,
    SocialCulturalHypotheses,
    BiasLimitationHypotheses,
    DomainSpecificHypotheses,
)
from llm_cognitive_crawler.core.data_models import CognitiveDomain


class TestCognitiveHypothesis:
    """Test CognitiveHypothesis data structure."""
    
    def test_hypothesis_creation(self):
        """Test creating a cognitive hypothesis."""
        hypothesis = CognitiveHypothesis(
            name="Test Hypothesis",
            description="A test hypothesis",
            category=HypothesisCategory.REASONING_STYLE,
            predicted_response_patterns={
                "scenario_a": {"response_1": 0.8, "response_2": 0.2},
                "scenario_b": {"response_x": 0.6, "response_y": 0.4}
            },
            cognitive_attributes={
                "attribute_1": 0.9,
                "attribute_2": 0.3
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING],
            prior_probability=0.15,
            tags=["test", "example"]
        )
        
        assert hypothesis.name == "Test Hypothesis"
        assert hypothesis.category == HypothesisCategory.REASONING_STYLE
        assert len(hypothesis.predicted_response_patterns) == 2
        assert len(hypothesis.cognitive_attributes) == 2
        assert hypothesis.prior_probability == 0.15
    
    def test_get_prediction_for_scenario(self):
        """Test getting predictions for specific scenarios."""
        hypothesis = CognitiveHypothesis(
            predicted_response_patterns={
                "trolley": {"pull": 0.8, "dont_pull": 0.2}
            }
        )
        
        assert hypothesis.get_prediction_for_scenario("trolley", "pull") == 0.8
        assert hypothesis.get_prediction_for_scenario("trolley", "dont_pull") == 0.2
        assert hypothesis.get_prediction_for_scenario("unknown", "any") == 0.0
        assert hypothesis.get_prediction_for_scenario("trolley", "unknown") == 0.0
    
    def test_domain_applicability(self):
        """Test checking domain applicability."""
        # Hypothesis with specific domains
        hypothesis1 = CognitiveHypothesis(
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING, CognitiveDomain.SOCIAL_COGNITION]
        )
        
        assert hypothesis1.is_applicable_to_domain(CognitiveDomain.ETHICAL_REASONING)
        assert hypothesis1.is_applicable_to_domain(CognitiveDomain.SOCIAL_COGNITION)
        assert not hypothesis1.is_applicable_to_domain(CognitiveDomain.LOGICAL_REASONING)
        
        # Hypothesis with no domain restrictions
        hypothesis2 = CognitiveHypothesis(domain_specificity=[])
        assert hypothesis2.is_applicable_to_domain(CognitiveDomain.ETHICAL_REASONING)
        assert hypothesis2.is_applicable_to_domain(CognitiveDomain.LOGICAL_REASONING)


class TestHypothesisValidator:
    """Test hypothesis validation functionality."""
    
    @pytest.fixture
    def validator(self):
        return HypothesisValidator()
    
    def test_internal_consistency_valid(self, validator):
        """Test validation of internally consistent hypothesis."""
        hypothesis = CognitiveHypothesis(
            predicted_response_patterns={
                "scenario": {"response_a": 0.6, "response_b": 0.4}
            },
            cognitive_attributes={
                "attr1": 0.5,
                "attr2": 0.8
            }
        )
        
        result = validator._check_internal_consistency(hypothesis)
        assert result["is_consistent"]
        assert len(result["issues"]) == 0
    
    def test_internal_consistency_invalid_probabilities(self, validator):
        """Test detection of invalid probability sums."""
        hypothesis = CognitiveHypothesis(
            predicted_response_patterns={
                "scenario": {"response_a": 0.7, "response_b": 0.6}  # Sum > 1
            }
        )
        
        result = validator._check_internal_consistency(hypothesis)
        assert not result["is_consistent"]
        assert len(result["issues"]) > 0
        assert "sum to" in result["issues"][0]
    
    def test_internal_consistency_invalid_attributes(self, validator):
        """Test detection of invalid attribute values."""
        hypothesis = CognitiveHypothesis(
            cognitive_attributes={
                "valid": 0.5,
                "invalid": 1.5  # > 1
            }
        )
        
        result = validator._check_internal_consistency(hypothesis)
        assert not result["is_consistent"]
        assert any("invalid value" in issue for issue in result["issues"])
    
    def test_prediction_coverage(self, validator):
        """Test checking prediction coverage."""
        # Good coverage
        hypothesis1 = CognitiveHypothesis(
            predicted_response_patterns={
                "scenario1": {"r1": 0.5, "r2": 0.5},
                "scenario2": {"r1": 0.3, "r2": 0.7},
                "scenario3": {"r1": 0.8, "r2": 0.2},
            }
        )
        
        result1 = validator._check_prediction_coverage(hypothesis1)
        assert result1["has_sufficient_coverage"]
        assert result1["scenario_types_covered"] == 3
        assert result1["total_predictions"] == 6
        
        # Poor coverage
        hypothesis2 = CognitiveHypothesis(
            predicted_response_patterns={
                "scenario1": {"r1": 0.5}
            }
        )
        
        result2 = validator._check_prediction_coverage(hypothesis2)
        assert not result2["has_sufficient_coverage"]
    
    def test_discriminative_power(self, validator):
        """Test checking discriminative power between hypotheses."""
        # Very similar hypotheses
        h1 = CognitiveHypothesis(
            name="H1",
            predicted_response_patterns={
                "scenario": {"r1": 0.8, "r2": 0.2}
            }
        )
        h2 = CognitiveHypothesis(
            name="H2",
            predicted_response_patterns={
                "scenario": {"r1": 0.75, "r2": 0.25}  # Very similar
            }
        )
        
        # Different hypotheses
        h3 = CognitiveHypothesis(
            name="H3",
            predicted_response_patterns={
                "scenario": {"r1": 0.2, "r2": 0.8}  # Opposite
            }
        )
        
        result = validator._check_discriminative_power([h1, h2, h3])
        assert len(result["similar_pairs"]) > 0  # H1 and H2 are similar
        assert any("H1" in pair[0] and "H2" in pair[1] for pair in result["similar_pairs"])


class TestHypothesisGenerators:
    """Test hypothesis generator classes."""
    
    def test_reasoning_style_hypotheses(self):
        """Test reasoning style hypothesis generation."""
        generator = ReasoningStyleHypotheses()
        hypotheses = generator.generate_hypotheses()
        
        assert len(hypotheses) >= 10  # Should have at least 10 reasoning styles
        assert all(h.category == HypothesisCategory.REASONING_STYLE for h in hypotheses)
        
        # Check for key reasoning styles
        names = [h.name for h in hypotheses]
        assert any("Utilitarian" in name for name in names)
        assert any("Deontological" in name for name in names)
        assert any("Virtue Ethics" in name for name in names)
        assert any("Cautious" in name for name in names)
    
    def test_risk_decision_hypotheses(self):
        """Test risk and decision-making hypothesis generation."""
        generator = RiskDecisionHypotheses()
        hypotheses = generator.generate_hypotheses()
        
        assert len(hypotheses) >= 10
        assert all(h.category == HypothesisCategory.RISK_DECISION for h in hypotheses)
        
        # Check for key risk profiles
        names = [h.name for h in hypotheses]
        assert any("Risk-Averse" in name for name in names)
        assert any("Risk-Seeking" in name for name in names)
        assert any("Expected Value" in name for name in names)
    
    def test_social_cultural_hypotheses(self):
        """Test social and cultural hypothesis generation."""
        generator = SocialCulturalHypotheses()
        hypotheses = generator.generate_hypotheses()
        
        assert len(hypotheses) >= 10
        assert all(h.category == HypothesisCategory.SOCIAL_CULTURAL for h in hypotheses)
        
        # Check for key social profiles
        names = [h.name for h in hypotheses]
        assert any("Empathetic" in name for name in names)
        assert any("Cultural Relativist" in name for name in names)
        assert any("Theory of Mind" in name for name in names)
    
    def test_bias_limitation_hypotheses(self):
        """Test bias and limitation hypothesis generation."""
        generator = BiasLimitationHypotheses()
        hypotheses = generator.generate_hypotheses()
        
        assert len(hypotheses) >= 10
        assert all(h.category == HypothesisCategory.BIAS_LIMITATION for h in hypotheses)
        
        # Check for key biases
        names = [h.name for h in hypotheses]
        assert any("Optimism Bias" in name for name in names)
        assert any("Confirmation Bias" in name for name in names)
        assert any("Anchoring" in name for name in names)
    
    def test_domain_specific_hypotheses(self):
        """Test domain-specific hypothesis generation."""
        generator = DomainSpecificHypotheses()
        hypotheses = generator.generate_hypotheses()
        
        assert len(hypotheses) >= 10
        assert all(h.category == HypothesisCategory.DOMAIN_SPECIFIC for h in hypotheses)
        
        # Check for key domain styles
        names = [h.name for h in hypotheses]
        assert any("Science-Oriented" in name for name in names)
        assert any("Mathematical" in name for name in names)
        assert any("Narrative" in name for name in names)


class TestHypothesisManager:
    """Test hypothesis management system."""
    
    @pytest.fixture
    def manager(self):
        return HypothesisManager()
    
    def test_initialization(self, manager):
        """Test manager initialization."""
        assert not manager._initialized
        manager.initialize()
        assert manager._initialized
        assert len(manager.all_hypotheses) > 50  # Should have 50+ hypotheses
        assert len(manager.hypothesis_index) > 0
    
    def test_get_hypothesis(self, manager):
        """Test retrieving specific hypothesis."""
        manager.initialize()
        
        # Get first hypothesis
        first_hypothesis = manager.all_hypotheses[0]
        retrieved = manager.get_hypothesis(first_hypothesis.hypothesis_id)
        
        assert retrieved is not None
        assert retrieved.hypothesis_id == first_hypothesis.hypothesis_id
        assert retrieved.name == first_hypothesis.name
    
    def test_get_hypotheses_by_category(self, manager):
        """Test filtering hypotheses by category."""
        manager.initialize()
        
        reasoning_hypotheses = manager.get_hypotheses_by_category(HypothesisCategory.REASONING_STYLE)
        assert len(reasoning_hypotheses) >= 10
        assert all(h.category == HypothesisCategory.REASONING_STYLE for h in reasoning_hypotheses)
        
        risk_hypotheses = manager.get_hypotheses_by_category(HypothesisCategory.RISK_DECISION)
        assert len(risk_hypotheses) >= 10
        assert all(h.category == HypothesisCategory.RISK_DECISION for h in risk_hypotheses)
    
    def test_get_hypotheses_by_domain(self, manager):
        """Test filtering hypotheses by cognitive domain."""
        manager.initialize()
        
        ethical_hypotheses = manager.get_hypotheses_by_domain(CognitiveDomain.ETHICAL_REASONING)
        assert len(ethical_hypotheses) > 0
        assert all(h.is_applicable_to_domain(CognitiveDomain.ETHICAL_REASONING) for h in ethical_hypotheses)
    
    def test_get_hypotheses_by_tags(self, manager):
        """Test filtering hypotheses by tags."""
        manager.initialize()
        
        utilitarian_hypotheses = manager.get_hypotheses_by_tags(["utilitarian"])
        assert len(utilitarian_hypotheses) > 0
        assert all("utilitarian" in h.tags for h in utilitarian_hypotheses)
    
    def test_create_hypothesis_set(self, manager):
        """Test creating custom hypothesis sets."""
        manager.initialize()
        
        # Create set with category filter
        ethical_set = manager.create_hypothesis_set(
            name="Ethical Reasoning Set",
            description="Hypotheses for ethical reasoning",
            category_filter=HypothesisCategory.REASONING_STYLE
        )
        
        assert ethical_set.name == "Ethical Reasoning Set"
        assert len(ethical_set.hypotheses) > 0
        assert all(h.category == HypothesisCategory.REASONING_STYLE for h in ethical_set.hypotheses)
    
    def test_find_discriminating_scenarios(self, manager):
        """Test finding scenarios that discriminate between hypotheses."""
        manager.initialize()
        
        # Find two hypotheses likely to have different predictions
        utilitarian = None
        deontological = None
        
        for h in manager.all_hypotheses:
            if "Utilitarian" in h.name:
                utilitarian = h
            elif "Deontological" in h.name:
                deontological = h
        
        if utilitarian and deontological:
            discriminating = manager.find_discriminating_scenarios(
                utilitarian.hypothesis_id,
                deontological.hypothesis_id
            )
            
            # Should find some discriminating scenarios
            assert len(discriminating) > 0
            
            # Check format
            for scenario_type, patterns1, patterns2 in discriminating:
                assert isinstance(scenario_type, str)
                assert isinstance(patterns1, dict)
                assert isinstance(patterns2, dict)
    
    def test_statistics(self, manager):
        """Test hypothesis statistics generation."""
        manager.initialize()
        
        stats = manager.get_statistics()
        
        assert "total_hypotheses" in stats
        assert stats["total_hypotheses"] >= 50
        
        assert "category_distribution" in stats
        assert len(stats["category_distribution"]) == 5  # 5 categories
        
        assert "domain_coverage" in stats
        assert len(stats["domain_coverage"]) == len(CognitiveDomain)
        
        assert "top_tags" in stats
        assert len(stats["top_tags"]) > 0


class TestHypothesisCount:
    """Test that we have 50+ hypotheses as required."""
    
    def test_total_hypothesis_count(self):
        """Verify we generate 50+ cognitive hypotheses."""
        manager = HypothesisManager()
        manager.initialize()
        
        # Count total hypotheses
        total = len(manager.all_hypotheses)
        assert total >= 50, f"Expected 50+ hypotheses, got {total}"
        
        # Count by category
        category_counts = {}
        for hypothesis in manager.all_hypotheses:
            category = hypothesis.category.value
            category_counts[category] = category_counts.get(category, 0) + 1
        
        print(f"\nTotal hypotheses: {total}")
        print("By category:")
        for category, count in category_counts.items():
            print(f"  {category}: {count}")
        
        # Verify each category has reasonable coverage
        assert all(count >= 10 for count in category_counts.values())


class TestHypothesisQuality:
    """Test quality aspects of generated hypotheses."""
    
    def test_hypothesis_completeness(self):
        """Test that all hypotheses have required fields."""
        manager = HypothesisManager()
        manager.initialize()
        
        for hypothesis in manager.all_hypotheses:
            # Required fields
            assert hypothesis.hypothesis_id
            assert hypothesis.name
            assert hypothesis.description
            assert hypothesis.category
            
            # Should have predictions
            assert len(hypothesis.predicted_response_patterns) > 0
            
            # Should have cognitive attributes
            assert len(hypothesis.cognitive_attributes) > 0
            
            # Should have reasonable prior
            assert 0 < hypothesis.prior_probability <= 1
            
            # Should have tags
            assert len(hypothesis.tags) > 0
    
    def test_hypothesis_uniqueness(self):
        """Test that hypotheses are unique."""
        manager = HypothesisManager()
        manager.initialize()
        
        # Check uniqueness of IDs
        ids = [h.hypothesis_id for h in manager.all_hypotheses]
        assert len(ids) == len(set(ids))
        
        # Check uniqueness of names
        names = [h.name for h in manager.all_hypotheses]
        assert len(names) == len(set(names))
    
    def test_cross_references_resolved(self):
        """Test that hypothesis cross-references are properly resolved."""
        manager = HypothesisManager()
        manager.initialize()
        
        for hypothesis in manager.all_hypotheses:
            # Check contradictions are valid IDs
            for cont_id in hypothesis.contradicts:
                assert manager.get_hypothesis(cont_id) is not None
            
            # Check compatibilities are valid IDs
            for comp_id in hypothesis.compatible_with:
                assert manager.get_hypothesis(comp_id) is not None