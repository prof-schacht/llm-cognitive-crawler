"""Domain-specific cognitive hypotheses."""

from typing import List
from .base import HypothesisGenerator, CognitiveHypothesis, HypothesisCategory
from ..core.data_models import CognitiveDomain


class DomainSpecificHypotheses(HypothesisGenerator):
    """Generator for domain-specific cognitive hypotheses."""
    
    def __init__(self):
        super().__init__(HypothesisCategory.DOMAIN_SPECIFIC)
    
    def generate_hypotheses(self) -> List[CognitiveHypothesis]:
        """Generate all domain-specific hypotheses."""
        self.hypotheses = []
        
        # 1. Science-Oriented Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Science-Oriented Reasoner",
            description="Prioritizes empirical evidence, systematic testing, and scientific method",
            predicted_response_patterns={
                "evidence_request": {
                    "demand_evidence": 0.95,
                    "accept_assertion": 0.05
                },
                "hypothesis_testing": {
                    "propose_experiment": 0.9,
                    "accept_untested": 0.1
                },
                "claim_evaluation": {
                    "skeptical_analysis": 0.88,
                    "credulous_acceptance": 0.12
                },
                "methodology": {
                    "systematic_approach": 0.92,
                    "informal_approach": 0.08
                }
            },
            cognitive_attributes={
                "empiricism": 0.95,
                "systematic_thinking": 0.9,
                "skepticism": 0.85,
                "evidence_based": 0.95,
                "methodological_rigor": 0.88
            },
            domain_specificity=[CognitiveDomain.CAUSAL_REASONING],
            confidence_intervals={
                "empiricism": (0.9, 0.98),
                "evidence_based": (0.9, 0.98)
            },
            prior_probability=0.12,
            tags=["scientific", "empirical", "evidence-based", "skeptical"],
            contradicts=["faith_based_reasoner_id", "intuitive_reasoner_id"],
            compatible_with=["analytical_reasoner_id", "probabilistic_thinker_id"]
        ))
        
        # 2. Intuitive Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Intuitive Domain Reasoner",
            description="Relies on gut feelings, pattern recognition, and holistic understanding",
            predicted_response_patterns={
                "decision_style": {
                    "intuitive_choice": 0.85,
                    "analytical_process": 0.15
                },
                "problem_approach": {
                    "holistic_grasp": 0.88,
                    "step_by_step": 0.12
                },
                "pattern_recognition": {
                    "implicit_pattern": 0.9,
                    "explicit_rules": 0.1
                },
                "explanation_style": {
                    "feels_right": 0.8,
                    "logical_proof": 0.2
                }
            },
            cognitive_attributes={
                "intuition": 0.9,
                "holistic_processing": 0.88,
                "pattern_sensitivity": 0.85,
                "implicit_knowledge": 0.85,
                "gestalt_thinking": 0.82
            },
            domain_specificity=[],
            confidence_intervals={
                "intuition": (0.85, 0.95),
                "holistic_processing": (0.83, 0.93)
            },
            prior_probability=0.15,
            tags=["intuitive", "holistic", "pattern-based", "implicit"],
            contradicts=["analytical_systematic_reasoner_id", "science_oriented_reasoner_id"],
            compatible_with=["creative_thinker_id"]
        ))
        
        # 3. Mathematical/Formal Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Mathematical Formal Reasoner",
            description="Thinks in formal systems, mathematical structures, and logical proofs",
            predicted_response_patterns={
                "problem_formulation": {
                    "formal_notation": 0.9,
                    "informal_description": 0.1
                },
                "proof_preference": {
                    "rigorous_proof": 0.95,
                    "intuitive_argument": 0.05
                },
                "quantification": {
                    "precise_numbers": 0.88,
                    "qualitative_terms": 0.12
                },
                "abstraction_level": {
                    "high_abstraction": 0.85,
                    "concrete_examples": 0.15
                }
            },
            cognitive_attributes={
                "mathematical_thinking": 0.95,
                "formal_reasoning": 0.92,
                "abstraction_ability": 0.9,
                "precision": 0.95,
                "logical_rigor": 0.92
            },
            domain_specificity=[CognitiveDomain.LOGICAL_REASONING],
            confidence_intervals={
                "mathematical_thinking": (0.9, 0.98),
                "precision": (0.9, 0.98)
            },
            prior_probability=0.08,
            tags=["mathematical", "formal", "rigorous", "abstract"],
            contradicts=["concrete_thinker_id", "approximate_reasoner_id"],
            compatible_with=["analytical_reasoner_id", "systematic_thinker_id"]
        ))
        
        # 4. Narrative/Story-Based Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Narrative Story Reasoner",
            description="Understands and communicates through stories, examples, and narratives",
            predicted_response_patterns={
                "explanation_method": {
                    "story_example": 0.9,
                    "abstract_principle": 0.1
                },
                "memory_style": {
                    "narrative_memory": 0.88,
                    "factual_list": 0.12
                },
                "persuasion_approach": {
                    "anecdotal_evidence": 0.85,
                    "statistical_data": 0.15
                },
                "understanding_mode": {
                    "through_stories": 0.9,
                    "through_rules": 0.1
                }
            },
            cognitive_attributes={
                "narrative_thinking": 0.92,
                "story_construction": 0.88,
                "contextual_memory": 0.85,
                "experiential_focus": 0.85,
                "concrete_thinking": 0.8
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "narrative_thinking": (0.87, 0.97),
                "story_construction": (0.83, 0.93)
            },
            prior_probability=0.2,
            tags=["narrative", "story-based", "contextual", "experiential"],
            contradicts=["abstract_thinker_id", "mathematical_reasoner_id"],
            compatible_with=["empathetic_reasoner_id", "social_reasoner_id"]
        ))
        
        # 5. Systems Thinker
        self.add_hypothesis(CognitiveHypothesis(
            name="Systems Thinker",
            description="Sees interconnections, feedback loops, and emergent properties",
            predicted_response_patterns={
                "problem_analysis": {
                    "systemic_view": 0.9,
                    "isolated_factors": 0.1
                },
                "causation_model": {
                    "circular_causation": 0.85,
                    "linear_causation": 0.15
                },
                "solution_approach": {
                    "holistic_intervention": 0.88,
                    "targeted_fix": 0.12
                },
                "complexity_handling": {
                    "embrace_complexity": 0.85,
                    "simplify_away": 0.15
                }
            },
            cognitive_attributes={
                "systems_thinking": 0.95,
                "complexity_appreciation": 0.9,
                "feedback_awareness": 0.88,
                "emergence_recognition": 0.85,
                "interconnection_focus": 0.92
            },
            domain_specificity=[CognitiveDomain.CAUSAL_REASONING],
            confidence_intervals={
                "systems_thinking": (0.9, 0.98),
                "complexity_appreciation": (0.85, 0.95)
            },
            prior_probability=0.1,
            tags=["systems", "holistic", "complexity", "emergence"],
            contradicts=["reductionist_id", "linear_thinker_id"],
            compatible_with=["ecological_thinker_id", "network_theorist_id"]
        ))
        
        # 6. Historical/Precedent-Based Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Historical Precedent Reasoner",
            description="Draws heavily on historical examples and past precedents",
            predicted_response_patterns={
                "decision_basis": {
                    "historical_precedent": 0.9,
                    "novel_approach": 0.1
                },
                "prediction_method": {
                    "past_patterns": 0.88,
                    "theoretical_model": 0.12
                },
                "argument_style": {
                    "cite_history": 0.85,
                    "abstract_principle": 0.15
                },
                "learning_approach": {
                    "case_studies": 0.9,
                    "general_rules": 0.1
                }
            },
            cognitive_attributes={
                "historical_awareness": 0.92,
                "precedent_focus": 0.88,
                "pattern_from_past": 0.85,
                "case_based_reasoning": 0.9,
                "tradition_respect": 0.8
            },
            domain_specificity=[],
            confidence_intervals={
                "historical_awareness": (0.87, 0.97),
                "case_based_reasoning": (0.85, 0.95)
            },
            prior_probability=0.12,
            tags=["historical", "precedent-based", "case-study", "traditional"],
            contradicts=["future_oriented_id", "innovative_thinker_id"],
            compatible_with=["conservative_thinker_id", "empirical_reasoner_id"]
        ))
        
        # 7. Creative/Divergent Thinker
        self.add_hypothesis(CognitiveHypothesis(
            name="Creative Divergent Thinker",
            description="Generates novel ideas, thinks outside conventional boundaries",
            predicted_response_patterns={
                "solution_generation": {
                    "novel_solutions": 0.9,
                    "conventional_solutions": 0.1
                },
                "problem_reframing": {
                    "redefine_problem": 0.85,
                    "accept_framing": 0.15
                },
                "idea_quantity": {
                    "many_alternatives": 0.88,
                    "few_options": 0.12
                },
                "constraint_response": {
                    "transcend_limits": 0.82,
                    "work_within": 0.18
                }
            },
            cognitive_attributes={
                "creativity": 0.92,
                "divergent_thinking": 0.9,
                "originality": 0.88,
                "flexibility": 0.85,
                "boundary_breaking": 0.85
            },
            domain_specificity=[],
            confidence_intervals={
                "creativity": (0.87, 0.97),
                "divergent_thinking": (0.85, 0.95)
            },
            prior_probability=0.1,
            tags=["creative", "divergent", "innovative", "original"],
            contradicts=["conventional_thinker_id", "rule_follower_id"],
            compatible_with=["intuitive_reasoner_id", "systems_thinker_id"]
        ))
        
        # 8. Philosophical/Abstract Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Philosophical Abstract Reasoner",
            description="Engages with abstract concepts, fundamental questions, and philosophical frameworks",
            predicted_response_patterns={
                "question_type": {
                    "fundamental_questions": 0.9,
                    "practical_questions": 0.1
                },
                "conceptual_level": {
                    "high_abstraction": 0.88,
                    "concrete_specifics": 0.12
                },
                "argument_depth": {
                    "deep_principles": 0.85,
                    "surface_features": 0.15
                },
                "thought_experiments": {
                    "use_hypotheticals": 0.9,
                    "stick_to_reality": 0.1
                }
            },
            cognitive_attributes={
                "abstract_thinking": 0.92,
                "philosophical_depth": 0.9,
                "conceptual_analysis": 0.88,
                "fundamental_questioning": 0.85,
                "theoretical_orientation": 0.88
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "abstract_thinking": (0.87, 0.97),
                "philosophical_depth": (0.85, 0.95)
            },
            prior_probability=0.08,
            tags=["philosophical", "abstract", "theoretical", "conceptual"],
            contradicts=["practical_reasoner_id", "concrete_thinker_id"],
            compatible_with=["dialectical_reasoner_id", "principled_reasoner_id"]
        ))
        
        # 9. Ecological/Environmental Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Ecological Environmental Reasoner",
            description="Thinks in terms of ecosystems, sustainability, and environmental impact",
            predicted_response_patterns={
                "impact_assessment": {
                    "consider_environment": 0.95,
                    "ignore_environment": 0.05
                },
                "time_horizon": {
                    "long_term_impact": 0.9,
                    "short_term_only": 0.1
                },
                "value_system": {
                    "sustainability_focus": 0.88,
                    "growth_focus": 0.12
                },
                "system_boundaries": {
                    "broad_ecosystem": 0.85,
                    "narrow_focus": 0.15
                }
            },
            cognitive_attributes={
                "ecological_thinking": 0.92,
                "sustainability_focus": 0.9,
                "long_term_orientation": 0.88,
                "interconnection_awareness": 0.85,
                "environmental_ethics": 0.88
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING, CognitiveDomain.CAUSAL_REASONING],
            confidence_intervals={
                "ecological_thinking": (0.87, 0.97),
                "sustainability_focus": (0.85, 0.95)
            },
            prior_probability=0.1,
            tags=["ecological", "environmental", "sustainable", "systems"],
            contradicts=["short_term_maximizer_id"],
            compatible_with=["systems_thinker_id", "future_oriented_id"]
        ))
        
        # 10. Legal/Procedural Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Legal Procedural Reasoner",
            description="Thinks in terms of rules, procedures, precedents, and legal frameworks",
            predicted_response_patterns={
                "conflict_resolution": {
                    "procedural_approach": 0.9,
                    "informal_resolution": 0.1
                },
                "rule_application": {
                    "strict_interpretation": 0.88,
                    "flexible_interpretation": 0.12
                },
                "evidence_standard": {
                    "formal_requirements": 0.85,
                    "informal_judgment": 0.15
                },
                "fairness_conception": {
                    "procedural_fairness": 0.9,
                    "outcome_fairness": 0.1
                }
            },
            cognitive_attributes={
                "rule_orientation": 0.92,
                "procedural_thinking": 0.9,
                "precedent_awareness": 0.88,
                "formal_reasoning": 0.85,
                "systematic_application": 0.88
            },
            domain_specificity=[CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "rule_orientation": (0.87, 0.97),
                "procedural_thinking": (0.85, 0.95)
            },
            prior_probability=0.08,
            tags=["legal", "procedural", "rule-based", "formal"],
            contradicts=["flexible_reasoner_id", "context_dependent_id"],
            compatible_with=["deontological_reasoner_id", "systematic_thinker_id"]
        ))
        
        # 11. Engineering/Design Thinker
        self.add_hypothesis(CognitiveHypothesis(
            name="Engineering Design Thinker",
            description="Focuses on practical solutions, optimization, and functional design",
            predicted_response_patterns={
                "problem_approach": {
                    "design_solution": 0.9,
                    "analyze_only": 0.1
                },
                "optimization_focus": {
                    "seek_optimal": 0.88,
                    "accept_suboptimal": 0.12
                },
                "constraint_handling": {
                    "work_with_constraints": 0.9,
                    "ignore_constraints": 0.1
                },
                "solution_criteria": {
                    "functional_metrics": 0.85,
                    "aesthetic_only": 0.15
                }
            },
            cognitive_attributes={
                "design_thinking": 0.92,
                "optimization_mindset": 0.88,
                "practical_orientation": 0.9,
                "constraint_awareness": 0.88,
                "solution_focused": 0.9
            },
            domain_specificity=[CognitiveDomain.CAUSAL_REASONING],
            confidence_intervals={
                "design_thinking": (0.87, 0.97),
                "practical_orientation": (0.85, 0.95)
            },
            prior_probability=0.12,
            tags=["engineering", "design", "optimization", "practical"],
            contradicts=["theoretical_only_id"],
            compatible_with=["systems_thinker_id", "pragmatic_reasoner_id"]
        ))
        
        # 12. Pedagogical/Teaching Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Pedagogical Teaching Reasoner",
            description="Thinks about how to effectively communicate and teach concepts",
            predicted_response_patterns={
                "explanation_style": {
                    "scaffolded_learning": 0.9,
                    "dump_information": 0.1
                },
                "concept_introduction": {
                    "gradual_complexity": 0.88,
                    "full_complexity": 0.12
                },
                "understanding_check": {
                    "verify_comprehension": 0.85,
                    "assume_understanding": 0.15
                },
                "example_use": {
                    "multiple_examples": 0.9,
                    "abstract_only": 0.1
                }
            },
            cognitive_attributes={
                "pedagogical_awareness": 0.92,
                "communication_focus": 0.9,
                "learner_modeling": 0.85,
                "scaffolding_ability": 0.88,
                "clarity_emphasis": 0.9
            },
            domain_specificity=[],
            confidence_intervals={
                "pedagogical_awareness": (0.87, 0.97),
                "communication_focus": (0.85, 0.95)
            },
            prior_probability=0.15,
            tags=["pedagogical", "teaching", "educational", "communicative"],
            contradicts=["expert_assumption_id"],
            compatible_with=["empathetic_reasoner_id", "systematic_thinker_id"]
        ))
        
        return self.hypotheses