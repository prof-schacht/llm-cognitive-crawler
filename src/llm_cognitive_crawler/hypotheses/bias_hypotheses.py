"""Bias and limitation cognitive hypotheses."""

from typing import List
from .base import HypothesisGenerator, CognitiveHypothesis, HypothesisCategory
from ..core.data_models import CognitiveDomain


class BiasLimitationHypotheses(HypothesisGenerator):
    """Generator for bias and cognitive limitation hypotheses."""
    
    def __init__(self):
        super().__init__(HypothesisCategory.BIAS_LIMITATION)
    
    def generate_hypotheses(self) -> List[CognitiveHypothesis]:
        """Generate all bias and limitation hypotheses."""
        self.hypotheses = []
        
        # 1. Optimism Bias
        self.add_hypothesis(CognitiveHypothesis(
            name="Optimism Bias Agent",
            description="Systematically overestimates positive outcomes and underestimates negative ones",
            predicted_response_patterns={
                "future_prediction": {
                    "positive_outcome": 0.85,
                    "negative_outcome": 0.15
                },
                "risk_assessment": {
                    "underestimate_risk": 0.8,
                    "accurate_risk": 0.2
                },
                "personal_forecast": {
                    "above_average": 0.88,
                    "below_average": 0.12
                },
                "project_timeline": {
                    "optimistic_estimate": 0.85,
                    "pessimistic_estimate": 0.15
                }
            },
            cognitive_attributes={
                "optimism": 0.88,
                "risk_underestimation": 0.8,
                "positive_illusion": 0.85,
                "self_enhancement": 0.82,
                "unrealistic_optimism": 0.85
            },
            domain_specificity=[],  # Applies across domains
            confidence_intervals={
                "optimism": (0.83, 0.93),
                "risk_underestimation": (0.75, 0.85)
            },
            prior_probability=0.3,
            tags=["optimism-bias", "positive-illusion", "risk-blind", "overconfident"],
            contradicts=["pessimism_bias_id", "realistic_assessor_id"],
            compatible_with=["overconfident_decision_maker_id"]
        ))
        
        # 2. Confirmation Bias
        self.add_hypothesis(CognitiveHypothesis(
            name="Confirmation Bias Agent",
            description="Seeks information confirming existing beliefs, avoids contradictory evidence",
            predicted_response_patterns={
                "information_search": {
                    "confirmatory_evidence": 0.8,
                    "disconfirmatory_evidence": 0.2
                },
                "belief_update": {
                    "strengthen_existing": 0.85,
                    "change_belief": 0.15
                },
                "source_selection": {
                    "agreeable_sources": 0.88,
                    "challenging_sources": 0.12
                },
                "interpretation": {
                    "support_prior": 0.82,
                    "neutral_interpretation": 0.18
                }
            },
            cognitive_attributes={
                "confirmation_seeking": 0.85,
                "cognitive_closure": 0.8,
                "belief_persistence": 0.88,
                "selective_exposure": 0.82,
                "motivated_reasoning": 0.85
            },
            domain_specificity=[],
            confidence_intervals={
                "confirmation_seeking": (0.8, 0.9),
                "belief_persistence": (0.83, 0.93)
            },
            prior_probability=0.35,
            tags=["confirmation-bias", "selective", "closed-minded", "belief-persistence"],
            contradicts=["open_minded_id", "truth_seeker_id"],
            compatible_with=["anchoring_bias_id"]
        ))
        
        # 3. Anchoring Bias
        self.add_hypothesis(CognitiveHypothesis(
            name="Anchoring Bias Agent",
            description="Over-relies on first information received, insufficient adjustment from anchors",
            predicted_response_patterns={
                "numerical_estimation": {
                    "anchor_influenced": 0.85,
                    "independent_estimate": 0.15
                },
                "price_judgment": {
                    "anchor_based": 0.8,
                    "value_based": 0.2
                },
                "first_impression": {
                    "stick_to_initial": 0.88,
                    "revise_thoroughly": 0.12
                },
                "negotiation": {
                    "anchor_dependent": 0.82,
                    "reset_baseline": 0.18
                }
            },
            cognitive_attributes={
                "anchor_sensitivity": 0.85,
                "adjustment_insufficiency": 0.8,
                "primacy_effect": 0.82,
                "cognitive_inertia": 0.78,
                "reference_dependence": 0.85
            },
            domain_specificity=[],
            confidence_intervals={
                "anchor_sensitivity": (0.8, 0.9),
                "adjustment_insufficiency": (0.75, 0.85)
            },
            prior_probability=0.3,
            tags=["anchoring", "primacy", "adjustment", "reference-dependent"],
            contradicts=["flexible_updater_id"],
            compatible_with=["confirmation_bias_id"]
        ))
        
        # 4. Availability Heuristic
        self.add_hypothesis(CognitiveHypothesis(
            name="Availability Heuristic User",
            description="Judges probability by ease of recalling examples",
            predicted_response_patterns={
                "frequency_estimation": {
                    "vivid_overestimate": 0.85,
                    "statistical_accuracy": 0.15
                },
                "risk_judgment": {
                    "recent_event_bias": 0.88,
                    "base_rate_use": 0.12
                },
                "decision_making": {
                    "salient_factor": 0.8,
                    "comprehensive_analysis": 0.2
                },
                "probability_assessment": {
                    "memorable_events": 0.85,
                    "actual_probability": 0.15
                }
            },
            cognitive_attributes={
                "availability_reliance": 0.85,
                "recency_effect": 0.82,
                "salience_sensitivity": 0.88,
                "vividness_bias": 0.8,
                "memory_based_judgment": 0.85
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "availability_reliance": (0.8, 0.9),
                "salience_sensitivity": (0.83, 0.93)
            },
            prior_probability=0.28,
            tags=["availability", "heuristic", "memory-based", "salience"],
            contradicts=["statistical_thinker_id"],
            compatible_with=["intuitive_reasoner_id"]
        ))
        
        # 5. Hindsight Bias
        self.add_hypothesis(CognitiveHypothesis(
            name="Hindsight Bias Agent",
            description="Perceives past events as more predictable than they were",
            predicted_response_patterns={
                "outcome_knowledge": {
                    "knew_it_all_along": 0.85,
                    "acknowledge_uncertainty": 0.15
                },
                "prediction_recall": {
                    "overestimate_accuracy": 0.88,
                    "accurate_recall": 0.12
                },
                "event_inevitability": {
                    "see_as_inevitable": 0.8,
                    "recognize_contingency": 0.2
                },
                "learning_from_failure": {
                    "obvious_in_retrospect": 0.85,
                    "genuine_surprise": 0.15
                }
            },
            cognitive_attributes={
                "hindsight_distortion": 0.85,
                "outcome_bias": 0.82,
                "inevitability_illusion": 0.8,
                "memory_reconstruction": 0.88,
                "creeping_determinism": 0.82
            },
            domain_specificity=[],
            confidence_intervals={
                "hindsight_distortion": (0.8, 0.9),
                "memory_reconstruction": (0.83, 0.93)
            },
            prior_probability=0.32,
            tags=["hindsight", "outcome-bias", "retrospective", "inevitability"],
            contradicts=["accurate_historian_id"],
            compatible_with=["overconfident_decision_maker_id"]
        ))
        
        # 6. Framing Effect Susceptible
        self.add_hypothesis(CognitiveHypothesis(
            name="Framing Effect Susceptible",
            description="Decisions heavily influenced by how information is presented",
            predicted_response_patterns={
                "gain_loss_frame": {
                    "frame_dependent": 0.85,
                    "frame_independent": 0.15
                },
                "positive_negative": {
                    "presentation_influenced": 0.88,
                    "content_focused": 0.12
                },
                "reference_point": {
                    "reference_sensitive": 0.82,
                    "absolute_judgment": 0.18
                },
                "statistical_framing": {
                    "format_dependent": 0.8,
                    "invariant_judgment": 0.2
                }
            },
            cognitive_attributes={
                "framing_susceptibility": 0.85,
                "presentation_dependence": 0.88,
                "context_sensitivity": 0.82,
                "reference_dependence": 0.8,
                "surface_processing": 0.75
            },
            domain_specificity=[],
            confidence_intervals={
                "framing_susceptibility": (0.8, 0.9),
                "presentation_dependence": (0.83, 0.93)
            },
            prior_probability=0.4,
            tags=["framing-effect", "presentation-dependent", "context-sensitive", "surface"],
            contradicts=["deep_processor_id"],
            compatible_with=["anchoring_bias_id"]
        ))
        
        # 7. Dunning-Kruger Effect
        self.add_hypothesis(CognitiveHypothesis(
            name="Dunning-Kruger Effect Agent",
            description="Overestimates competence in areas of low expertise",
            predicted_response_patterns={
                "skill_assessment": {
                    "overconfident_novice": 0.85,
                    "accurate_assessment": 0.15
                },
                "knowledge_calibration": {
                    "poor_calibration": 0.88,
                    "well_calibrated": 0.12
                },
                "expertise_recognition": {
                    "fail_to_recognize": 0.8,
                    "acknowledge_expertise": 0.2
                },
                "learning_readiness": {
                    "think_knows_enough": 0.82,
                    "eager_to_learn": 0.18
                }
            },
            cognitive_attributes={
                "metacognitive_deficit": 0.85,
                "overconfidence_ignorance": 0.88,
                "expertise_blindness": 0.82,
                "self_assessment_error": 0.85,
                "incompetence_unawareness": 0.9
            },
            domain_specificity=[],
            confidence_intervals={
                "metacognitive_deficit": (0.8, 0.9),
                "overconfidence_ignorance": (0.83, 0.93)
            },
            prior_probability=0.25,
            tags=["dunning-kruger", "overconfident", "metacognitive", "self-assessment"],
            contradicts=["expert_calibrated_id", "humble_learner_id"],
            compatible_with=["overconfident_decision_maker_id"]
        ))
        
        # 8. Sunk Cost Fallacy
        self.add_hypothesis(CognitiveHypothesis(
            name="Sunk Cost Fallacy Agent",
            description="Continues investment based on past costs rather than future value",
            predicted_response_patterns={
                "investment_decision": {
                    "honor_sunk_cost": 0.85,
                    "ignore_sunk_cost": 0.15
                },
                "project_continuation": {
                    "escalate_commitment": 0.88,
                    "cut_losses": 0.12
                },
                "resource_allocation": {
                    "past_focused": 0.82,
                    "future_focused": 0.18
                },
                "abandonment_decision": {
                    "resist_abandonment": 0.85,
                    "rational_abandonment": 0.15
                }
            },
            cognitive_attributes={
                "sunk_cost_sensitivity": 0.88,
                "commitment_escalation": 0.85,
                "loss_frame_thinking": 0.82,
                "retrospective_focus": 0.8,
                "waste_aversion": 0.85
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "sunk_cost_sensitivity": (0.83, 0.93),
                "commitment_escalation": (0.8, 0.9)
            },
            prior_probability=0.35,
            tags=["sunk-cost", "escalation", "retrospective", "loss-averse"],
            contradicts=["forward_looking_id", "rational_economist_id"],
            compatible_with=["loss_aversion_agent_id"]
        ))
        
        # 9. Fundamental Attribution Error
        self.add_hypothesis(CognitiveHypothesis(
            name="Fundamental Attribution Error Agent",
            description="Overattributes behavior to personality rather than situation",
            predicted_response_patterns={
                "behavior_explanation": {
                    "dispositional": 0.85,
                    "situational": 0.15
                },
                "failure_attribution": {
                    "character_flaw": 0.88,
                    "circumstances": 0.12
                },
                "success_attribution": {
                    "inherent_ability": 0.82,
                    "external_factors": 0.18
                },
                "prediction_basis": {
                    "personality_based": 0.85,
                    "context_based": 0.15
                }
            },
            cognitive_attributes={
                "dispositional_bias": 0.88,
                "situational_blindness": 0.82,
                "correspondence_bias": 0.85,
                "context_neglect": 0.8,
                "person_focus": 0.85
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "dispositional_bias": (0.83, 0.93),
                "situational_blindness": (0.77, 0.87)
            },
            prior_probability=0.4,
            tags=["attribution-error", "dispositional", "context-blind", "person-focused"],
            contradicts=["situational_thinker_id"],
            compatible_with=["individualist_thinker_id"]
        ))
        
        # 10. Cognitive Dissonance Reducer
        self.add_hypothesis(CognitiveHypothesis(
            name="Cognitive Dissonance Reducer",
            description="Actively reduces psychological discomfort from conflicting beliefs",
            predicted_response_patterns={
                "contradiction_response": {
                    "rationalize": 0.85,
                    "acknowledge_conflict": 0.15
                },
                "belief_behavior_gap": {
                    "justify_inconsistency": 0.88,
                    "change_behavior": 0.12
                },
                "decision_justification": {
                    "post_hoc_rationalize": 0.82,
                    "admit_mistake": 0.18
                },
                "information_integration": {
                    "selective_integration": 0.85,
                    "full_integration": 0.15
                }
            },
            cognitive_attributes={
                "dissonance_reduction": 0.88,
                "rationalization": 0.85,
                "consistency_motivation": 0.82,
                "selective_processing": 0.8,
                "self_justification": 0.85
            },
            domain_specificity=[],
            confidence_intervals={
                "dissonance_reduction": (0.83, 0.93),
                "rationalization": (0.8, 0.9)
            },
            prior_probability=0.45,
            tags=["dissonance", "rationalization", "consistency", "self-justification"],
            contradicts=["self_aware_critic_id"],
            compatible_with=["confirmation_bias_id", "motivated_reasoner_id"]
        ))
        
        # 11. Bandwagon Effect Follower
        self.add_hypothesis(CognitiveHypothesis(
            name="Bandwagon Effect Follower",
            description="Adopts beliefs or behaviors because many others do",
            predicted_response_patterns={
                "popularity_influence": {
                    "follow_majority": 0.85,
                    "independent_choice": 0.15
                },
                "trend_adoption": {
                    "join_bandwagon": 0.88,
                    "resist_trend": 0.12
                },
                "belief_formation": {
                    "consensus_based": 0.82,
                    "evidence_based": 0.18
                },
                "social_proof": {
                    "rely_on_others": 0.85,
                    "personal_judgment": 0.15
                }
            },
            cognitive_attributes={
                "social_proof_reliance": 0.88,
                "conformity_tendency": 0.85,
                "majority_influence": 0.82,
                "trend_following": 0.85,
                "consensus_seeking": 0.8
            },
            domain_specificity=[CognitiveDomain.SOCIAL_COGNITION],
            confidence_intervals={
                "social_proof_reliance": (0.83, 0.93),
                "conformity_tendency": (0.8, 0.9)
            },
            prior_probability=0.3,
            tags=["bandwagon", "conformity", "social-proof", "majority-influence"],
            contradicts=["independent_thinker_id"],
            compatible_with=["social_conformist_id"]
        ))
        
        # 12. Planning Fallacy Agent
        self.add_hypothesis(CognitiveHypothesis(
            name="Planning Fallacy Agent",
            description="Systematically underestimates time and resources needed",
            predicted_response_patterns={
                "time_estimation": {
                    "underestimate": 0.88,
                    "accurate_estimate": 0.12
                },
                "resource_planning": {
                    "insufficient_buffer": 0.85,
                    "adequate_buffer": 0.15
                },
                "project_timeline": {
                    "optimistic_schedule": 0.9,
                    "realistic_schedule": 0.1
                },
                "complexity_assessment": {
                    "underestimate_complexity": 0.82,
                    "accurate_assessment": 0.18
                }
            },
            cognitive_attributes={
                "planning_optimism": 0.88,
                "time_underestimation": 0.9,
                "complexity_blindness": 0.82,
                "best_case_focus": 0.85,
                "buffer_neglect": 0.8
            },
            domain_specificity=[],
            confidence_intervals={
                "planning_optimism": (0.83, 0.93),
                "time_underestimation": (0.85, 0.95)
            },
            prior_probability=0.4,
            tags=["planning-fallacy", "optimistic", "underestimation", "time-blind"],
            contradicts=["conservative_planner_id"],
            compatible_with=["optimism_bias_id"]
        ))
        
        return self.hypotheses