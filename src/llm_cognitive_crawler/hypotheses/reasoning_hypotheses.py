"""Reasoning style cognitive hypotheses."""

from typing import List
from .base import HypothesisGenerator, CognitiveHypothesis, HypothesisCategory
from ..core.data_models import CognitiveDomain


class ReasoningStyleHypotheses(HypothesisGenerator):
    """Generator for reasoning style hypotheses."""
    
    def __init__(self):
        super().__init__(HypothesisCategory.REASONING_STYLE)
    
    def generate_hypotheses(self) -> List[CognitiveHypothesis]:
        """Generate all reasoning style hypotheses."""
        self.hypotheses = []
        
        # 1. Utilitarian Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Utilitarian Reasoner",
            description="Maximizes overall outcomes and happiness, focuses on greatest good for greatest number",
            predicted_response_patterns={
                "trolley_problem": {
                    "pull_lever": 0.8,
                    "do_nothing": 0.2
                },
                "resource_allocation": {
                    "maximize_lives_saved": 0.9,
                    "equal_distribution": 0.1
                },
                "lying_dilemma": {
                    "lie_to_save_lives": 0.7,
                    "always_truth": 0.3
                },
                "sacrifice_dilemma": {
                    "sacrifice_one_save_many": 0.85,
                    "never_sacrifice": 0.15
                }
            },
            cognitive_attributes={
                "outcome_focused": 0.9,
                "rule_based": 0.2,
                "quantitative_reasoning": 0.8,
                "emotional_detachment": 0.7,
                "consequentialist": 0.95
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "outcome_focused": (0.85, 0.95),
                "rule_based": (0.1, 0.3)
            },
            prior_probability=0.15,
            tags=["utilitarian", "consequentialist", "outcome-based", "quantitative"],
            contradicts=["deontological_reasoner_id"],
            compatible_with=["expected_value_maximizer_id"]
        ))
        
        # 2. Deontological Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Deontological Reasoner",
            description="Follows rules and duties regardless of consequences, emphasizes moral absolutes",
            predicted_response_patterns={
                "trolley_problem": {
                    "pull_lever": 0.2,
                    "do_nothing": 0.8
                },
                "lying_dilemma": {
                    "lie_to_save_lives": 0.1,
                    "always_truth": 0.9
                },
                "promise_breaking": {
                    "keep_promise": 0.95,
                    "break_for_benefit": 0.05
                },
                "property_rights": {
                    "respect_property": 0.9,
                    "violate_for_need": 0.1
                }
            },
            cognitive_attributes={
                "rule_based": 0.95,
                "outcome_focused": 0.2,
                "principled": 0.9,
                "consistency": 0.85,
                "moral_absolutism": 0.8
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "rule_based": (0.9, 0.98),
                "outcome_focused": (0.1, 0.3)
            },
            prior_probability=0.12,
            tags=["deontological", "rule-based", "duty", "categorical"],
            contradicts=["utilitarian_reasoner_id"],
            compatible_with=["virtue_ethics_reasoner_id"]
        ))
        
        # 3. Virtue Ethics Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Virtue Ethics Reasoner",
            description="Focuses on character traits and moral virtues rather than rules or outcomes",
            predicted_response_patterns={
                "honesty_dilemma": {
                    "honest_response": 0.85,
                    "deceptive_response": 0.15
                },
                "compassion_scenario": {
                    "compassionate_choice": 0.9,
                    "indifferent_choice": 0.1
                },
                "courage_test": {
                    "courageous_action": 0.8,
                    "cowardly_action": 0.2
                },
                "wisdom_application": {
                    "wise_counsel": 0.85,
                    "rash_advice": 0.15
                }
            },
            cognitive_attributes={
                "character_focused": 0.9,
                "context_sensitive": 0.8,
                "wisdom_oriented": 0.85,
                "emotional_integration": 0.8,
                "holistic_thinking": 0.85
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING, CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "character_focused": (0.85, 0.95),
                "context_sensitive": (0.7, 0.85)
            },
            prior_probability=0.1,
            tags=["virtue_ethics", "character", "aristotelian", "wisdom"],
            contradicts=["purely_analytical_id"],
            compatible_with=["deontological_reasoner_id", "empathetic_reasoner_id"]
        ))
        
        # 4. Cautious/Uncertain Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Cautious Uncertain Reasoner",
            description="Expresses uncertainty, seeks more information, avoids hasty conclusions",
            predicted_response_patterns={
                "complex_dilemma": {
                    "need_more_info": 0.7,
                    "decisive_answer": 0.3
                },
                "ambiguous_scenario": {
                    "express_uncertainty": 0.8,
                    "confident_judgment": 0.2
                },
                "risk_assessment": {
                    "seek_clarification": 0.75,
                    "immediate_decision": 0.25
                },
                "moral_judgment": {
                    "qualified_response": 0.85,
                    "absolute_judgment": 0.15
                }
            },
            cognitive_attributes={
                "confidence": 0.3,
                "information_seeking": 0.9,
                "epistemic_humility": 0.85,
                "analytical_thoroughness": 0.8,
                "decision_delay": 0.7
            },
            domain_specificity=[],  # Applies across all domains
            confidence_intervals={
                "confidence": (0.2, 0.4),
                "information_seeking": (0.85, 0.95)
            },
            prior_probability=0.15,
            tags=["cautious", "uncertain", "information-seeking", "humble"],
            contradicts=["overconfident_reasoner_id"],
            compatible_with=["analytical_reasoner_id", "scientific_reasoner_id"]
        ))
        
        # 5. Pragmatic Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Pragmatic Reasoner",
            description="Focuses on practical solutions and real-world applicability",
            predicted_response_patterns={
                "theoretical_vs_practical": {
                    "practical_solution": 0.9,
                    "theoretical_ideal": 0.1
                },
                "resource_constraint": {
                    "work_within_limits": 0.85,
                    "demand_ideal": 0.15
                },
                "implementation_focus": {
                    "consider_feasibility": 0.9,
                    "ignore_constraints": 0.1
                },
                "compromise_scenario": {
                    "find_middle_ground": 0.8,
                    "stick_to_principle": 0.2
                }
            },
            cognitive_attributes={
                "practicality": 0.95,
                "flexibility": 0.8,
                "result_oriented": 0.85,
                "context_awareness": 0.9,
                "compromise_willing": 0.75
            },
            domain_specificity=[],
            confidence_intervals={
                "practicality": (0.9, 0.98),
                "flexibility": (0.7, 0.85)
            },
            prior_probability=0.18,
            tags=["pragmatic", "practical", "flexible", "results-focused"],
            contradicts=["idealist_reasoner_id"],
            compatible_with=["utilitarian_reasoner_id"]
        ))
        
        # 6. Analytical Systematic Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Analytical Systematic Reasoner",
            description="Breaks down problems systematically, uses logical frameworks",
            predicted_response_patterns={
                "complex_problem": {
                    "systematic_breakdown": 0.95,
                    "intuitive_leap": 0.05
                },
                "data_analysis": {
                    "methodical_approach": 0.9,
                    "quick_judgment": 0.1
                },
                "decision_tree": {
                    "structured_analysis": 0.95,
                    "gut_feeling": 0.05
                },
                "pattern_recognition": {
                    "explicit_reasoning": 0.85,
                    "implicit_recognition": 0.15
                }
            },
            cognitive_attributes={
                "analytical": 0.95,
                "systematic": 0.9,
                "logical_consistency": 0.9,
                "detail_oriented": 0.85,
                "methodical": 0.9
            },
            domain_specificity=[CognitiveDomain.LOGICAL_REASONING, CognitiveDomain.CAUSAL_REASONING],
            confidence_intervals={
                "analytical": (0.9, 0.98),
                "systematic": (0.85, 0.95)
            },
            prior_probability=0.2,
            tags=["analytical", "systematic", "logical", "methodical"],
            contradicts=["intuitive_reasoner_id"],
            compatible_with=["scientific_reasoner_id", "cautious_reasoner_id"]
        ))
        
        # 7. Intuitive Pattern Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Intuitive Pattern Reasoner",
            description="Relies on pattern recognition and intuitive leaps rather than explicit logic",
            predicted_response_patterns={
                "pattern_completion": {
                    "intuitive_answer": 0.85,
                    "analytical_derivation": 0.15
                },
                "creative_problem": {
                    "innovative_solution": 0.8,
                    "conventional_approach": 0.2
                },
                "quick_decision": {
                    "gut_instinct": 0.9,
                    "deliberative_choice": 0.1
                },
                "gestalt_perception": {
                    "holistic_view": 0.85,
                    "component_analysis": 0.15
                }
            },
            cognitive_attributes={
                "intuitive": 0.9,
                "pattern_sensitive": 0.85,
                "creative": 0.8,
                "fast_thinking": 0.85,
                "holistic": 0.8
            },
            domain_specificity=[],
            confidence_intervals={
                "intuitive": (0.85, 0.95),
                "pattern_sensitive": (0.8, 0.9)
            },
            prior_probability=0.12,
            tags=["intuitive", "pattern-based", "creative", "holistic"],
            contradicts=["analytical_systematic_reasoner_id"],
            compatible_with=["creative_reasoner_id"]
        ))
        
        # 8. Dialectical Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Dialectical Reasoner",
            description="Considers opposing viewpoints, seeks synthesis of contradictions",
            predicted_response_patterns={
                "controversial_topic": {
                    "acknowledge_both_sides": 0.9,
                    "one_sided_view": 0.1
                },
                "thesis_antithesis": {
                    "seek_synthesis": 0.85,
                    "choose_one_side": 0.15
                },
                "paradox_resolution": {
                    "integrate_contradiction": 0.8,
                    "reject_one_side": 0.2
                },
                "perspective_taking": {
                    "multiple_viewpoints": 0.9,
                    "single_perspective": 0.1
                }
            },
            cognitive_attributes={
                "dialectical_thinking": 0.9,
                "perspective_integration": 0.85,
                "complexity_tolerance": 0.9,
                "synthesis_oriented": 0.85,
                "nuanced_thinking": 0.9
            },
            domain_specificity=[],
            confidence_intervals={
                "dialectical_thinking": (0.85, 0.95),
                "complexity_tolerance": (0.85, 0.95)
            },
            prior_probability=0.08,
            tags=["dialectical", "integrative", "synthesis", "balanced"],
            contradicts=["binary_thinker_id"],
            compatible_with=["cautious_reasoner_id", "contextual_reasoner_id"]
        ))
        
        # 9. Principled Idealist Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Principled Idealist Reasoner",
            description="Adheres to ideals and principles even when impractical",
            predicted_response_patterns={
                "ideal_vs_real": {
                    "pursue_ideal": 0.85,
                    "accept_compromise": 0.15
                },
                "principle_test": {
                    "maintain_principle": 0.9,
                    "pragmatic_exception": 0.1
                },
                "vision_pursuit": {
                    "idealistic_goal": 0.88,
                    "realistic_target": 0.12
                },
                "moral_purity": {
                    "pure_stance": 0.85,
                    "practical_adjustment": 0.15
                }
            },
            cognitive_attributes={
                "idealistic": 0.9,
                "principled": 0.95,
                "vision_driven": 0.85,
                "uncompromising": 0.8,
                "aspirational": 0.9
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "idealistic": (0.85, 0.95),
                "principled": (0.9, 0.98)
            },
            prior_probability=0.06,
            tags=["idealist", "principled", "uncompromising", "visionary"],
            contradicts=["pragmatic_reasoner_id"],
            compatible_with=["deontological_reasoner_id"]
        ))
        
        # 10. Contextual Adaptive Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Contextual Adaptive Reasoner",
            description="Adapts reasoning style to context and situation",
            predicted_response_patterns={
                "context_change": {
                    "adapt_approach": 0.9,
                    "maintain_consistency": 0.1
                },
                "cultural_scenario": {
                    "culturally_sensitive": 0.85,
                    "universal_approach": 0.15
                },
                "situational_ethics": {
                    "context_dependent": 0.88,
                    "absolute_rule": 0.12
                },
                "flexible_framework": {
                    "adjust_method": 0.85,
                    "rigid_application": 0.15
                }
            },
            cognitive_attributes={
                "contextual_sensitivity": 0.95,
                "adaptive_flexibility": 0.9,
                "situational_awareness": 0.9,
                "meta_cognitive": 0.85,
                "responsive": 0.88
            },
            domain_specificity=[],
            confidence_intervals={
                "contextual_sensitivity": (0.9, 0.98),
                "adaptive_flexibility": (0.85, 0.95)
            },
            prior_probability=0.14,
            tags=["contextual", "adaptive", "flexible", "situational"],
            contradicts=["rigid_reasoner_id"],
            compatible_with=["dialectical_reasoner_id", "pragmatic_reasoner_id"]
        ))
        
        return self.hypotheses