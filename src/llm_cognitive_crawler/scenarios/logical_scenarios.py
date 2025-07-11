"""Logical reasoning scenario generator."""

from typing import List
from .base import ScenarioGenerator, ScenarioTemplate, DifficultyLevel
from ..core.data_models import CognitiveDomain, ResponseType


class LogicalReasoningGenerator(ScenarioGenerator):
    """Generator for logical reasoning scenarios."""
    
    def __init__(self, random_seed=None):
        super().__init__(CognitiveDomain.LOGICAL_REASONING, random_seed)
    
    def create_templates(self) -> List[ScenarioTemplate]:
        """Create templates for logical reasoning scenarios."""
        templates = []
        
        # 1. Syllogistic reasoning (15 scenarios)
        templates.extend(self._create_syllogistic_templates())
        
        # 2. Probability reasoning (10 scenarios)
        templates.extend(self._create_probability_templates())
        
        # 3. Causal reasoning (8 scenarios)
        templates.extend(self._create_causal_templates())
        
        # 4. Counterfactual reasoning (6 scenarios)
        templates.extend(self._create_counterfactual_templates())
        
        # 5. Fallacy detection (12 scenarios)
        templates.extend(self._create_fallacy_templates())
        
        return templates
    
    def _create_syllogistic_templates(self) -> List[ScenarioTemplate]:
        """Create syllogistic reasoning scenarios."""
        return [
            # Valid syllogism - Barbara (AAA-1)
            ScenarioTemplate(
                title_template="Valid Syllogism - Universal Affirmative",
                description_template="Testing valid deductive reasoning",
                prompt_template="Premise 1: All {category_a} are {category_b}. Premise 2: All {category_b} are {category_c}. What can we conclude about the relationship between {category_a} and {category_c}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "category_a": ["mammals", "professors", "trees"],
                    "category_b": ["vertebrates", "educators", "plants"],
                    "category_c": ["animals", "professionals", "living things"]
                },
                expected_patterns={
                    "all": 0.9,
                    "valid": 0.7,
                    "conclusion": 0.8,
                    "therefore": 0.7
                },
                tags=["syllogism", "valid", "barbara", "deduction"]
            ),
            
            # Invalid syllogism - Affirming consequent
            ScenarioTemplate(
                title_template="Invalid Syllogism - Affirming Consequent",
                description_template="Testing detection of logical fallacy",
                prompt_template="Premise 1: If {condition}, then {result}. Premise 2: {result} is true. Can we conclude that {condition} is true? Explain your reasoning.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "condition": [
                        "it rains",
                        "someone studies hard",
                        "a car breaks down"
                    ],
                    "result": [
                        "the ground is wet",
                        "they pass the exam",
                        "they are late"
                    ]
                },
                expected_patterns={
                    "invalid": 0.8,
                    "fallacy": 0.7,
                    "other causes": 0.6,
                    "cannot conclude": 0.8
                },
                tags=["syllogism", "invalid", "affirming_consequent", "fallacy"]
            ),
            
            # Valid syllogism - Modus Ponens
            ScenarioTemplate(
                title_template="Modus Ponens",
                description_template="Testing conditional reasoning",
                prompt_template="If {antecedent}, then {consequent}. {antecedent} is true. What can we conclude?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.MULTIPLE_CHOICE,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "antecedent": [
                        "a number is divisible by 4",
                        "someone has a fever",
                        "it's a weekend"
                    ],
                    "consequent": [
                        "it's divisible by 2",
                        "they are sick",
                        "banks are closed"
                    ]
                },
                expected_patterns={
                    "valid": 0.9,
                    "conclude": 0.8,
                    "follows": 0.7
                },
                tags=["modus_ponens", "conditional", "valid", "implication"]
            ),
            
            # Valid syllogism - Modus Tollens
            ScenarioTemplate(
                title_template="Modus Tollens",
                description_template="Testing contrapositive reasoning",
                prompt_template="If {antecedent}, then {consequent}. {consequent} is NOT true. What can we conclude about {antecedent}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "antecedent": [
                        "it's raining",
                        "the battery is dead",
                        "she's in Paris"
                    ],
                    "consequent": [
                        "the streets are wet",
                        "the car won't start",
                        "she can see the Eiffel Tower"
                    ]
                },
                expected_patterns={
                    "not": 0.9,
                    "false": 0.8,
                    "contrapositive": 0.5,
                    "valid": 0.7
                },
                tags=["modus_tollens", "contrapositive", "valid", "negation"]
            ),
            
            # Categorical syllogism with negation
            ScenarioTemplate(
                title_template="Syllogism with Negation",
                description_template="Testing reasoning with negative premises",
                prompt_template="Premise 1: No {category_a} are {category_b}. Premise 2: All {category_c} are {category_b}. What is the relationship between {category_a} and {category_c}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "category_a": ["reptiles", "students", "metals"],
                    "category_b": ["warm-blooded", "employees", "transparent"],
                    "category_c": ["mammals", "teachers", "glass"]
                },
                expected_patterns={
                    "no": 0.9,
                    "none": 0.8,
                    "disjoint": 0.6,
                    "cannot be": 0.7
                },
                tags=["syllogism", "negation", "categorical", "exclusion"]
            ),
            
            # Particular affirmative syllogism
            ScenarioTemplate(
                title_template="Particular Affirmative Syllogism",
                description_template="Testing reasoning with 'some' statements",
                prompt_template="Premise 1: Some {category_a} are {category_b}. Premise 2: All {category_b} are {category_c}. What can we conclude about {category_a} and {category_c}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "category_a": ["athletes", "books", "countries"],
                    "category_b": ["swimmers", "bestsellers", "islands"],
                    "category_c": ["fit people", "popular items", "surrounded by water"]
                },
                expected_patterns={
                    "some": 0.9,
                    "at least": 0.7,
                    "exist": 0.6,
                    "valid": 0.6
                },
                tags=["syllogism", "particular", "existential", "some"]
            ),
            
            # Invalid conversion
            ScenarioTemplate(
                title_template="Invalid Conversion",
                description_template="Testing understanding of logical conversion",
                prompt_template="If 'All {category_a} are {category_b}' is true, can we conclude that 'All {category_b} are {category_a}'? Explain why or why not.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "category_a": ["dogs", "roses", "squares"],
                    "category_b": ["animals", "flowers", "rectangles"]
                },
                expected_patterns={
                    "no": 0.8,
                    "invalid": 0.7,
                    "not all": 0.7,
                    "subset": 0.6,
                    "counterexample": 0.5
                },
                tags=["conversion", "invalid", "universal", "subset"]
            ),
            
            # Disjunctive syllogism
            ScenarioTemplate(
                title_template="Disjunctive Syllogism",
                description_template="Testing either/or reasoning",
                prompt_template="Either {option_a} or {option_b} (but not both). We know that {option_a} is false. What can we conclude?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "option_a": [
                        "the door is locked",
                        "she took the bus",
                        "it's Monday"
                    ],
                    "option_b": [
                        "the door is open",
                        "she took the train",
                        "it's Tuesday"
                    ]
                },
                expected_patterns={
                    "must be": 0.9,
                    "therefore": 0.7,
                    "true": 0.8,
                    "conclude": 0.7
                },
                tags=["disjunctive", "either_or", "elimination", "valid"]
            ),
            
            # Hypothetical syllogism
            ScenarioTemplate(
                title_template="Hypothetical Syllogism",
                description_template="Testing chain reasoning",
                prompt_template="If {a}, then {b}. If {b}, then {c}. What can we conclude about the relationship between {a} and {c}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "a": ["you study hard", "it snows", "prices increase"],
                    "b": ["you understand the material", "schools close", "demand decreases"],
                    "c": ["you pass the exam", "parents stay home", "production slows"]
                },
                expected_patterns={
                    "if then": 0.8,
                    "transitive": 0.5,
                    "chain": 0.6,
                    "implies": 0.7
                },
                tags=["hypothetical", "transitive", "chain", "conditional"]
            ),
            
            # Complex categorical
            ScenarioTemplate(
                title_template="Complex Categorical Reasoning",
                description_template="Testing multi-premise categorical logic",
                prompt_template="Given: 1) All {a} are {b}, 2) No {b} are {c}, 3) Some {d} are {c}. What can we conclude about the relationship between {a} and {d}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "a": ["scientists", "tigers", "computers"],
                    "b": ["researchers", "felines", "machines"],
                    "c": ["artists", "herbivores", "organic"],
                    "d": ["professors", "animals", "systems"]
                },
                expected_patterns={
                    "not all": 0.7,
                    "some are not": 0.8,
                    "cannot be": 0.6,
                    "disjoint": 0.5
                },
                tags=["complex", "categorical", "multi_premise", "advanced"]
            ),
            
            # Sorites (chain syllogism)
            ScenarioTemplate(
                title_template="Sorites Chain",
                description_template="Testing extended chain reasoning",
                prompt_template="Given: {a} are {b}, {b} are {c}, {c} are {d}, {d} are {e}. What is the relationship between {a} and {e}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "a": ["All sparrows", "All CEOs", "All diamonds"],
                    "b": ["birds", "executives", "crystals"],
                    "c": ["vertebrates", "managers", "minerals"],
                    "d": ["animals", "employees", "natural substances"],
                    "e": ["living things", "people", "materials"]
                },
                expected_patterns={
                    "all": 0.8,
                    "are": 0.9,
                    "transitive": 0.5,
                    "therefore": 0.6
                },
                tags=["sorites", "chain", "extended", "transitive"]
            ),
            
            # Existential instantiation
            ScenarioTemplate(
                title_template="Existential Reasoning",
                description_template="Testing reasoning about existence",
                prompt_template="Some {category} have property {property}. We meet a specific {category} named X. Can we conclude X has {property}? Explain.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "category": ["birds", "metals", "students"],
                    "property": ["the ability to fly", "magnetic properties", "perfect grades"]
                },
                expected_patterns={
                    "cannot": 0.8,
                    "not necessarily": 0.8,
                    "some not all": 0.7,
                    "possible": 0.6
                },
                tags=["existential", "instantiation", "some", "particular"]
            ),
            
            # Universal instantiation
            ScenarioTemplate(
                title_template="Universal Instantiation",
                description_template="Testing application of universal statements",
                prompt_template="All {category} have property {property}. Object X is a {category}. What can we conclude about X?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "category": ["triangles", "mammals", "prime numbers"],
                    "property": ["three sides", "warm blood", "exactly two factors"]
                },
                expected_patterns={
                    "has": 0.9,
                    "must": 0.8,
                    "therefore": 0.7,
                    "conclude": 0.7
                },
                tags=["universal", "instantiation", "application", "deduction"]
            ),
            
            # Contraposition
            ScenarioTemplate(
                title_template="Contrapositive Reasoning",
                description_template="Testing understanding of contraposition",
                prompt_template="Statement: 'If {p}, then {q}'. What is the contrapositive of this statement, and is it logically equivalent?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "p": ["a number is even", "it's a mammal", "you're eligible"],
                    "q": ["it's divisible by 2", "it's warm-blooded", "you can apply"]
                },
                expected_patterns={
                    "if not": 0.8,
                    "then not": 0.8,
                    "equivalent": 0.8,
                    "contrapositive": 0.7
                },
                tags=["contrapositive", "equivalence", "conditional", "logic"]
            ),
            
            # Biconditional reasoning
            ScenarioTemplate(
                title_template="Biconditional Logic",
                description_template="Testing if-and-only-if reasoning",
                prompt_template="Statement: '{a} if and only if {b}'. Given that {given_condition}, what can we conclude?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "a": ["a triangle is equilateral", "water freezes", "a number is even"],
                    "b": ["all sides are equal", "temperature is below 0°C", "it's divisible by 2"],
                    "given_condition": ["all sides are equal", "temperature is 5°C", "the number is 7"]
                },
                expected_patterns={
                    "if and only if": 0.6,
                    "both ways": 0.5,
                    "equivalent": 0.6,
                    "necessary and sufficient": 0.4
                },
                tags=["biconditional", "iff", "equivalence", "necessary_sufficient"]
            )
        ]
    
    def _create_probability_templates(self) -> List[ScenarioTemplate]:
        """Create probability reasoning scenarios."""
        return [
            # Base rate fallacy
            ScenarioTemplate(
                title_template="Base Rate Reasoning",
                description_template="Testing consideration of base rates",
                prompt_template="In a city, {base_rate}% of people have {condition}. A test for {condition} is {accuracy}% accurate. Someone tests positive. What's the probability they actually have {condition}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "base_rate": ["1", "5", "0.1"],
                    "condition": ["a rare disease", "a genetic marker", "a specific trait"],
                    "accuracy": ["95", "99", "90"]
                },
                expected_patterns={
                    "base rate": 0.7,
                    "bayes": 0.6,
                    "prior": 0.5,
                    "false positive": 0.6,
                    "less than": 0.7
                },
                tags=["probability", "base_rate", "bayes", "medical_testing"]
            ),
            
            # Conjunction fallacy
            ScenarioTemplate(
                title_template="Conjunction Probability",
                description_template="Testing understanding of conjunction rule",
                prompt_template="{person} is {description}. Which is more probable: (A) {person} is a {option_a}, or (B) {person} is a {option_a} who {option_b}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.MULTIPLE_CHOICE,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "person": ["Linda", "John", "Maria"],
                    "description": [
                        "31, single, outspoken, and very bright",
                        "45, married, quiet, and analytical",
                        "28, athletic, social, and ambitious"
                    ],
                    "option_a": ["bank teller", "engineer", "teacher"],
                    "option_b": ["is active in social justice", "plays chess", "coaches youth sports"]
                },
                expected_patterns={
                    "A": 0.8,
                    "more probable": 0.7,
                    "conjunction": 0.5,
                    "subset": 0.6
                },
                tags=["probability", "conjunction", "fallacy", "linda_problem"]
            ),
            
            # Monty Hall problem
            ScenarioTemplate(
                title_template="Three Door Problem",
                description_template="Testing conditional probability reasoning",
                prompt_template="You choose door {initial} from 3 doors. Behind one is a {prize}, others have {nothing}. Host opens door {opened} showing {nothing}. Should you switch to door {remaining}? What's the probability?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "initial": ["1", "A", "X"],
                    "prize": ["car", "prize", "treasure"],
                    "nothing": ["goats", "nothing", "empty"],
                    "opened": ["2", "B", "Y"],
                    "remaining": ["3", "C", "Z"]
                },
                expected_patterns={
                    "switch": 0.7,
                    "2/3": 0.8,
                    "better odds": 0.6,
                    "conditional": 0.5
                },
                tags=["probability", "monty_hall", "conditional", "counterintuitive"]
            ),
            
            # Gambler's fallacy
            ScenarioTemplate(
                title_template="Independent Events",
                description_template="Testing understanding of independence",
                prompt_template="A fair {object} has landed on {outcome} {streak} times in a row. What's the probability it lands on {outcome} on the next {action}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "object": ["coin", "die", "roulette wheel"],
                    "outcome": ["heads", "six", "red"],
                    "streak": ["5", "10", "7"],
                    "action": ["flip", "roll", "spin"]
                },
                expected_patterns={
                    "same": 0.8,
                    "independent": 0.7,
                    "50%": 0.7,
                    "doesn't affect": 0.6,
                    "fallacy": 0.5
                },
                tags=["probability", "independence", "gamblers_fallacy", "common_error"]
            ),
            
            # Conditional probability
            ScenarioTemplate(
                title_template="Conditional Probability",
                description_template="Testing P(A|B) reasoning",
                prompt_template="In a group: {stat_1}% are {property_a}, {stat_2}% are {property_b}, and {stat_3}% are both. If someone is {property_b}, what's the probability they're also {property_a}?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "stat_1": ["60", "40", "70"],
                    "property_a": ["female", "graduates", "employed"],
                    "stat_2": ["50", "30", "80"],
                    "property_b": ["engineers", "athletes", "managers"],
                    "stat_3": ["20", "15", "35"]
                },
                expected_patterns={
                    "conditional": 0.6,
                    "given": 0.7,
                    "divide": 0.6,
                    "P(": 0.5
                },
                tags=["probability", "conditional", "bayes", "statistics"]
            ),
            
            # Law of large numbers
            ScenarioTemplate(
                title_template="Law of Large Numbers",
                description_template="Testing understanding of convergence",
                prompt_template="After flipping a fair coin {small_n} times, you get {small_result}% heads. After {large_n} flips, what percentage of heads do you expect?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "small_n": ["10", "20", "5"],
                    "small_result": ["70", "80", "20"],
                    "large_n": ["1000", "10000", "100000"]
                },
                expected_patterns={
                    "50": 0.8,
                    "closer": 0.7,
                    "converge": 0.6,
                    "law of large": 0.5
                },
                tags=["probability", "law_of_large_numbers", "convergence", "expectation"]
            ),
            
            # Birthday paradox
            ScenarioTemplate(
                title_template="Birthday Probability",
                description_template="Testing counterintuitive probability",
                prompt_template="In a group of {n} people, what's the approximate probability that at least two share the same birthday? Is this higher or lower than most people expect?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "n": ["23", "30", "50"]
                },
                expected_patterns={
                    "50": 0.6,
                    "higher": 0.7,
                    "surprising": 0.5,
                    "counterintuitive": 0.5
                },
                tags=["probability", "birthday_paradox", "counterintuitive", "combinations"]
            ),
            
            # False positive paradox
            ScenarioTemplate(
                title_template="False Positive Reasoning",
                description_template="Testing understanding of screening paradox",
                prompt_template="A {test} for {rare_condition} (affecting {rate}% of people) has {sensitivity}% sensitivity and {specificity}% specificity. Most positive tests are actually false positives. Why?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "test": ["screening test", "diagnostic", "detector"],
                    "rare_condition": ["rare cancer", "uncommon disease", "genetic condition"],
                    "rate": ["0.1", "0.5", "1"],
                    "sensitivity": ["99", "95", "99.9"],
                    "specificity": ["95", "99", "98"]
                },
                expected_patterns={
                    "rare": 0.8,
                    "base rate": 0.7,
                    "false positive": 0.8,
                    "outnumber": 0.6
                },
                tags=["probability", "false_positive", "screening", "base_rate"]
            ),
            
            # Simpson's paradox
            ScenarioTemplate(
                title_template="Simpson's Paradox",
                description_template="Testing understanding of statistical paradox",
                prompt_template="Treatment A beats Treatment B in {group_1} (A: {a1}% vs B: {b1}%) and in {group_2} (A: {a2}% vs B: {b2}%). Yet overall, B beats A. How is this possible?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "group_1": ["men", "young patients", "mild cases"],
                    "group_2": ["women", "elderly patients", "severe cases"],
                    "a1": ["70", "80", "90"],
                    "b1": ["60", "70", "85"],
                    "a2": ["40", "50", "60"],
                    "b2": ["30", "40", "55"]
                },
                expected_patterns={
                    "sample size": 0.6,
                    "proportion": 0.7,
                    "weight": 0.6,
                    "aggregation": 0.5,
                    "paradox": 0.5
                },
                tags=["probability", "simpsons_paradox", "statistics", "aggregation"]
            ),
            
            # Expected value
            ScenarioTemplate(
                title_template="Expected Value Calculation",
                description_template="Testing expected value reasoning",
                prompt_template="Game: Pay ${cost} to play. {prob_1}% chance to win ${prize_1}, {prob_2}% chance to win ${prize_2}, otherwise win nothing. What's the expected value? Should you play?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "cost": ["10", "5", "20"],
                    "prob_1": ["10", "20", "5"],
                    "prize_1": ["50", "20", "100"],
                    "prob_2": ["30", "40", "15"],
                    "prize_2": ["20", "10", "50"]
                },
                expected_patterns={
                    "expected": 0.8,
                    "average": 0.6,
                    "multiply": 0.7,
                    "sum": 0.6,
                    "negative": 0.5
                },
                tags=["probability", "expected_value", "decision", "gambling"]
            )
        ]
    
    def _create_causal_templates(self) -> List[ScenarioTemplate]:
        """Create causal reasoning scenarios."""
        return [
            # Correlation vs causation
            ScenarioTemplate(
                title_template="Correlation vs Causation",
                description_template="Testing distinction between correlation and causation",
                prompt_template="Study finds: {correlation}. Can we conclude that {causal_claim}? What other explanations are possible?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "correlation": [
                        "ice cream sales correlate with drowning deaths",
                        "shoe size correlates with reading ability in children",
                        "coffee consumption correlates with heart disease"
                    ],
                    "causal_claim": [
                        "ice cream causes drowning",
                        "bigger feet improve reading",
                        "coffee causes heart problems"
                    ]
                },
                expected_patterns={
                    "correlation not causation": 0.8,
                    "third variable": 0.7,
                    "confound": 0.6,
                    "alternative": 0.7
                },
                tags=["causal", "correlation", "confounding", "statistics"]
            ),
            
            # Reverse causation
            ScenarioTemplate(
                title_template="Reverse Causation",
                description_template="Testing consideration of causal direction",
                prompt_template="Observation: {observation}. Hypothesis: {forward_cause}. Could the causation run in the opposite direction? Explain.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "observation": [
                        "depressed people often have fewer friends",
                        "successful companies have happy employees",
                        "fit people eat healthy food"
                    ],
                    "forward_cause": [
                        "lack of friends causes depression",
                        "success makes employees happy",
                        "fitness motivates healthy eating"
                    ]
                },
                expected_patterns={
                    "reverse": 0.7,
                    "opposite": 0.6,
                    "could be": 0.7,
                    "direction": 0.6,
                    "both ways": 0.5
                },
                tags=["causal", "reverse", "direction", "bidirectional"]
            ),
            
            # Common cause
            ScenarioTemplate(
                title_template="Common Cause Reasoning",
                description_template="Testing identification of common causes",
                prompt_template="Phenomena: {event_1} and {event_2} often occur together. Rather than one causing the other, what common cause might explain both?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "event_1": [
                        "yellow teeth",
                        "high crime rates",
                        "poor grades"
                    ],
                    "event_2": [
                        "lung cancer",
                        "poverty",
                        "behavioral problems"
                    ]
                },
                expected_patterns={
                    "common": 0.7,
                    "third": 0.6,
                    "underlying": 0.6,
                    "both caused by": 0.7
                },
                tags=["causal", "common_cause", "third_variable", "confounding"]
            ),
            
            # Causal chain
            ScenarioTemplate(
                title_template="Causal Chain Analysis",
                description_template="Testing understanding of causal chains",
                prompt_template="{event_a} leads to {event_b}, which leads to {event_c}. If we prevent {event_b}, what happens to the causal chain?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "event_a": [
                        "Deforestation",
                        "Poor education",
                        "Pollution"
                    ],
                    "event_b": [
                        "soil erosion",
                        "limited job opportunities",
                        "health problems"
                    ],
                    "event_c": [
                        "crop failure",
                        "poverty",
                        "increased healthcare costs"
                    ]
                },
                expected_patterns={
                    "break": 0.7,
                    "prevent": 0.8,
                    "chain": 0.6,
                    "interrupt": 0.6
                },
                tags=["causal", "chain", "intervention", "mechanism"]
            ),
            
            # Multiple causes
            ScenarioTemplate(
                title_template="Multiple Causation",
                description_template="Testing understanding of multiple causes",
                prompt_template="{outcome} increased by {percentage}%. Proposed causes: {cause_1}, {cause_2}, {cause_3}. How would you determine the relative contribution of each?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "outcome": ["Obesity rates", "Traffic accidents", "Student performance"],
                    "percentage": ["20", "30", "15"],
                    "cause_1": ["increased fast food", "more cars on road", "better teachers"],
                    "cause_2": ["less exercise", "distracted driving", "smaller classes"],
                    "cause_3": ["genetic factors", "poor road design", "new curriculum"]
                },
                expected_patterns={
                    "control": 0.6,
                    "isolate": 0.6,
                    "study": 0.7,
                    "compare": 0.6,
                    "multiple": 0.7
                },
                tags=["causal", "multiple_causes", "contribution", "analysis"]
            ),
            
            # Necessary vs sufficient
            ScenarioTemplate(
                title_template="Necessary vs Sufficient Causes",
                description_template="Testing understanding of causal conditions",
                prompt_template="For {outcome}: {condition_1} is observed in 90% of cases, {condition_2} in 60%, and {condition_3} in 100%. Which are necessary vs sufficient causes?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "outcome": ["fire", "plant growth", "disease"],
                    "condition_1": ["oxygen present", "sunlight", "genetic predisposition"],
                    "condition_2": ["heat source", "water", "environmental trigger"],
                    "condition_3": ["combustible material", "carbon dioxide", "pathogen exposure"]
                },
                expected_patterns={
                    "necessary": 0.8,
                    "sufficient": 0.7,
                    "100%": 0.6,
                    "always present": 0.6,
                    "not enough": 0.5
                },
                tags=["causal", "necessary", "sufficient", "conditions"]
            ),
            
            # Feedback loops
            ScenarioTemplate(
                title_template="Feedback Loop Reasoning",
                description_template="Testing understanding of feedback mechanisms",
                prompt_template="{initial_change} causes {effect}, which in turn {feedback_effect} the original change. Is this a positive or negative feedback loop? What are the implications?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "initial_change": [
                        "Global warming",
                        "Economic recession",
                        "Population growth"
                    ],
                    "effect": [
                        "melts polar ice",
                        "reduces spending",
                        "increases resource use"
                    ],
                    "feedback_effect": [
                        "reduces Earth's reflectivity, increasing",
                        "lowers business revenue, worsening",
                        "degrades environment, limiting"
                    ]
                },
                expected_patterns={
                    "positive feedback": 0.5,
                    "negative feedback": 0.5,
                    "amplify": 0.6,
                    "stabilize": 0.6,
                    "runaway": 0.5
                },
                tags=["causal", "feedback", "systems", "dynamics"]
            ),
            
            # Causal inference from data
            ScenarioTemplate(
                title_template="Causal Inference from Patterns",
                description_template="Testing causal reasoning from data patterns",
                prompt_template="Data shows: When {intervention}, {outcome} changes from {before}% to {after}%. Control group shows no change. What causal conclusion is warranted?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "intervention": [
                        "new teaching method introduced",
                        "speed limits reduced",
                        "health program implemented"
                    ],
                    "outcome": [
                        "test scores",
                        "accident rates",
                        "disease incidence"
                    ],
                    "before": ["60", "15", "30"],
                    "after": ["75", "10", "20"]
                },
                expected_patterns={
                    "causal": 0.7,
                    "evidence": 0.7,
                    "control": 0.8,
                    "suggests": 0.6,
                    "effective": 0.6
                },
                tags=["causal", "inference", "experimental", "control"]
            )
        ]
    
    def _create_counterfactual_templates(self) -> List[ScenarioTemplate]:
        """Create counterfactual reasoning scenarios."""
        return [
            # Historical counterfactual
            ScenarioTemplate(
                title_template="Historical Counterfactual",
                description_template="Testing alternative history reasoning",
                prompt_template="If {historical_change}, how might {domain} be different today? What chain of events would likely have followed?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "historical_change": [
                        "the printing press was never invented",
                        "antibiotics were discovered 100 years earlier",
                        "the internet was developed in the 1950s"
                    ],
                    "domain": [
                        "education and literacy",
                        "human population and cities",
                        "global communication and commerce"
                    ]
                },
                expected_patterns={
                    "would": 0.8,
                    "might": 0.7,
                    "consequence": 0.6,
                    "different": 0.7,
                    "chain": 0.5
                },
                tags=["counterfactual", "historical", "what_if", "causal_chain"]
            ),
            
            # Scientific counterfactual
            ScenarioTemplate(
                title_template="Scientific Counterfactual",
                description_template="Testing reasoning about alternative physical laws",
                prompt_template="If {physical_change}, what would be the implications for {system}? Consider both immediate and long-term effects.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "physical_change": [
                        "gravity was twice as strong",
                        "water froze at 10°C instead of 0°C",
                        "light traveled at half its current speed"
                    ],
                    "system": [
                        "life on Earth",
                        "climate and weather",
                        "space and time"
                    ]
                },
                expected_patterns={
                    "would": 0.8,
                    "impossible": 0.5,
                    "adapt": 0.5,
                    "consequence": 0.7,
                    "fundamental": 0.6
                },
                tags=["counterfactual", "scientific", "physics", "hypothetical"]
            ),
            
            # Personal counterfactual
            ScenarioTemplate(
                title_template="Personal Decision Counterfactual",
                description_template="Testing reasoning about alternative choices",
                prompt_template="Someone chose {actual_choice} over {alternative}. Years later, {outcome}. Should they conclude the alternative would have been better? Why or why not?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "actual_choice": [
                        "stable job",
                        "moving to a new city",
                        "studying medicine"
                    ],
                    "alternative": [
                        "startup opportunity",
                        "staying home",
                        "pursuing art"
                    ],
                    "outcome": [
                        "they feel unfulfilled",
                        "they're successful but stressed",
                        "they have financial security but no passion"
                    ]
                },
                expected_patterns={
                    "cannot know": 0.7,
                    "unknowable": 0.6,
                    "might have": 0.6,
                    "hindsight": 0.5,
                    "different problems": 0.5
                },
                tags=["counterfactual", "personal", "regret", "uncertainty"]
            ),
            
            # Policy counterfactual
            ScenarioTemplate(
                title_template="Policy Counterfactual",
                description_template="Testing reasoning about alternative policies",
                prompt_template="Country A implemented {policy} while similar Country B didn't. A saw {result}. Can we conclude B would see the same result if they implemented it?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "policy": [
                        "universal basic income",
                        "strict gun control",
                        "free university education"
                    ],
                    "result": [
                        "reduced poverty",
                        "lower crime rates",
                        "increased innovation"
                    ]
                },
                expected_patterns={
                    "different": 0.7,
                    "context": 0.8,
                    "factors": 0.7,
                    "cannot assume": 0.6,
                    "culture": 0.5
                },
                tags=["counterfactual", "policy", "comparison", "generalization"]
            ),
            
            # Biological counterfactual
            ScenarioTemplate(
                title_template="Evolutionary Counterfactual",
                description_template="Testing reasoning about alternative evolution",
                prompt_template="If {evolutionary_event} had not occurred, how might {biological_feature} have evolved differently? What alternatives were possible?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "evolutionary_event": [
                        "the asteroid impact 66 million years ago",
                        "the evolution of flowering plants",
                        "the development of eyes"
                    ],
                    "biological_feature": [
                        "mammalian dominance",
                        "insect pollination",
                        "predator-prey relationships"
                    ]
                },
                expected_patterns={
                    "might": 0.7,
                    "alternative": 0.7,
                    "selection": 0.6,
                    "different": 0.8,
                    "adapt": 0.6
                },
                tags=["counterfactual", "evolution", "biology", "alternatives"]
            ),
            
            # Technological counterfactual
            ScenarioTemplate(
                title_template="Technological Development Counterfactual",
                description_template="Testing reasoning about alternative tech development",
                prompt_template="If {tech_assumption} were true, how would {technology} have developed differently? What would be the societal implications?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "tech_assumption": [
                        "battery technology was 10x more efficient from the start",
                        "quantum computing was achieved in the 1980s",
                        "AI development had focused on symbolic reasoning only"
                    ],
                    "technology": [
                        "electric vehicles and renewable energy",
                        "cryptography and internet security",
                        "machine learning and automation"
                    ]
                },
                expected_patterns={
                    "earlier": 0.6,
                    "different": 0.7,
                    "society": 0.6,
                    "implications": 0.7,
                    "development": 0.6
                },
                tags=["counterfactual", "technology", "innovation", "society"]
            )
        ]
    
    def _create_fallacy_templates(self) -> List[ScenarioTemplate]:
        """Create fallacy detection scenarios."""
        return [
            # Ad hominem
            ScenarioTemplate(
                title_template="Ad Hominem Fallacy",
                description_template="Testing recognition of personal attacks",
                prompt_template="Person A: '{claim}' Person B: 'We shouldn't listen to A because {attack}.' Is B's response a valid refutation? Explain.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "claim": [
                        "We should increase environmental regulations",
                        "This medical treatment is effective",
                        "The economic policy will help"
                    ],
                    "attack": [
                        "they drive a gas-guzzling car",
                        "they're not a doctor",
                        "they're wealthy themselves"
                    ]
                },
                expected_patterns={
                    "ad hominem": 0.8,
                    "fallacy": 0.7,
                    "not valid": 0.8,
                    "attack person": 0.6,
                    "address argument": 0.6
                },
                tags=["fallacy", "ad_hominem", "invalid", "personal_attack"]
            ),
            
            # Straw man
            ScenarioTemplate(
                title_template="Straw Man Fallacy",
                description_template="Testing recognition of misrepresentation",
                prompt_template="Person A: '{position}' Person B responds: 'So you're saying {misrepresentation}?' Is B accurately representing A's position?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "position": [
                        "We should have some gun regulations",
                        "College should be more affordable",
                        "We need immigration reform"
                    ],
                    "misrepresentation": [
                        "we should ban all guns",
                        "education should be completely free",
                        "we should have open borders"
                    ]
                },
                expected_patterns={
                    "straw man": 0.7,
                    "misrepresent": 0.8,
                    "not same": 0.7,
                    "extreme": 0.6,
                    "fallacy": 0.6
                },
                tags=["fallacy", "straw_man", "misrepresentation", "distortion"]
            ),
            
            # False dilemma
            ScenarioTemplate(
                title_template="False Dilemma",
                description_template="Testing recognition of false dichotomies",
                prompt_template="Statement: '{dilemma}' Is this a fair representation of the available options? What's missing?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "dilemma": [
                        "You're either with us or against us",
                        "Either we cut all social programs or go bankrupt",
                        "Support this policy or you don't care about children"
                    ]
                },
                expected_patterns={
                    "false dilemma": 0.7,
                    "more options": 0.8,
                    "middle ground": 0.6,
                    "not only": 0.7,
                    "fallacy": 0.6
                },
                tags=["fallacy", "false_dilemma", "binary", "oversimplification"]
            ),
            
            # Slippery slope
            ScenarioTemplate(
                title_template="Slippery Slope",
                description_template="Testing recognition of slippery slope arguments",
                prompt_template="Argument: 'If we allow {initial_action}, then {consequence_1}, which will lead to {consequence_2}, and eventually {extreme_consequence}.' Evaluate this reasoning.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "initial_action": [
                        "same-sex marriage",
                        "marijuana legalization",
                        "AI in healthcare"
                    ],
                    "consequence_1": [
                        "people will want to marry anything",
                        "everyone will use hard drugs",
                        "doctors will be replaced"
                    ],
                    "consequence_2": [
                        "marriage will lose meaning",
                        "society will collapse",
                        "medical errors will increase"
                    ],
                    "extreme_consequence": [
                        "the end of civilization",
                        "complete anarchy",
                        "human extinction"
                    ]
                },
                expected_patterns={
                    "slippery slope": 0.8,
                    "fallacy": 0.7,
                    "doesn't follow": 0.7,
                    "extreme": 0.6,
                    "evidence": 0.6
                },
                tags=["fallacy", "slippery_slope", "catastrophizing", "chain_reaction"]
            ),
            
            # Appeal to authority
            ScenarioTemplate(
                title_template="Appeal to Authority",
                description_template="Testing appropriate vs inappropriate appeals to authority",
                prompt_template="Argument: '{claim} because {authority} says so.' Is this a valid use of authority? Why or why not?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "claim": [
                        "This medical treatment works",
                        "This economic policy is best",
                        "This historical event happened"
                    ],
                    "authority": [
                        "a famous actor",
                        "a Nobel economist",
                        "my teacher"
                    ]
                },
                expected_patterns={
                    "expertise": 0.7,
                    "relevant": 0.8,
                    "field": 0.6,
                    "evidence": 0.6,
                    "qualified": 0.7
                },
                tags=["fallacy", "authority", "expertise", "credibility"]
            ),
            
            # Circular reasoning
            ScenarioTemplate(
                title_template="Circular Reasoning",
                description_template="Testing recognition of circular arguments",
                prompt_template="Argument: '{premise} because {reason}.' Analysis: The reason is just restating the premise. What's the logical problem here?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "premise": [
                        "The Bible is true",
                        "This medicine is effective",
                        "He's trustworthy"
                    ],
                    "reason": [
                        "it says so in the Bible",
                        "it cures people",
                        "he never lies"
                    ]
                },
                expected_patterns={
                    "circular": 0.8,
                    "begging question": 0.6,
                    "assumes": 0.7,
                    "no evidence": 0.6,
                    "tautology": 0.5
                },
                tags=["fallacy", "circular", "begging_question", "tautology"]
            ),
            
            # Post hoc ergo propter hoc
            ScenarioTemplate(
                title_template="Post Hoc Fallacy",
                description_template="Testing false causal reasoning from sequence",
                prompt_template="Observation: '{event_a} happened, then {event_b} happened. Therefore, {event_a} caused {event_b}.' What's wrong with this reasoning?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "event_a": [
                        "A rooster crowed",
                        "I wore my lucky shirt",
                        "The mayor was elected"
                    ],
                    "event_b": [
                        "the sun rose",
                        "my team won",
                        "crime decreased"
                    ]
                },
                expected_patterns={
                    "post hoc": 0.7,
                    "sequence": 0.6,
                    "correlation": 0.7,
                    "coincidence": 0.6,
                    "other factors": 0.7
                },
                tags=["fallacy", "post_hoc", "false_cause", "sequence"]
            ),
            
            # Hasty generalization
            ScenarioTemplate(
                title_template="Hasty Generalization",
                description_template="Testing recognition of insufficient evidence",
                prompt_template="Statement: 'I met {sample_size} {group} who were {characteristic}, so all {group} must be {characteristic}.' Evaluate this reasoning.",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "sample_size": ["two", "three", "five"],
                    "group": ["engineers", "teenagers", "politicians"],
                    "characteristic": ["introverted", "irresponsible", "dishonest"]
                },
                expected_patterns={
                    "hasty": 0.7,
                    "sample": 0.8,
                    "generalization": 0.8,
                    "not enough": 0.7,
                    "fallacy": 0.6
                },
                tags=["fallacy", "hasty_generalization", "sample_size", "stereotype"]
            ),
            
            # No true Scotsman
            ScenarioTemplate(
                title_template="No True Scotsman",
                description_template="Testing recognition of definition shifting",
                prompt_template="A: 'No {group} would {action}.' B: 'But X is a {group} and did {action}.' A: 'Well, no TRUE {group} would do that.' Is A's response valid?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "group": ["scientist", "Christian", "patriot"],
                    "action": ["reject evidence", "support violence", "criticize their country"]
                },
                expected_patterns={
                    "no true": 0.8,
                    "moving goalpost": 0.6,
                    "redefine": 0.7,
                    "fallacy": 0.7,
                    "arbitrary": 0.5
                },
                tags=["fallacy", "no_true_scotsman", "definition", "moving_goalpost"]
            ),
            
            # Appeal to emotion
            ScenarioTemplate(
                title_template="Appeal to Emotion",
                description_template="Testing recognition of emotional manipulation",
                prompt_template="Argument for {position}: '{emotional_appeal}' Does this emotional appeal constitute a logical argument? What's missing?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "position": [
                        "banning violent video games",
                        "increasing military spending",
                        "restricting immigration"
                    ],
                    "emotional_appeal": [
                        "Think of the innocent children!",
                        "Our brave soldiers are in danger!",
                        "They're taking our jobs and destroying our culture!"
                    ]
                },
                expected_patterns={
                    "emotion": 0.8,
                    "evidence": 0.7,
                    "fallacy": 0.6,
                    "manipulation": 0.5,
                    "facts": 0.6
                },
                tags=["fallacy", "emotional_appeal", "manipulation", "pathos"]
            ),
            
            # Bandwagon fallacy
            ScenarioTemplate(
                title_template="Bandwagon Fallacy",
                description_template="Testing recognition of popularity arguments",
                prompt_template="Argument: '{claim} must be true/good because {popularity_statement}.' Is popularity a valid indicator of truth or quality?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "claim": [
                        "This treatment",
                        "This belief",
                        "This product"
                    ],
                    "popularity_statement": [
                        "millions of people use it",
                        "most people believe it",
                        "everyone's buying it"
                    ]
                },
                expected_patterns={
                    "bandwagon": 0.7,
                    "popularity": 0.8,
                    "fallacy": 0.6,
                    "not evidence": 0.7,
                    "truth": 0.6
                },
                tags=["fallacy", "bandwagon", "popularity", "peer_pressure"]
            ),
            
            # Tu quoque
            ScenarioTemplate(
                title_template="Tu Quoque Fallacy",
                description_template="Testing recognition of hypocrisy deflection",
                prompt_template="A: '{criticism}' B: 'But you do the same thing!' Does B's response refute A's criticism? Why or why not?",
                domain=CognitiveDomain.LOGICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "criticism": [
                        "Smoking is bad for your health",
                        "We should reduce carbon emissions",
                        "Lying is wrong"
                    ]
                },
                expected_patterns={
                    "tu quoque": 0.6,
                    "hypocrisy": 0.7,
                    "doesn't refute": 0.8,
                    "still true": 0.7,
                    "deflection": 0.6
                },
                tags=["fallacy", "tu_quoque", "hypocrisy", "whataboutism"]
            )
        ]