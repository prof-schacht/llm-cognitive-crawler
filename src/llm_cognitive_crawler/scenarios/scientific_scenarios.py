"""Scientific and causal reasoning scenario generator."""

from typing import List
from .base import ScenarioGenerator, ScenarioTemplate, DifficultyLevel
from ..core.data_models import CognitiveDomain, ResponseType


class ScientificReasoningGenerator(ScenarioGenerator):
    """Generator for scientific and causal reasoning scenarios."""
    
    def __init__(self, random_seed=None):
        super().__init__(CognitiveDomain.CAUSAL_REASONING, random_seed)
    
    def create_templates(self) -> List[ScenarioTemplate]:
        """Create templates for scientific reasoning scenarios."""
        templates = []
        
        # 1. Hypothesis testing (8 scenarios)
        templates.extend(self._create_hypothesis_testing_templates())
        
        # 2. Correlation vs causation (6 scenarios)
        templates.extend(self._create_correlation_causation_templates())
        
        # 3. Experimental design (5 scenarios)
        templates.extend(self._create_experimental_design_templates())
        
        return templates
    
    def _create_hypothesis_testing_templates(self) -> List[ScenarioTemplate]:
        """Create hypothesis testing scenarios."""
        return [
            # Basic hypothesis formation
            ScenarioTemplate(
                title_template="Hypothesis Formation",
                description_template="Developing testable hypotheses from observations",
                prompt_template="Observation: {observation}. What testable hypothesis would explain this? What would be the null hypothesis? How would you test it?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "observation": [
                        "Plants near the window grow faster than those in the corner",
                        "Students who take notes by hand score better on tests",
                        "Crime rates are higher in areas with more street lights"
                    ]
                },
                expected_patterns={
                    "hypothesis": 0.8,
                    "testable": 0.7,
                    "null": 0.6,
                    "variables": 0.6,
                    "experiment": 0.7
                },
                tags=["hypothesis", "scientific_method", "testable", "null_hypothesis"]
            ),
            
            # Evaluating evidence
            ScenarioTemplate(
                title_template="Evidence Evaluation",
                description_template="Assessing strength of scientific evidence",
                prompt_template="Study claims: '{claim}' based on {study_design} with {sample}. Limitations include {limitations}. How strong is this evidence? What additional studies needed?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "claim": [
                        "Coffee reduces heart disease risk by 20%",
                        "Video games improve reaction times",
                        "Meditation changes brain structure"
                    ],
                    "study_design": [
                        "observational study over 10 years",
                        "randomized controlled trial for 3 months",
                        "brain imaging of 50 participants"
                    ],
                    "sample": [
                        "100,000 adults",
                        "200 teenagers",
                        "experienced meditators only"
                    ],
                    "limitations": [
                        "self-reported data",
                        "short duration",
                        "no control group"
                    ]
                },
                expected_patterns={
                    "limitations": 0.8,
                    "strength": 0.6,
                    "replication": 0.5,
                    "generalizability": 0.6,
                    "control": 0.6
                },
                tags=["evidence", "study_design", "limitations", "scientific_rigor"]
            ),
            
            # Falsifiability
            ScenarioTemplate(
                title_template="Falsifiability Assessment",
                description_template="Determining if claims are scientifically testable",
                prompt_template="Claim: '{claim}'. Is this claim falsifiable? If yes, what observation would disprove it? If no, why is it not scientific?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "claim": [
                        "All swans are white",
                        "Positive thinking always improves outcomes",
                        "There's an invisible dragon in my garage",
                        "Exercise improves mood",
                        "The universe was created last Thursday"
                    ]
                },
                expected_patterns={
                    "falsifiable": 0.7,
                    "observation": 0.6,
                    "testable": 0.7,
                    "scientific": 0.6,
                    "unfalsifiable": 0.5
                },
                tags=["falsifiability", "scientific_method", "testability", "philosophy_of_science"]
            ),
            
            # Statistical significance
            ScenarioTemplate(
                title_template="Statistical Significance Interpretation",
                description_template="Understanding statistical results and significance",
                prompt_template="Study results: {outcome} with p={p_value}, effect size={effect_size}, sample size={n}. {additional_info}. What can we conclude? What can't we conclude?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "outcome": [
                        "Drug A outperformed placebo",
                        "Teaching method B improved scores",
                        "Diet C reduced weight"
                    ],
                    "p_value": ["0.04", "0.001", "0.06"],
                    "effect_size": ["small (d=0.2)", "large (d=0.8)", "medium (d=0.5)"],
                    "n": ["30", "500", "1000"],
                    "additional_info": [
                        "Multiple comparisons were made",
                        "This replicates earlier findings",
                        "Industry-funded study"
                    ]
                },
                expected_patterns={
                    "significance": 0.7,
                    "effect size": 0.6,
                    "practical": 0.5,
                    "limitations": 0.6,
                    "cannot conclude causation": 0.5
                },
                tags=["statistics", "p_value", "significance", "interpretation"]
            ),
            
            # Replication crisis
            ScenarioTemplate(
                title_template="Replication and Reliability",
                description_template="Evaluating replication in science",
                prompt_template="Original study found {original_finding}. Replication attempts: {replication_results}. What does this mean for the finding? How should science proceed?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "original_finding": [
                        "power posing increases confidence hormones",
                        "priming with money makes people more selfish",
                        "ego depletion reduces willpower"
                    ],
                    "replication_results": [
                        "3 studies found no effect, 1 found smaller effect",
                        "Mixed results across 5 labs",
                        "Failed to replicate with larger sample"
                    ]
                },
                expected_patterns={
                    "replication": 0.8,
                    "reliability": 0.6,
                    "methodology": 0.5,
                    "update beliefs": 0.6,
                    "meta-analysis": 0.4
                },
                tags=["replication", "reliability", "scientific_process", "updating"]
            ),
            
            # Mechanism vs correlation
            ScenarioTemplate(
                title_template="Mechanism Identification",
                description_template="Distinguishing mechanism from correlation",
                prompt_template="Observation: {correlation}. Proposed mechanism: {mechanism}. What experiments would test if this mechanism is correct vs just correlation?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "correlation": [
                        "Exercise correlates with better mental health",
                        "Reading to children correlates with academic success",
                        "Social media use correlates with depression"
                    ],
                    "mechanism": [
                        "Endorphins from exercise improve mood",
                        "Language exposure builds neural pathways",
                        "Social comparison causes negative feelings"
                    ]
                },
                expected_patterns={
                    "mechanism": 0.7,
                    "experiment": 0.7,
                    "control": 0.6,
                    "alternative": 0.5,
                    "mediation": 0.4
                },
                tags=["mechanism", "causation", "experimentation", "theory"]
            ),
            
            # Paradigm shifts
            ScenarioTemplate(
                title_template="Scientific Paradigm Evaluation",
                description_template="Recognizing when theories need updating",
                prompt_template="Current theory: {current_theory}. New observations: {contradicting_observations}. Some scientists propose {new_theory}. How evaluate competing paradigms?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "current_theory": [
                        "Stress always weakens immune system",
                        "Genes determine behavior",
                        "Rational choice drives decisions"
                    ],
                    "contradicting_observations": [
                        "Some stress enhances immunity",
                        "Environmental factors change gene expression",
                        "Predictable irrationality in choices"
                    ],
                    "new_theory": [
                        "Hormesis model of stress",
                        "Epigenetic regulation",
                        "Behavioral economics framework"
                    ]
                },
                expected_patterns={
                    "evidence": 0.7,
                    "explanatory power": 0.6,
                    "predictions": 0.6,
                    "parsimony": 0.4,
                    "paradigm": 0.5
                },
                tags=["paradigm_shift", "theory_change", "scientific_revolution", "evidence"]
            ),
            
            # Meta-analysis interpretation
            ScenarioTemplate(
                title_template="Meta-Analysis Evaluation",
                description_template="Synthesizing multiple studies",
                prompt_template="Meta-analysis of {n_studies} studies on {topic} shows {overall_effect}. However, {heterogeneity}. Publication bias {pub_bias}. What conclusions are warranted?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "n_studies": ["23", "47", "112"],
                    "topic": [
                        "antidepressant effectiveness",
                        "educational intervention",
                        "dietary supplement benefits"
                    ],
                    "overall_effect": [
                        "small positive effect",
                        "moderate effect",
                        "no significant effect"
                    ],
                    "heterogeneity": [
                        "high variability between studies",
                        "consistent across studies",
                        "depends on population"
                    ],
                    "pub_bias": [
                        "likely present",
                        "minimal",
                        "cannot be assessed"
                    ]
                },
                expected_patterns={
                    "heterogeneity": 0.6,
                    "publication bias": 0.6,
                    "overall effect": 0.7,
                    "moderators": 0.5,
                    "quality": 0.5
                },
                tags=["meta_analysis", "synthesis", "publication_bias", "heterogeneity"]
            )
        ]
    
    def _create_correlation_causation_templates(self) -> List[ScenarioTemplate]:
        """Create correlation vs causation scenarios."""
        return [
            # Classic correlation confusion
            ScenarioTemplate(
                title_template="Correlation-Causation Distinction",
                description_template="Identifying when correlation doesn't imply causation",
                prompt_template="Data shows: {variable_a} strongly correlates with {variable_b} (r={correlation}). Media reports: '{causal_claim}'. What alternative explanations exist? How test causation?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "variable_a": [
                        "Ice cream sales",
                        "Number of firefighters at scene",
                        "Student laptop use in class"
                    ],
                    "variable_b": [
                        "drowning incidents",
                        "fire damage",
                        "lower grades"
                    ],
                    "correlation": ["0.85", "0.92", "0.73"],
                    "causal_claim": [
                        "Ice cream causes drowning",
                        "Firefighters cause damage",
                        "Laptops harm learning"
                    ]
                },
                expected_patterns={
                    "third variable": 0.8,
                    "correlation not causation": 0.8,
                    "confound": 0.6,
                    "experiment": 0.6,
                    "alternative": 0.7
                },
                tags=["correlation", "causation", "confounds", "media_interpretation"]
            ),
            
            # Bidirectional causation
            ScenarioTemplate(
                title_template="Bidirectional Relationships",
                description_template="Recognizing two-way causal relationships",
                prompt_template="Research shows {factor_a} associates with {factor_b}. Theory A: {a_causes_b}. Theory B: {b_causes_a}. Could both be true? How would you investigate?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "factor_a": [
                        "Depression",
                        "Poverty",
                        "Social isolation"
                    ],
                    "factor_b": [
                        "sleep problems",
                        "poor health",
                        "cognitive decline"
                    ],
                    "a_causes_b": [
                        "Depression disrupts sleep",
                        "Poverty limits healthcare access",
                        "Isolation reduces stimulation"
                    ],
                    "b_causes_a": [
                        "Poor sleep triggers depression",
                        "Illness causes financial strain",
                        "Cognitive decline reduces social ability"
                    ]
                },
                expected_patterns={
                    "bidirectional": 0.7,
                    "feedback loop": 0.5,
                    "longitudinal": 0.6,
                    "both": 0.7,
                    "temporal": 0.5
                },
                tags=["bidirectional", "feedback", "complex_causation", "investigation"]
            ),
            
            # Mediators and moderators
            ScenarioTemplate(
                title_template="Mediation and Moderation",
                description_template="Understanding indirect effects and conditions",
                prompt_template="{intervention} improves {outcome}, but only for {subgroup} and seems to work through {mediator}. Design study to test if {mediator} explains the effect.",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "intervention": [
                        "Exercise program",
                        "Mindfulness training",
                        "Tutoring"
                    ],
                    "outcome": [
                        "cognitive function",
                        "work performance",
                        "test scores"
                    ],
                    "subgroup": [
                        "older adults",
                        "high-stress individuals",
                        "struggling students"
                    ],
                    "mediator": [
                        "improved cardiovascular health",
                        "reduced anxiety",
                        "increased confidence"
                    ]
                },
                expected_patterns={
                    "mediation": 0.7,
                    "moderation": 0.6,
                    "mechanism": 0.6,
                    "pathway": 0.5,
                    "statistical test": 0.4
                },
                tags=["mediation", "moderation", "mechanisms", "subgroups"]
            ),
            
            # Spurious correlations
            ScenarioTemplate(
                title_template="Spurious Correlation Detection",
                description_template="Identifying meaningless correlations",
                prompt_template="Database analysis reveals: {variable_1} correlates with {variable_2} at r={correlation} (p<0.001) over {time_period}. Is this meaningful or spurious? How decide?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "variable_1": [
                        "Nicolas Cage movie releases",
                        "Cheese consumption",
                        "Number of sociology PhDs"
                    ],
                    "variable_2": [
                        "swimming pool drownings",
                        "bedsheet strangulations",
                        "arcade revenue"
                    ],
                    "correlation": ["0.87", "0.92", "0.78"],
                    "time_period": ["10 years", "15 years", "20 years"]
                },
                expected_patterns={
                    "spurious": 0.8,
                    "coincidence": 0.7,
                    "no mechanism": 0.7,
                    "multiple testing": 0.5,
                    "meaningless": 0.7
                },
                tags=["spurious", "coincidence", "data_mining", "false_patterns"]
            ),
            
            # Natural experiments
            ScenarioTemplate(
                title_template="Natural Experiment Analysis",
                description_template="Using natural variation to infer causation",
                prompt_template="{natural_event} created natural experiment: {group_a} experienced {change} while similar {group_b} didn't. Outcome: {result}. What causal inference is justified?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "natural_event": [
                        "Factory closure",
                        "Policy change in one state",
                        "Natural disaster"
                    ],
                    "group_a": [
                        "workers laid off",
                        "state residents",
                        "affected region"
                    ],
                    "change": [
                        "job loss",
                        "new education requirements",
                        "infrastructure damage"
                    ],
                    "group_b": [
                        "workers in similar factories",
                        "neighboring state residents",
                        "unaffected nearby region"
                    ],
                    "result": [
                        "health outcomes differed",
                        "test scores changed",
                        "economic patterns shifted"
                    ]
                },
                expected_patterns={
                    "natural experiment": 0.6,
                    "comparison": 0.7,
                    "causal": 0.6,
                    "limitations": 0.6,
                    "quasi-experimental": 0.4
                },
                tags=["natural_experiment", "quasi_experimental", "causal_inference", "comparison"]
            ),
            
            # Time series causation
            ScenarioTemplate(
                title_template="Temporal Causation Analysis",
                description_template="Using time patterns to understand causation",
                prompt_template="Time series shows: {event_a} consistently preceded {event_b} by {time_lag} across {instances}. {additional_pattern}. Does timing prove causation? What else needed?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "event_a": [
                        "Stock market decline",
                        "Social media trend",
                        "Weather pattern"
                    ],
                    "event_b": [
                        "unemployment rise",
                        "behavioral change",
                        "health outcomes"
                    ],
                    "time_lag": [
                        "3 months",
                        "2 weeks",
                        "1 year"
                    ],
                    "instances": [
                        "5 recessions",
                        "12 viral trends",
                        "20 years data"
                    ],
                    "additional_pattern": [
                        "Magnitude correlates",
                        "Effect size varies",
                        "Pattern weakening over time"
                    ]
                },
                expected_patterns={
                    "temporal precedence": 0.7,
                    "necessary not sufficient": 0.6,
                    "mechanism": 0.6,
                    "third variable": 0.5,
                    "granger": 0.3
                },
                tags=["time_series", "temporal", "precedence", "causation"]
            )
        ]
    
    def _create_experimental_design_templates(self) -> List[ScenarioTemplate]:
        """Create experimental design scenarios."""
        return [
            # Control group design
            ScenarioTemplate(
                title_template="Control Group Selection",
                description_template="Designing appropriate control conditions",
                prompt_template="Testing if {intervention} improves {outcome}. Proposed control: {control_option}. What confounds might this miss? What's ideal control?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "intervention": [
                        "new teaching method",
                        "meditation app",
                        "exercise program"
                    ],
                    "outcome": [
                        "student engagement",
                        "stress reduction",
                        "cognitive function"
                    ],
                    "control_option": [
                        "no intervention",
                        "waitlist control",
                        "usual care"
                    ]
                },
                expected_patterns={
                    "placebo": 0.6,
                    "active control": 0.5,
                    "expectations": 0.5,
                    "confounds": 0.7,
                    "blinding": 0.4
                },
                tags=["control_group", "experimental_design", "confounds", "placebo"]
            ),
            
            # Randomization importance
            ScenarioTemplate(
                title_template="Randomization and Assignment",
                description_template="Understanding randomization in experiments",
                prompt_template="Study assigns participants to {treatment} vs control by {assignment_method}. This creates {problem}. How does proper randomization solve this? What if randomization impossible?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "treatment": [
                        "therapy type",
                        "educational program",
                        "diet plan"
                    ],
                    "assignment_method": [
                        "patient choice",
                        "doctor recommendation",
                        "convenience"
                    ],
                    "problem": [
                        "selection bias",
                        "confounding by severity",
                        "motivation differences"
                    ]
                },
                expected_patterns={
                    "randomization": 0.8,
                    "bias": 0.7,
                    "confounding": 0.6,
                    "balance": 0.5,
                    "quasi-experimental": 0.4
                },
                tags=["randomization", "selection_bias", "assignment", "RCT"]
            ),
            
            # Sample size and power
            ScenarioTemplate(
                title_template="Sample Size Determination",
                description_template="Planning adequate sample sizes",
                prompt_template="Want to detect {effect_size} effect of {intervention} on {outcome} with 80% power. Pilot suggests high/low variability: {variability}. What influences needed sample size?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "effect_size": [
                        "small",
                        "medium",
                        "large"
                    ],
                    "intervention": [
                        "training program",
                        "medication",
                        "policy change"
                    ],
                    "outcome": [
                        "performance scores",
                        "symptom reduction",
                        "behavior change"
                    ],
                    "variability": [
                        "high between-person differences",
                        "measurement error",
                        "clustered data"
                    ]
                },
                expected_patterns={
                    "power": 0.7,
                    "effect size": 0.8,
                    "variability": 0.7,
                    "sample size": 0.8,
                    "calculation": 0.4
                },
                tags=["sample_size", "power_analysis", "planning", "statistics"]
            ),
            
            # Blinding and bias
            ScenarioTemplate(
                title_template="Blinding in Experiments",
                description_template="Preventing experimenter and subject bias",
                prompt_template="Study testing {intervention} where {obvious_difference}. Single-blind would {single_blind_limit}. Double-blind seems {double_blind_challenge}. How minimize bias?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "intervention": [
                        "psychotherapy vs medication",
                        "surgery vs physical therapy",
                        "online vs in-person teaching"
                    ],
                    "obvious_difference": [
                        "participants know if talking to therapist",
                        "surgery has visible incisions",
                        "delivery mode is apparent"
                    ],
                    "single_blind_limit": [
                        "still allow therapist bias",
                        "surgeon knows procedure",
                        "teacher knows format"
                    ],
                    "double_blind_challenge": [
                        "impossible",
                        "unethical",
                        "impractical"
                    ]
                },
                expected_patterns={
                    "blinding": 0.7,
                    "bias": 0.8,
                    "alternatives": 0.5,
                    "outcome assessor": 0.5,
                    "expectations": 0.6
                },
                tags=["blinding", "bias_prevention", "double_blind", "methodology"]
            ),
            
            # External validity
            ScenarioTemplate(
                title_template="Generalizability and External Validity",
                description_template="Designing studies that generalize",
                prompt_template="Lab study finds {finding} using {sample} in {setting}. Want findings to apply to {target_population} in {real_setting}. What threatens generalizability? How improve?",
                domain=CognitiveDomain.CAUSAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "finding": [
                        "memory technique improves recall 40%",
                        "incentive increases productivity",
                        "intervention reduces aggression"
                    ],
                    "sample": [
                        "college students",
                        "volunteers",
                        "WEIRD population"
                    ],
                    "setting": [
                        "controlled lab",
                        "artificial tasks",
                        "short duration"
                    ],
                    "target_population": [
                        "elderly adults",
                        "actual employees",
                        "diverse communities"
                    ],
                    "real_setting": [
                        "daily life",
                        "workplace",
                        "natural environment"
                    ]
                },
                expected_patterns={
                    "external validity": 0.7,
                    "generalizability": 0.8,
                    "ecological": 0.5,
                    "sample diversity": 0.6,
                    "field study": 0.5
                },
                tags=["external_validity", "generalizability", "ecological_validity", "WEIRD"]
            )
        ]