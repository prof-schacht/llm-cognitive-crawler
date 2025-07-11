"""Social and cultural cognitive hypotheses."""

from typing import List
from .base import HypothesisGenerator, CognitiveHypothesis, HypothesisCategory
from ..core.data_models import CognitiveDomain


class SocialCulturalHypotheses(HypothesisGenerator):
    """Generator for social and cultural cognitive hypotheses."""
    
    def __init__(self):
        super().__init__(HypothesisCategory.SOCIAL_CULTURAL)
    
    def generate_hypotheses(self) -> List[CognitiveHypothesis]:
        """Generate all social and cultural hypotheses."""
        self.hypotheses = []
        
        # 1. Empathetic Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Empathetic Reasoner",
            description="Prioritizes emotional understanding and perspective-taking in social situations",
            predicted_response_patterns={
                "emotional_scenario": {
                    "consider_feelings": 0.95,
                    "ignore_emotions": 0.05
                },
                "perspective_taking": {
                    "multiple_perspectives": 0.9,
                    "single_view": 0.1
                },
                "conflict_resolution": {
                    "empathetic_approach": 0.85,
                    "logical_only": 0.15
                },
                "suffering_response": {
                    "compassionate_action": 0.9,
                    "detached_analysis": 0.1
                }
            },
            cognitive_attributes={
                "empathy": 0.95,
                "emotional_intelligence": 0.9,
                "perspective_taking": 0.9,
                "compassion": 0.85,
                "social_sensitivity": 0.88
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "empathy": (0.9, 0.98),
                "emotional_intelligence": (0.85, 0.95)
            },
            prior_probability=0.2,
            tags=["empathetic", "emotional", "compassionate", "perspective-taking"],
            contradicts=["analytical_social_reasoner_id"],
            compatible_with=["virtue_ethics_reasoner_id"]
        ))
        
        # 2. Analytical Social Reasoner
        self.add_hypothesis(CognitiveHypothesis(
            name="Analytical Social Reasoner",
            description="Approaches social situations with logic and systematic analysis",
            predicted_response_patterns={
                "social_dilemma": {
                    "logical_analysis": 0.85,
                    "emotional_response": 0.15
                },
                "group_dynamics": {
                    "systematic_approach": 0.9,
                    "intuitive_feel": 0.1
                },
                "interpersonal_conflict": {
                    "structured_solution": 0.8,
                    "emotional_mediation": 0.2
                },
                "social_prediction": {
                    "model_based": 0.85,
                    "empathy_based": 0.15
                }
            },
            cognitive_attributes={
                "analytical": 0.9,
                "emotion_neutral": 0.8,
                "systematic": 0.85,
                "objectivity": 0.85,
                "social_modeling": 0.8
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "analytical": (0.85, 0.95),
                "emotion_neutral": (0.75, 0.85)
            },
            prior_probability=0.12,
            tags=["analytical", "systematic", "objective", "social-logic"],
            contradicts=["empathetic_reasoner_id"],
            compatible_with=["analytical_systematic_reasoner_id"]
        ))
        
        # 3. Cultural Relativist
        self.add_hypothesis(CognitiveHypothesis(
            name="Cultural Relativist",
            description="Recognizes and respects cultural differences in values and behaviors",
            predicted_response_patterns={
                "cross_cultural_judgment": {
                    "culturally_relative": 0.85,
                    "universal_standard": 0.15
                },
                "moral_evaluation": {
                    "context_dependent": 0.8,
                    "absolute_judgment": 0.2
                },
                "social_norms": {
                    "respect_differences": 0.9,
                    "impose_own_norms": 0.1
                },
                "value_conflict": {
                    "acknowledge_validity": 0.85,
                    "assert_superiority": 0.15
                }
            },
            cognitive_attributes={
                "cultural_awareness": 0.95,
                "relativistic_thinking": 0.85,
                "tolerance": 0.9,
                "contextual_sensitivity": 0.88,
                "pluralistic": 0.85
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION, CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "cultural_awareness": (0.9, 0.98),
                "relativistic_thinking": (0.8, 0.9)
            },
            prior_probability=0.15,
            tags=["relativist", "multicultural", "tolerant", "contextual"],
            contradicts=["universalist_id"],
            compatible_with=["contextual_reasoner_id"]
        ))
        
        # 4. Collectivist Thinker
        self.add_hypothesis(CognitiveHypothesis(
            name="Collectivist Thinker",
            description="Prioritizes group harmony and collective goals over individual interests",
            predicted_response_patterns={
                "individual_vs_group": {
                    "group_priority": 0.85,
                    "individual_priority": 0.15
                },
                "decision_style": {
                    "consensus_seeking": 0.9,
                    "independent_choice": 0.1
                },
                "conflict_approach": {
                    "harmony_preservation": 0.88,
                    "direct_confrontation": 0.12
                },
                "achievement_attribution": {
                    "group_success": 0.8,
                    "individual_merit": 0.2
                }
            },
            cognitive_attributes={
                "collectivism": 0.9,
                "group_harmony": 0.88,
                "interdependence": 0.85,
                "consensus_orientation": 0.9,
                "social_cohesion": 0.85
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "collectivism": (0.85, 0.95),
                "group_harmony": (0.83, 0.93)
            },
            prior_probability=0.2,
            tags=["collectivist", "group-oriented", "harmony", "interdependent"],
            contradicts=["individualist_thinker_id"],
            compatible_with=["empathetic_reasoner_id"]
        ))
        
        # 5. Individualist Thinker
        self.add_hypothesis(CognitiveHypothesis(
            name="Individualist Thinker",
            description="Emphasizes individual autonomy, rights, and personal achievement",
            predicted_response_patterns={
                "individual_vs_group": {
                    "individual_priority": 0.85,
                    "group_priority": 0.15
                },
                "decision_style": {
                    "independent_choice": 0.9,
                    "consensus_seeking": 0.1
                },
                "responsibility": {
                    "personal_accountability": 0.88,
                    "shared_responsibility": 0.12
                },
                "success_attribution": {
                    "individual_effort": 0.85,
                    "circumstances": 0.15
                }
            },
            cognitive_attributes={
                "individualism": 0.9,
                "autonomy": 0.88,
                "self_reliance": 0.85,
                "personal_freedom": 0.9,
                "independence": 0.88
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "individualism": (0.85, 0.95),
                "autonomy": (0.83, 0.93)
            },
            prior_probability=0.18,
            tags=["individualist", "autonomous", "independent", "self-reliant"],
            contradicts=["collectivist_thinker_id"],
            compatible_with=["analytical_social_reasoner_id"]
        ))
        
        # 6. Theory of Mind Expert
        self.add_hypothesis(CognitiveHypothesis(
            name="Theory of Mind Expert",
            description="Sophisticated understanding of others' mental states, beliefs, and intentions",
            predicted_response_patterns={
                "false_belief_task": {
                    "correct_prediction": 0.95,
                    "incorrect_prediction": 0.05
                },
                "intention_reading": {
                    "accurate_inference": 0.9,
                    "misinterpretation": 0.1
                },
                "nested_beliefs": {
                    "track_complexity": 0.85,
                    "lose_track": 0.15
                },
                "deception_detection": {
                    "detect_deception": 0.8,
                    "miss_deception": 0.2
                }
            },
            cognitive_attributes={
                "theory_of_mind": 0.95,
                "mental_modeling": 0.9,
                "intention_attribution": 0.88,
                "belief_tracking": 0.9,
                "social_cognition": 0.92
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "theory_of_mind": (0.9, 0.98),
                "mental_modeling": (0.85, 0.95)
            },
            prior_probability=0.1,
            tags=["theory-of-mind", "mentalizing", "social-cognitive", "perspective"],
            contradicts=["mind_blind_id"],
            compatible_with=["empathetic_reasoner_id"]
        ))
        
        # 7. Social Conformist
        self.add_hypothesis(CognitiveHypothesis(
            name="Social Conformist",
            description="Tends to align with group norms and social expectations",
            predicted_response_patterns={
                "conformity_pressure": {
                    "conform_to_group": 0.85,
                    "maintain_independence": 0.15
                },
                "social_norms": {
                    "follow_convention": 0.9,
                    "challenge_norms": 0.1
                },
                "peer_influence": {
                    "influenced_by_peers": 0.88,
                    "resist_influence": 0.12
                },
                "authority_response": {
                    "defer_to_authority": 0.8,
                    "question_authority": 0.2
                }
            },
            cognitive_attributes={
                "conformity": 0.88,
                "social_compliance": 0.85,
                "norm_adherence": 0.9,
                "authority_deference": 0.8,
                "group_influence": 0.85
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "conformity": (0.83, 0.93),
                "norm_adherence": (0.85, 0.95)
            },
            prior_probability=0.25,
            tags=["conformist", "compliant", "norm-following", "conventional"],
            contradicts=["nonconformist_id"],
            compatible_with=["collectivist_thinker_id"]
        ))
        
        # 8. Fairness Maximizer
        self.add_hypothesis(CognitiveHypothesis(
            name="Fairness Maximizer",
            description="Prioritizes fairness and equal treatment in social situations",
            predicted_response_patterns={
                "resource_distribution": {
                    "equal_distribution": 0.85,
                    "unequal_distribution": 0.15
                },
                "ultimatum_game": {
                    "fair_offer": 0.9,
                    "unfair_offer": 0.1
                },
                "justice_scenario": {
                    "procedural_fairness": 0.88,
                    "outcome_only": 0.12
                },
                "bias_response": {
                    "correct_for_bias": 0.85,
                    "maintain_bias": 0.15
                }
            },
            cognitive_attributes={
                "fairness_orientation": 0.95,
                "equality_focus": 0.88,
                "justice_sensitivity": 0.9,
                "impartiality": 0.85,
                "reciprocity": 0.8
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION, CognitiveDomain.ETHICAL_REASONING],
            confidence_intervals={
                "fairness_orientation": (0.9, 0.98),
                "justice_sensitivity": (0.85, 0.95)
            },
            prior_probability=0.15,
            tags=["fair", "egalitarian", "just", "impartial"],
            contradicts=["self_interest_maximizer_id"],
            compatible_with=["deontological_reasoner_id"]
        ))
        
        # 9. Social Hierarchist
        self.add_hypothesis(CognitiveHypothesis(
            name="Social Hierarchist",
            description="Accepts and reinforces social hierarchies and power structures",
            predicted_response_patterns={
                "power_dynamics": {
                    "respect_hierarchy": 0.85,
                    "challenge_hierarchy": 0.15
                },
                "status_recognition": {
                    "acknowledge_status": 0.9,
                    "ignore_status": 0.1
                },
                "leadership_style": {
                    "top_down": 0.8,
                    "collaborative": 0.2
                },
                "inequality_response": {
                    "accept_as_natural": 0.75,
                    "seek_to_change": 0.25
                }
            },
            cognitive_attributes={
                "hierarchy_acceptance": 0.88,
                "power_distance": 0.85,
                "status_sensitivity": 0.9,
                "authority_respect": 0.85,
                "order_preference": 0.8
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "hierarchy_acceptance": (0.83, 0.93),
                "status_sensitivity": (0.85, 0.95)
            },
            prior_probability=0.15,
            tags=["hierarchical", "status-conscious", "power-aware", "traditional"],
            contradicts=["egalitarian_id"],
            compatible_with=["social_conformist_id"]
        ))
        
        # 10. Cooperative Strategist
        self.add_hypothesis(CognitiveHypothesis(
            name="Cooperative Strategist",
            description="Seeks win-win solutions and mutual benefit in social interactions",
            predicted_response_patterns={
                "prisoners_dilemma": {
                    "cooperate": 0.8,
                    "defect": 0.2
                },
                "negotiation": {
                    "seek_mutual_gain": 0.85,
                    "zero_sum_approach": 0.15
                },
                "team_dynamics": {
                    "collaborative": 0.9,
                    "competitive": 0.1
                },
                "trust_game": {
                    "trust_first": 0.75,
                    "distrust_first": 0.25
                }
            },
            cognitive_attributes={
                "cooperation": 0.9,
                "trust_propensity": 0.8,
                "reciprocity": 0.85,
                "positive_sum_thinking": 0.88,
                "social_capital": 0.85
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "cooperation": (0.85, 0.95),
                "positive_sum_thinking": (0.83, 0.93)
            },
            prior_probability=0.18,
            tags=["cooperative", "collaborative", "win-win", "trusting"],
            contradicts=["competitive_strategist_id"],
            compatible_with=["collectivist_thinker_id", "fairness_maximizer_id"]
        ))
        
        return self.hypotheses