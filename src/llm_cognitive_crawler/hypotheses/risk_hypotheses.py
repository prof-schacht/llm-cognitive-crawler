"""Risk and decision-making cognitive hypotheses."""

from typing import List
from .base import HypothesisGenerator, CognitiveHypothesis, HypothesisCategory
from ..core.data_models import CognitiveDomain


class RiskDecisionHypotheses(HypothesisGenerator):
    """Generator for risk and decision-making hypotheses."""
    
    def __init__(self):
        super().__init__(HypothesisCategory.RISK_DECISION)
    
    def generate_hypotheses(self) -> List[CognitiveHypothesis]:
        """Generate all risk and decision-making hypotheses."""
        self.hypotheses = []
        
        # 1. Risk-Averse Agent
        self.add_hypothesis(CognitiveHypothesis(
            name="Risk-Averse Agent",
            description="Strongly prefers certain outcomes over uncertain ones, prioritizes safety",
            predicted_response_patterns={
                "investment_choice": {
                    "guaranteed_return": 0.85,
                    "risky_high_return": 0.15
                },
                "medical_decision": {
                    "proven_treatment": 0.9,
                    "experimental_option": 0.1
                },
                "career_choice": {
                    "stable_job": 0.88,
                    "startup_opportunity": 0.12
                },
                "insurance_decision": {
                    "buy_insurance": 0.9,
                    "self_insure": 0.1
                }
            },
            cognitive_attributes={
                "risk_tolerance": 0.2,
                "safety_priority": 0.9,
                "uncertainty_avoidance": 0.85,
                "loss_aversion": 0.9,
                "conservative_bias": 0.85
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "risk_tolerance": (0.1, 0.3),
                "safety_priority": (0.85, 0.95)
            },
            prior_probability=0.25,
            tags=["risk-averse", "conservative", "safety-focused", "cautious"],
            contradicts=["risk_seeking_agent_id"],
            compatible_with=["cautious_reasoner_id"]
        ))
        
        # 2. Risk-Seeking Agent
        self.add_hypothesis(CognitiveHypothesis(
            name="Risk-Seeking Agent",
            description="Comfortable with uncertainty, actively seeks high-reward opportunities despite risks",
            predicted_response_patterns={
                "investment_choice": {
                    "guaranteed_return": 0.2,
                    "risky_high_return": 0.8
                },
                "adventure_decision": {
                    "extreme_sport": 0.85,
                    "safe_activity": 0.15
                },
                "business_strategy": {
                    "aggressive_expansion": 0.8,
                    "conservative_growth": 0.2
                },
                "gambling_scenario": {
                    "take_gamble": 0.75,
                    "sure_thing": 0.25
                }
            },
            cognitive_attributes={
                "risk_tolerance": 0.85,
                "thrill_seeking": 0.8,
                "optimism_bias": 0.75,
                "gain_focus": 0.85,
                "uncertainty_comfort": 0.8
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "risk_tolerance": (0.8, 0.9),
                "thrill_seeking": (0.7, 0.85)
            },
            prior_probability=0.15,
            tags=["risk-seeking", "adventurous", "optimistic", "gain-focused"],
            contradicts=["risk_averse_agent_id"],
            compatible_with=["optimistic_agent_id"]
        ))
        
        # 3. Expected Value Maximizer
        self.add_hypothesis(CognitiveHypothesis(
            name="Expected Value Maximizer",
            description="Makes mathematically optimal decisions based on probability and value calculations",
            predicted_response_patterns={
                "probability_game": {
                    "ev_optimal_choice": 0.95,
                    "suboptimal_choice": 0.05
                },
                "insurance_math": {
                    "calculate_expected_value": 0.9,
                    "emotional_decision": 0.1
                },
                "lottery_decision": {
                    "reject_negative_ev": 0.95,
                    "play_anyway": 0.05
                },
                "portfolio_allocation": {
                    "optimal_diversification": 0.9,
                    "concentrated_bet": 0.1
                }
            },
            cognitive_attributes={
                "quantitative_reasoning": 0.95,
                "rational_calculation": 0.9,
                "emotion_neutral": 0.85,
                "probability_literacy": 0.9,
                "optimization_focus": 0.9
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT, CognitiveDomain.LOGICAL_REASONING],
            confidence_intervals={
                "quantitative_reasoning": (0.9, 0.98),
                "rational_calculation": (0.85, 0.95)
            },
            prior_probability=0.1,
            tags=["rational", "mathematical", "optimizer", "expected-value"],
            contradicts=["emotion_driven_decider_id"],
            compatible_with=["analytical_reasoner_id"]
        ))
        
        # 4. Loss Aversion Agent
        self.add_hypothesis(CognitiveHypothesis(
            name="Loss Aversion Agent",
            description="Disproportionately weights potential losses over equivalent gains",
            predicted_response_patterns={
                "gain_loss_frame": {
                    "avoid_loss_frame": 0.85,
                    "seek_gain_frame": 0.15
                },
                "endowment_effect": {
                    "keep_possession": 0.8,
                    "trade_fairly": 0.2
                },
                "sunk_cost": {
                    "continue_losing": 0.7,
                    "cut_losses": 0.3
                },
                "status_quo": {
                    "maintain_current": 0.8,
                    "change_position": 0.2
                }
            },
            cognitive_attributes={
                "loss_aversion": 0.9,
                "status_quo_bias": 0.8,
                "endowment_effect": 0.85,
                "reference_dependence": 0.85,
                "asymmetric_valuation": 0.9
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "loss_aversion": (0.85, 0.95),
                "status_quo_bias": (0.7, 0.85)
            },
            prior_probability=0.3,
            tags=["loss-averse", "status-quo", "endowment", "prospect-theory"],
            contradicts=["gain_seeking_id"],
            compatible_with=["risk_averse_agent_id"]
        ))
        
        # 5. Ambiguity Averse Agent
        self.add_hypothesis(CognitiveHypothesis(
            name="Ambiguity Averse Agent",
            description="Avoids situations where probabilities are unknown or unclear",
            predicted_response_patterns={
                "known_vs_unknown": {
                    "known_probability": 0.9,
                    "ambiguous_option": 0.1
                },
                "information_seeking": {
                    "gather_more_data": 0.85,
                    "decide_now": 0.15
                },
                "ellsberg_paradox": {
                    "avoid_ambiguity": 0.8,
                    "indifferent": 0.2
                },
                "unclear_rules": {
                    "seek_clarification": 0.88,
                    "proceed_anyway": 0.12
                }
            },
            cognitive_attributes={
                "ambiguity_aversion": 0.9,
                "certainty_seeking": 0.85,
                "information_need": 0.9,
                "clarity_preference": 0.88,
                "unknown_avoidance": 0.85
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "ambiguity_aversion": (0.85, 0.95),
                "certainty_seeking": (0.8, 0.9)
            },
            prior_probability=0.2,
            tags=["ambiguity-averse", "uncertainty", "information-seeking", "clarity"],
            contradicts=["ambiguity_tolerant_id"],
            compatible_with=["cautious_reasoner_id", "risk_averse_agent_id"]
        ))
        
        # 6. Overconfident Decision Maker
        self.add_hypothesis(CognitiveHypothesis(
            name="Overconfident Decision Maker",
            description="Systematically overestimates own abilities and prediction accuracy",
            predicted_response_patterns={
                "confidence_calibration": {
                    "overconfident_prediction": 0.85,
                    "calibrated_estimate": 0.15
                },
                "skill_assessment": {
                    "overestimate_ability": 0.8,
                    "accurate_assessment": 0.2
                },
                "planning_fallacy": {
                    "underestimate_time": 0.85,
                    "realistic_timeline": 0.15
                },
                "risk_perception": {
                    "underestimate_risk": 0.75,
                    "accurate_risk": 0.25
                }
            },
            cognitive_attributes={
                "overconfidence": 0.85,
                "self_enhancement": 0.8,
                "optimism_bias": 0.85,
                "illusion_of_control": 0.75,
                "planning_fallacy": 0.8
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "overconfidence": (0.8, 0.9),
                "optimism_bias": (0.8, 0.9)
            },
            prior_probability=0.25,
            tags=["overconfident", "optimistic", "self-enhancing", "biased"],
            contradicts=["cautious_reasoner_id", "calibrated_estimator_id"],
            compatible_with=["risk_seeking_agent_id"]
        ))
        
        # 7. Minimax Regret Minimizer
        self.add_hypothesis(CognitiveHypothesis(
            name="Minimax Regret Minimizer",
            description="Minimizes the maximum possible regret from any decision",
            predicted_response_patterns={
                "regret_scenario": {
                    "minimize_max_regret": 0.85,
                    "maximize_expected_value": 0.15
                },
                "missed_opportunity": {
                    "avoid_missing_out": 0.8,
                    "accept_possibility": 0.2
                },
                "decision_framing": {
                    "consider_regret": 0.9,
                    "ignore_regret": 0.1
                },
                "hindsight_consideration": {
                    "anticipate_hindsight": 0.85,
                    "focus_present": 0.15
                }
            },
            cognitive_attributes={
                "regret_sensitivity": 0.9,
                "hindsight_anticipation": 0.85,
                "defensive_decision": 0.8,
                "opportunity_cost_aware": 0.85,
                "anticipatory_emotion": 0.8
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "regret_sensitivity": (0.85, 0.95),
                "defensive_decision": (0.75, 0.85)
            },
            prior_probability=0.15,
            tags=["regret-minimizer", "defensive", "anticipatory", "minimax"],
            contradicts=["impulsive_decider_id"],
            compatible_with=["cautious_reasoner_id"]
        ))
        
        # 8. Satisficing Decision Maker
        self.add_hypothesis(CognitiveHypothesis(
            name="Satisficing Decision Maker",
            description="Seeks 'good enough' solutions rather than optimal ones",
            predicted_response_patterns={
                "option_search": {
                    "stop_at_satisfactory": 0.85,
                    "exhaustive_search": 0.15
                },
                "perfectionism_test": {
                    "accept_good_enough": 0.9,
                    "seek_perfection": 0.1
                },
                "time_pressure": {
                    "quick_satisfactory": 0.88,
                    "delay_for_optimal": 0.12
                },
                "decision_cost": {
                    "minimize_effort": 0.8,
                    "maximize_outcome": 0.2
                }
            },
            cognitive_attributes={
                "satisficing_tendency": 0.9,
                "efficiency_focus": 0.85,
                "pragmatism": 0.85,
                "bounded_rationality": 0.9,
                "effort_conservation": 0.8
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "satisficing_tendency": (0.85, 0.95),
                "bounded_rationality": (0.85, 0.95)
            },
            prior_probability=0.3,
            tags=["satisficer", "pragmatic", "efficient", "bounded-rational"],
            contradicts=["perfectionist_id", "optimizer_id"],
            compatible_with=["pragmatic_reasoner_id"]
        ))
        
        # 9. Temporal Discounting Agent
        self.add_hypothesis(CognitiveHypothesis(
            name="Temporal Discounting Agent",
            description="Heavily discounts future rewards in favor of immediate gains",
            predicted_response_patterns={
                "delayed_gratification": {
                    "immediate_reward": 0.8,
                    "larger_delayed_reward": 0.2
                },
                "savings_decision": {
                    "spend_now": 0.75,
                    "save_for_future": 0.25
                },
                "health_choice": {
                    "immediate_pleasure": 0.7,
                    "long_term_health": 0.3
                },
                "investment_horizon": {
                    "short_term": 0.85,
                    "long_term": 0.15
                }
            },
            cognitive_attributes={
                "present_bias": 0.85,
                "impulsivity": 0.8,
                "future_discounting": 0.9,
                "immediate_gratification": 0.85,
                "short_term_focus": 0.88
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT],
            confidence_intervals={
                "present_bias": (0.8, 0.9),
                "future_discounting": (0.85, 0.95)
            },
            prior_probability=0.25,
            tags=["present-biased", "impulsive", "short-term", "temporal-discounting"],
            contradicts=["long_term_planner_id"],
            compatible_with=["impulsive_decider_id"]
        ))
        
        # 10. Probabilistic Thinker
        self.add_hypothesis(CognitiveHypothesis(
            name="Probabilistic Thinker",
            description="Naturally thinks in terms of probabilities and distributions",
            predicted_response_patterns={
                "uncertainty_expression": {
                    "probabilistic_language": 0.9,
                    "binary_certainty": 0.1
                },
                "forecast_style": {
                    "confidence_intervals": 0.85,
                    "point_estimates": 0.15
                },
                "base_rate_problem": {
                    "use_base_rate": 0.8,
                    "ignore_base_rate": 0.2
                },
                "bayesian_update": {
                    "update_beliefs": 0.85,
                    "stick_to_prior": 0.15
                }
            },
            cognitive_attributes={
                "probabilistic_reasoning": 0.95,
                "uncertainty_comfort": 0.85,
                "statistical_thinking": 0.9,
                "calibration_accuracy": 0.8,
                "bayesian_tendency": 0.85
            },
            domain_specificity=[CognitiveDomain.RISK_ASSESSMENT, CognitiveDomain.LOGICAL_REASONING],
            confidence_intervals={
                "probabilistic_reasoning": (0.9, 0.98),
                "statistical_thinking": (0.85, 0.95)
            },
            prior_probability=0.08,
            tags=["probabilistic", "statistical", "bayesian", "calibrated"],
            contradicts=["binary_thinker_id"],
            compatible_with=["expected_value_maximizer_id", "scientific_reasoner_id"]
        ))
        
        return self.hypotheses