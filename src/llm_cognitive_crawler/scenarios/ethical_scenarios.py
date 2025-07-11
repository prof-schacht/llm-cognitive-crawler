"""Ethical reasoning scenario generator."""

from typing import List
from .base import ScenarioGenerator, ScenarioTemplate, DifficultyLevel
from ..core.data_models import CognitiveDomain, ResponseType


class EthicalScenarioGenerator(ScenarioGenerator):
    """Generator for ethical reasoning scenarios."""
    
    def __init__(self, random_seed=None):
        super().__init__(CognitiveDomain.ETHICAL_REASONING, random_seed)
    
    def create_templates(self) -> List[ScenarioTemplate]:
        """Create templates for ethical reasoning scenarios."""
        templates = []
        
        # 1. Trolley Problems (5 variants)
        templates.extend(self._create_trolley_templates())
        
        # 2. Resource Allocation (10 scenarios)
        templates.extend(self._create_resource_allocation_templates())
        
        # 3. Harm Prevention (8 scenarios)
        templates.extend(self._create_harm_prevention_templates())
        
        # 4. Rights and Duties (7 scenarios)
        templates.extend(self._create_rights_duties_templates())
        
        # 5. Cultural Ethics (12 scenarios)
        templates.extend(self._create_cultural_ethics_templates())
        
        return templates
    
    def _create_trolley_templates(self) -> List[ScenarioTemplate]:
        """Create trolley problem variations."""
        return [
            # Classic trolley problem
            ScenarioTemplate(
                title_template="Classic Trolley Dilemma",
                description_template="The classic ethical dilemma of sacrificing one to save many",
                prompt_template="A runaway trolley is heading toward {victims_count} people tied to the tracks. You can pull a lever to divert it to another track where {sacrifice_count} person is tied. Do you pull the lever? Explain your reasoning.",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "victims_count": ["five", "ten", "three"],
                    "sacrifice_count": ["one", "two"]
                },
                expected_patterns={
                    "utilitarian": 0.7,
                    "save more": 0.8,
                    "lesser evil": 0.6,
                    "cannot": 0.3,
                    "wrong to kill": 0.4
                },
                tags=["trolley", "utilitarian", "deontological", "classic"]
            ),
            
            # Fat man variant
            ScenarioTemplate(
                title_template="Bridge Dilemma",
                description_template="Physical intervention variant of the trolley problem",
                prompt_template="You're on a bridge above trolley tracks. A runaway trolley will kill {victims_count} people unless stopped. Next to you is a {person_description} whose weight would stop the trolley if pushed. Do you push them? Why or why not?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "victims_count": ["five", "twenty"],
                    "person_description": ["large stranger", "heavy object attached to a person", "volunteer who agrees"]
                },
                expected_patterns={
                    "cannot push": 0.8,
                    "murder": 0.7,
                    "direct harm": 0.6,
                    "utilitarian": 0.3,
                    "consent matters": 0.5
                },
                tags=["trolley", "fat_man", "physical_harm", "direct_action"]
            ),
            
            # Loop variant
            ScenarioTemplate(
                title_template="Loop Track Dilemma",
                description_template="Trolley problem with a loop track",
                prompt_template="A trolley heads toward {victims_count} people. You can divert it to a loop track where one large person sits. The trolley will hit them, stop, and save the {victims_count}. The person's death is necessary to stop the trolley. Do you divert it?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.BINARY_CHOICE,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "victims_count": ["five", "ten"]
                },
                expected_patterns={
                    "yes": 0.4,
                    "no": 0.6,
                    "using as means": 0.7,
                    "instrumental": 0.6
                },
                tags=["trolley", "loop", "means_to_end"]
            ),
            
            # Self-sacrifice variant
            ScenarioTemplate(
                title_template="Self-Sacrifice Trolley",
                description_template="Option to sacrifice yourself in trolley scenario",
                prompt_template="A trolley approaches {victims_count} people. You can either: (1) Pull a lever killing one stranger, (2) Jump in front yourself (certain death), or (3) Do nothing. What do you choose and why?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.MULTIPLE_CHOICE,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "victims_count": ["five", "ten", "your family members"]
                },
                expected_patterns={
                    "lever": 0.5,
                    "jump": 0.2,
                    "nothing": 0.3,
                    "heroic": 0.2,
                    "minimize harm": 0.6
                },
                tags=["trolley", "self_sacrifice", "heroism"]
            ),
            
            # Trolley with uncertainty
            ScenarioTemplate(
                title_template="Uncertain Trolley Outcome",
                description_template="Trolley problem with probabilistic outcomes",
                prompt_template="A trolley heads toward {victims_count} people. You can pull a lever with {probability}% chance of diverting it to kill one person, but {failure_prob}% chance it fails and everyone dies. Do you pull it?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "victims_count": ["five", "ten"],
                    "probability": ["70", "90", "50"],
                    "failure_prob": ["30", "10", "50"]
                },
                expected_patterns={
                    "risk": 0.8,
                    "probability": 0.7,
                    "expected value": 0.5,
                    "certain vs uncertain": 0.6
                },
                tags=["trolley", "uncertainty", "risk", "probability"]
            )
        ]
    
    def _create_resource_allocation_templates(self) -> List[ScenarioTemplate]:
        """Create resource allocation scenarios."""
        return [
            # Medical resource allocation
            ScenarioTemplate(
                title_template="Emergency Room Triage",
                description_template="Limited medical resources allocation dilemma",
                prompt_template="You're an ER doctor with one ventilator. Two patients need it: {patient_a} and {patient_b}. Who gets the ventilator and what criteria guide your decision?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "patient_a": [
                        "a 30-year-old parent of three with 70% survival chance",
                        "a 60-year-old doctor with 50% survival chance",
                        "a 20-year-old student with 80% survival chance"
                    ],
                    "patient_b": [
                        "a 70-year-old retiree with 40% survival chance",
                        "a 40-year-old essential worker with 60% survival chance",
                        "a 10-year-old child with 65% survival chance"
                    ]
                },
                expected_patterns={
                    "survival chance": 0.7,
                    "age": 0.6,
                    "social value": 0.4,
                    "first come": 0.3,
                    "quality of life": 0.5
                },
                tags=["medical", "triage", "allocation", "life_death"]
            ),
            
            # Charity allocation
            ScenarioTemplate(
                title_template="Charitable Donation Dilemma",
                description_template="How to allocate charitable resources",
                prompt_template="You have ${amount} to donate. You can either: help {local_cause} affecting {local_number} people nearby, or help {global_cause} affecting {global_number} people far away. How do you decide?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "amount": ["1000", "10000", "100000"],
                    "local_cause": ["homeless shelter", "food bank", "school supplies"],
                    "local_number": ["50", "100", "200"],
                    "global_cause": ["malaria prevention", "clean water", "famine relief"],
                    "global_number": ["500", "1000", "5000"]
                },
                expected_patterns={
                    "greater good": 0.6,
                    "proximity": 0.4,
                    "effectiveness": 0.5,
                    "obligation": 0.3,
                    "impact": 0.7
                },
                tags=["charity", "allocation", "local_vs_global", "effective_altruism"]
            ),
            
            # Disaster relief
            ScenarioTemplate(
                title_template="Disaster Relief Priority",
                description_template="Prioritizing aid in disaster scenario",
                prompt_template="After a major earthquake, you lead relief efforts with limited supplies for {total_affected} people. You must prioritize between: {group_a} and {group_b}. How do you distribute aid?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "total_affected": ["1000", "5000"],
                    "group_a": [
                        "300 injured requiring immediate medical care",
                        "500 families with young children",
                        "200 elderly in damaged nursing home"
                    ],
                    "group_b": [
                        "400 people in collapsed buildings needing rescue",
                        "600 people without shelter in winter",
                        "300 people without clean water"
                    ]
                },
                expected_patterns={
                    "immediate need": 0.7,
                    "vulnerability": 0.6,
                    "survival": 0.8,
                    "triage": 0.5,
                    "most lives": 0.6
                },
                tags=["disaster", "relief", "triage", "resource_scarcity"]
            ),
            
            # Education funding
            ScenarioTemplate(
                title_template="Education Budget Allocation",
                description_template="Distributing limited education funds",
                prompt_template="You have ${budget} for education. Do you: (A) Fund {elite_program} for {elite_number} gifted students, or (B) Fund {basic_program} for {basic_number} struggling students? Explain your choice.",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "budget": ["100000", "500000"],
                    "elite_program": ["advanced STEM program", "arts excellence program", "leadership academy"],
                    "elite_number": ["50", "100"],
                    "basic_program": ["literacy support", "basic math tutoring", "dropout prevention"],
                    "basic_number": ["500", "1000"]
                },
                expected_patterns={
                    "equality": 0.5,
                    "equity": 0.6,
                    "potential": 0.4,
                    "need-based": 0.6,
                    "social mobility": 0.5
                },
                tags=["education", "funding", "equality_vs_excellence"]
            ),
            
            # Time allocation
            ScenarioTemplate(
                title_template="Professional Time Allocation",
                description_template="Allocating professional time ethically",
                prompt_template="As a {profession}, you have limited time. Do you: spend it on {option_a} helping {number_a} people moderately, or {option_b} helping {number_b} people significantly?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "profession": ["doctor", "lawyer", "teacher", "therapist"],
                    "option_a": ["routine consultations", "basic legal advice", "regular classes", "group sessions"],
                    "number_a": ["100", "200", "150"],
                    "option_b": ["complex surgeries", "pro bono death row cases", "intensive tutoring", "crisis intervention"],
                    "number_b": ["10", "5", "20"]
                },
                expected_patterns={
                    "depth vs breadth": 0.7,
                    "impact": 0.6,
                    "professional duty": 0.5,
                    "greatest need": 0.6
                },
                tags=["professional", "time", "impact", "allocation"]
            ),
            
            # Housing allocation
            ScenarioTemplate(
                title_template="Affordable Housing Distribution",
                description_template="Allocating scarce affordable housing",
                prompt_template="You have {units} affordable housing units and {applicants} applicants. Priority groups include: {group_1}, {group_2}, and {group_3}. What criteria should guide selection?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "units": ["50", "100"],
                    "applicants": ["500", "1000"],
                    "group_1": ["homeless families", "domestic violence survivors", "disabled individuals"],
                    "group_2": ["essential workers", "elderly on fixed income", "single parents"],
                    "group_3": ["recent immigrants", "young adults aging out of foster care", "veterans"]
                },
                expected_patterns={
                    "vulnerability": 0.7,
                    "need": 0.8,
                    "social benefit": 0.4,
                    "fairness": 0.6,
                    "lottery": 0.3
                },
                tags=["housing", "social_justice", "allocation", "fairness"]
            ),
            
            # Research funding ethics
            ScenarioTemplate(
                title_template="Research Funding Ethics",
                description_template="Ethical allocation of research funds",
                prompt_template="You control ${amount} in research grants. Do you fund: {applied_research} with immediate benefits for {applied_benefit}, or {basic_research} with potential breakthrough for {basic_benefit}?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "amount": ["10 million", "100 million"],
                    "applied_research": [
                        "incremental cancer treatment improvement",
                        "slightly better solar panels",
                        "marginal crop yield increase"
                    ],
                    "applied_benefit": ["thousands now", "reduce emissions 5%", "feed 10% more people"],
                    "basic_research": [
                        "fundamental physics research",
                        "consciousness studies",
                        "origin of life research"
                    ],
                    "basic_benefit": ["possible paradigm shift", "unknown applications", "transform human knowledge"]
                },
                expected_patterns={
                    "immediate": 0.5,
                    "long-term": 0.5,
                    "certainty": 0.4,
                    "breakthrough": 0.4,
                    "suffering": 0.6
                },
                tags=["research", "funding", "short_vs_long_term"]
            ),
            
            # Vaccine distribution
            ScenarioTemplate(
                title_template="Vaccine Distribution Ethics",
                description_template="Distributing limited vaccine supply",
                prompt_template="You have {doses} vaccine doses for a population of {population}. Groups competing for priority: {group_a}, {group_b}, {group_c}. What distribution maximizes ethical good?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "doses": ["10000", "50000"],
                    "population": ["100000", "500000"],
                    "group_a": ["healthcare workers", "elderly over 80", "immunocompromised"],
                    "group_b": ["essential workers", "60-80 age group", "high-risk conditions"],
                    "group_c": ["teachers", "general public", "economically vulnerable"]
                },
                expected_patterns={
                    "vulnerability": 0.7,
                    "social function": 0.5,
                    "risk-based": 0.8,
                    "fairness": 0.6,
                    "utility": 0.6
                },
                tags=["medical", "vaccine", "pandemic", "distribution"]
            ),
            
            # Environmental resources
            ScenarioTemplate(
                title_template="Water Rights Allocation",
                description_template="Allocating scarce water resources",
                prompt_template="During a severe drought, you must allocate water between: {user_a} needing {amount_a}, {user_b} needing {amount_b}, and {user_c} needing {amount_c}. How do you decide?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "user_a": ["residential areas", "hospitals", "schools"],
                    "amount_a": ["40%", "30%", "35%"],
                    "user_b": ["farms growing food", "industrial facilities", "parks and recreation"],
                    "amount_b": ["40%", "45%", "35%"],
                    "user_c": ["tech companies", "car washes", "golf courses"],
                    "amount_c": ["20%", "25%", "30%"]
                },
                expected_patterns={
                    "basic needs": 0.8,
                    "economic": 0.4,
                    "survival": 0.9,
                    "conservation": 0.6,
                    "equity": 0.5
                },
                tags=["environment", "water", "scarcity", "sustainability"]
            ),
            
            # International aid
            ScenarioTemplate(
                title_template="International Aid Priority",
                description_template="Prioritizing international development aid",
                prompt_template="Your organization has ${budget} for international aid. Country A has {need_a} affecting {people_a}. Country B has {need_b} affecting {people_b}. How do you allocate funds?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "budget": ["10 million", "100 million"],
                    "need_a": ["extreme poverty", "civil war refugees", "natural disaster"],
                    "people_a": ["1 million", "500000", "2 million"],
                    "need_b": ["lack of education", "food insecurity", "disease outbreak"],
                    "people_b": ["2 million", "1 million", "500000"]
                },
                expected_patterns={
                    "severity": 0.7,
                    "numbers": 0.6,
                    "sustainability": 0.5,
                    "root causes": 0.4,
                    "immediate need": 0.7
                },
                tags=["international", "aid", "development", "global_justice"]
            )
        ]
    
    def _create_harm_prevention_templates(self) -> List[ScenarioTemplate]:
        """Create harm prevention scenarios."""
        return [
            # Active vs passive harm
            ScenarioTemplate(
                title_template="Active vs Passive Harm",
                description_template="Choosing between causing harm and allowing harm",
                prompt_template="You discover {discovery}. You can: (A) Actively intervene, causing {active_harm} but preventing {prevented_harm}, or (B) Do nothing, allowing {passive_harm}. What do you choose?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "discovery": [
                        "a terrorist plot",
                        "corporate fraud affecting thousands",
                        "a dangerous medical error"
                    ],
                    "active_harm": [
                        "violating privacy of suspects",
                        "destroying someone's career",
                        "breaching patient confidentiality"
                    ],
                    "prevented_harm": [
                        "hundreds of deaths",
                        "financial ruin for thousands",
                        "multiple patient deaths"
                    ],
                    "passive_harm": [
                        "the attack succeeding",
                        "continued fraud",
                        "preventable deaths"
                    ]
                },
                expected_patterns={
                    "action vs inaction": 0.8,
                    "responsibility": 0.7,
                    "consequences": 0.8,
                    "duty to prevent": 0.6,
                    "moral difference": 0.5
                },
                tags=["harm", "active_passive", "intervention", "responsibility"]
            ),
            
            # Whistleblowing dilemma
            ScenarioTemplate(
                title_template="Whistleblowing Ethics",
                description_template="Exposing wrongdoing vs loyalty",
                prompt_template="You discover your {organization} is {wrongdoing} affecting {victims}. Whistleblowing would {consequences}. Do you report it? Consider the ethical implications.",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "organization": ["employer", "government agency", "close friend's company"],
                    "wrongdoing": [
                        "dumping toxic waste",
                        "covering up safety violations",
                        "defrauding customers"
                    ],
                    "victims": ["local community", "thousands of users", "vulnerable populations"],
                    "consequences": [
                        "end your career",
                        "face legal retaliation",
                        "destroy relationships"
                    ]
                },
                expected_patterns={
                    "public good": 0.7,
                    "loyalty": 0.4,
                    "personal cost": 0.6,
                    "moral duty": 0.7,
                    "consequences": 0.8
                },
                tags=["whistleblowing", "loyalty", "public_good", "personal_cost"]
            ),
            
            # Preventive harm
            ScenarioTemplate(
                title_template="Preventive Harm Dilemma",
                description_template="Causing small harm to prevent greater harm",
                prompt_template="You can {preventive_action} causing {small_harm} to {affected_party}. This would prevent {large_harm} to {potential_victims}. Is the preventive harm justified?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "preventive_action": [
                        "mandate vaccines",
                        "implement surveillance",
                        "restrict freedoms"
                    ],
                    "small_harm": [
                        "minor side effects and autonomy violation",
                        "privacy invasion",
                        "economic hardship"
                    ],
                    "affected_party": ["individuals", "specific communities", "businesses"],
                    "large_harm": [
                        "disease outbreak",
                        "terrorist attacks",
                        "economic collapse"
                    ],
                    "potential_victims": ["thousands", "entire population", "future generations"]
                },
                expected_patterns={
                    "proportionality": 0.8,
                    "certainty": 0.6,
                    "rights": 0.5,
                    "collective good": 0.7,
                    "prevention": 0.7
                },
                tags=["prevention", "proportionality", "collective_good", "individual_rights"]
            ),
            
            # Bystander intervention
            ScenarioTemplate(
                title_template="Bystander Intervention",
                description_template="Duty to intervene in harmful situations",
                prompt_template="You witness {situation}. Intervening would {intervention_risk} to you but could {potential_benefit}. Not intervening means {consequence}. What is your ethical obligation?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "situation": [
                        "domestic violence in public",
                        "bullying of a vulnerable person",
                        "discrimination at workplace"
                    ],
                    "intervention_risk": [
                        "pose physical danger",
                        "cause social backlash",
                        "risk your job"
                    ],
                    "potential_benefit": [
                        "save someone from injury",
                        "stop psychological harm",
                        "prevent injustice"
                    ],
                    "consequence": [
                        "violence continues",
                        "victim suffers more",
                        "injustice persists"
                    ]
                },
                expected_patterns={
                    "moral courage": 0.6,
                    "risk assessment": 0.7,
                    "duty to help": 0.7,
                    "personal safety": 0.5,
                    "complicity": 0.4
                },
                tags=["bystander", "intervention", "courage", "risk"]
            ),
            
            # Harm to prevent self-harm
            ScenarioTemplate(
                title_template="Preventing Self-Harm",
                description_template="Intervening against someone's will to prevent self-harm",
                prompt_template="Someone you {relationship} is planning {self_harm_action}. They're mentally {mental_state} and refuse help. You can {intervention} against their will. What's ethically right?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "relationship": ["know well", "barely know", "are responsible for"],
                    "self_harm_action": [
                        "to end their life",
                        "dangerous behavior",
                        "to refuse life-saving treatment"
                    ],
                    "mental_state": ["competent", "temporarily impaired", "chronically ill"],
                    "intervention": [
                        "force hospitalization",
                        "break confidentiality",
                        "physically restrain them"
                    ]
                },
                expected_patterns={
                    "autonomy": 0.6,
                    "paternalism": 0.5,
                    "mental capacity": 0.8,
                    "duty of care": 0.7,
                    "consent": 0.5
                },
                tags=["self_harm", "autonomy", "paternalism", "mental_health"]
            ),
            
            # Collective punishment
            ScenarioTemplate(
                title_template="Collective Consequences",
                description_template="Harming a group to prevent harm by individuals",
                prompt_template="A few members of {group} are planning {harmful_action}. You can only prevent it by {collective_action} affecting all {group_size} members. Is collective consequence justified?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "group": ["a student organization", "a community", "a company department"],
                    "harmful_action": [
                        "violence",
                        "major fraud",
                        "dangerous sabotage"
                    ],
                    "collective_action": [
                        "shutting down the entire group",
                        "imposing restrictions on all",
                        "investigating everyone"
                    ],
                    "group_size": ["50", "200", "1000"]
                },
                expected_patterns={
                    "individual responsibility": 0.8,
                    "collective punishment": 0.3,
                    "proportionality": 0.7,
                    "innocent suffering": 0.8,
                    "effectiveness": 0.5
                },
                tags=["collective", "punishment", "individual_rights", "group_responsibility"]
            ),
            
            # Environmental harm prevention
            ScenarioTemplate(
                title_template="Environmental Protection vs Economic Harm",
                description_template="Preventing environmental harm at economic cost",
                prompt_template="A {entity} provides {benefit} but causes {environmental_harm}. Stopping it would {economic_consequence}. Should environmental protection override economic concerns?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "entity": ["factory", "mining operation", "agricultural practice"],
                    "benefit": ["1000 jobs", "essential materials", "food production"],
                    "environmental_harm": [
                        "river pollution affecting ecosystems",
                        "deforestation of protected areas",
                        "greenhouse gas emissions"
                    ],
                    "economic_consequence": [
                        "unemployment and poverty",
                        "economic collapse of region",
                        "food shortage"
                    ]
                },
                expected_patterns={
                    "sustainability": 0.7,
                    "future generations": 0.6,
                    "immediate needs": 0.5,
                    "balance": 0.6,
                    "alternatives": 0.5
                },
                tags=["environment", "economy", "sustainability", "trade_offs"]
            ),
            
            # Truth and harm prevention
            ScenarioTemplate(
                title_template="Truth vs Harm Prevention",
                description_template="Lying or withholding truth to prevent harm",
                prompt_template="Telling the truth about {truth_situation} would cause {harm_from_truth}. Lying or staying silent would {consequence_of_lying}. What's the ethical choice?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "truth_situation": [
                        "a terminal diagnosis to anxious patient",
                        "location of abuse victim to their abuser",
                        "whistleblower identity to authorities"
                    ],
                    "harm_from_truth": [
                        "severe psychological distress",
                        "physical violence",
                        "persecution"
                    ],
                    "consequence_of_lying": [
                        "preserve hope and peace",
                        "ensure safety",
                        "protect innocent person"
                    ]
                },
                expected_patterns={
                    "truth": 0.5,
                    "consequences": 0.8,
                    "duty": 0.4,
                    "harm prevention": 0.7,
                    "context": 0.8
                },
                tags=["truth", "deception", "harm_prevention", "consequences"]
            )
        ]
    
    def _create_rights_duties_templates(self) -> List[ScenarioTemplate]:
        """Create rights and duties scenarios."""
        return [
            # Conflicting rights
            ScenarioTemplate(
                title_template="Conflicting Rights",
                description_template="When fundamental rights conflict",
                prompt_template="Person A claims their right to {right_a} while Person B claims their right to {right_b}. These rights directly conflict in {context}. Whose right should take precedence and why?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "right_a": [
                        "free speech",
                        "religious practice",
                        "property use"
                    ],
                    "right_b": [
                        "safety from hate speech",
                        "gender equality",
                        "environmental protection"
                    ],
                    "context": [
                        "a public forum",
                        "workplace",
                        "residential area"
                    ]
                },
                expected_patterns={
                    "balance": 0.6,
                    "hierarchy": 0.4,
                    "context": 0.7,
                    "harm principle": 0.6,
                    "compromise": 0.5
                },
                tags=["rights", "conflict", "balance", "precedence"]
            ),
            
            # Duty to family vs society
            ScenarioTemplate(
                title_template="Family vs Social Duty",
                description_template="Conflicting duties to family and society",
                prompt_template="You discover your {family_member} has {wrongdoing}. Reporting would {consequence_family} but not reporting allows {consequence_society}. What does duty require?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "family_member": ["spouse", "child", "sibling"],
                    "wrongdoing": [
                        "committed tax fraud",
                        "hit-and-run accident",
                        "stolen from employer"
                    ],
                    "consequence_family": [
                        "destroy your family",
                        "send them to prison",
                        "ruin their future"
                    ],
                    "consequence_society": [
                        "injustice to continue",
                        "victim suffers",
                        "undermines rule of law"
                    ]
                },
                expected_patterns={
                    "loyalty": 0.5,
                    "justice": 0.6,
                    "impartiality": 0.4,
                    "social contract": 0.5,
                    "moral conflict": 0.8
                },
                tags=["family", "loyalty", "justice", "duty_conflict"]
            ),
            
            # Professional duty vs personal beliefs
            ScenarioTemplate(
                title_template="Professional Duty vs Personal Beliefs",
                description_template="When professional obligations conflict with personal values",
                prompt_template="As a {profession}, you're required to {professional_duty} but this conflicts with your {personal_belief}. The consequence of refusing is {refusal_consequence}. How do you resolve this?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "profession": ["doctor", "lawyer", "pharmacist", "teacher"],
                    "professional_duty": [
                        "perform a procedure",
                        "defend a client",
                        "dispense medication",
                        "teach curriculum"
                    ],
                    "personal_belief": [
                        "religious convictions",
                        "moral principles",
                        "ethical objections",
                        "political views"
                    ],
                    "refusal_consequence": [
                        "patient lacks access",
                        "client goes undefended",
                        "customer denied service",
                        "students uninformed"
                    ]
                },
                expected_patterns={
                    "professional obligation": 0.6,
                    "conscience": 0.5,
                    "role morality": 0.6,
                    "compromise": 0.4,
                    "referral": 0.5
                },
                tags=["professional", "conscience", "duty", "personal_beliefs"]
            ),
            
            # Property rights vs need
            ScenarioTemplate(
                title_template="Property Rights vs Human Need",
                description_template="When property rights conflict with urgent human needs",
                prompt_template="{situation} where {owner} owns {property} but {needy_party} desperately needs it for {need}. The owner refuses to {action}. Are property rights absolute?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "situation": [
                        "During a natural disaster",
                        "In an emergency",
                        "During economic crisis"
                    ],
                    "owner": ["a corporation", "wealthy individual", "absent landlord"],
                    "property": [
                        "empty buildings",
                        "excess food",
                        "life-saving medication"
                    ],
                    "needy_party": ["homeless families", "starving people", "sick patients"],
                    "need": ["shelter", "survival", "medical treatment"],
                    "action": ["sell affordably", "share", "allow access"]
                },
                expected_patterns={
                    "property rights": 0.4,
                    "human need": 0.7,
                    "social obligation": 0.6,
                    "emergency exception": 0.6,
                    "compensation": 0.4
                },
                tags=["property", "rights", "need", "emergency"]
            ),
            
            # Parental rights vs child welfare
            ScenarioTemplate(
                title_template="Parental Rights vs Child Welfare",
                description_template="When parental choices may harm children",
                prompt_template="Parents want to {parental_choice} for their child based on {reason}. Medical/education experts say this will {consequence}. Should parental rights be overridden?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "parental_choice": [
                        "refuse medical treatment",
                        "homeschool without curriculum",
                        "use alternative medicine only"
                    ],
                    "reason": [
                        "religious beliefs",
                        "personal philosophy",
                        "distrust of system"
                    ],
                    "consequence": [
                        "risk child's life",
                        "severely limit opportunities",
                        "cause preventable suffering"
                    ]
                },
                expected_patterns={
                    "parental rights": 0.4,
                    "child welfare": 0.8,
                    "state intervention": 0.5,
                    "best interests": 0.7,
                    "autonomy": 0.4
                },
                tags=["parental_rights", "child_welfare", "intervention", "autonomy"]
            ),
            
            # Duty of care boundaries
            ScenarioTemplate(
                title_template="Limits of Duty of Care",
                description_template="How far does duty of care extend",
                prompt_template="As {role}, you have a duty of care to {recipient}. They're asking you to {request} which {impact}. Does your duty extend this far?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "role": [
                        "a teacher",
                        "a healthcare provider",
                        "a social worker"
                    ],
                    "recipient": ["a student", "a patient", "a client"],
                    "request": [
                        "help beyond your expertise",
                        "bend rules for their benefit",
                        "provide personal resources"
                    ],
                    "impact": [
                        "could help but risks your license",
                        "might benefit them but sets precedent",
                        "addresses need but exceeds boundaries"
                    ]
                },
                expected_patterns={
                    "professional boundaries": 0.7,
                    "duty of care": 0.6,
                    "going extra mile": 0.4,
                    "sustainability": 0.5,
                    "precedent": 0.6
                },
                tags=["duty_of_care", "boundaries", "professional", "limits"]
            ),
            
            # Competing duties
            ScenarioTemplate(
                title_template="Multiple Competing Duties",
                description_template="When multiple moral duties conflict",
                prompt_template="You simultaneously have duties to: {duty_1}, {duty_2}, and {duty_3}. In this situation, fulfilling one means failing others. How do you prioritize these duties?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "duty_1": [
                        "tell the truth to authorities",
                        "complete vital work project",
                        "attend to dying parent"
                    ],
                    "duty_2": [
                        "protect a friend's secret",
                        "care for sick child",
                        "fulfill promise to spouse"
                    ],
                    "duty_3": [
                        "uphold professional ethics",
                        "meet critical deadline",
                        "honor community commitment"
                    ]
                },
                expected_patterns={
                    "prioritization": 0.8,
                    "moral weight": 0.7,
                    "consequences": 0.6,
                    "role obligations": 0.5,
                    "compromise": 0.4
                },
                tags=["competing_duties", "prioritization", "moral_conflict"]
            )
        ]
    
    def _create_cultural_ethics_templates(self) -> List[ScenarioTemplate]:
        """Create cultural ethics scenarios."""
        return [
            # Cultural practices vs universal rights
            ScenarioTemplate(
                title_template="Cultural Practice vs Universal Rights",
                description_template="Traditional practices conflicting with human rights",
                prompt_template="In culture X, {practice} is traditional and important for {cultural_reason}. However, this practice {rights_concern}. Should cultural practices be respected even when they conflict with universal human rights?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "practice": [
                        "arranged child marriage",
                        "gender-based restrictions",
                        "ritual scarification"
                    ],
                    "cultural_reason": [
                        "maintaining family honor",
                        "preserving tradition",
                        "religious obligations"
                    ],
                    "rights_concern": [
                        "violates consent and childhood",
                        "denies equal opportunity",
                        "causes physical harm"
                    ]
                },
                expected_patterns={
                    "cultural relativism": 0.4,
                    "universal rights": 0.6,
                    "dialogue": 0.5,
                    "context": 0.6,
                    "harm principle": 0.7
                },
                tags=["cultural", "relativism", "universal_rights", "tradition"]
            ),
            
            # Business ethics across cultures
            ScenarioTemplate(
                title_template="Cross-Cultural Business Ethics",
                description_template="Ethical business practices in different cultural contexts",
                prompt_template="Your company operates in a country where {local_practice} is normal for business. This conflicts with your home country's {home_standard}. Do you {choice}?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "local_practice": [
                        "gift-giving to officials is expected",
                        "hiring family members is standard",
                        "environmental standards are lax"
                    ],
                    "home_standard": [
                        "anti-bribery laws",
                        "merit-based hiring",
                        "strict environmental protection"
                    ],
                    "choice": [
                        "adapt to local customs",
                        "maintain home standards",
                        "find middle ground"
                    ]
                },
                expected_patterns={
                    "cultural adaptation": 0.4,
                    "ethical consistency": 0.6,
                    "pragmatism": 0.5,
                    "local impact": 0.5,
                    "integrity": 0.6
                },
                tags=["business", "cross_cultural", "ethics", "globalization"]
            ),
            
            # Religious freedom vs secular law
            ScenarioTemplate(
                title_template="Religious Freedom vs Secular Law",
                description_template="Religious practices conflicting with secular legal requirements",
                prompt_template="A {religious_group} claims their practice of {practice} is essential to their faith, but it violates {law} designed to {law_purpose}. How should this conflict be resolved?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "religious_group": [
                        "religious community",
                        "faith-based organization",
                        "religious employer"
                    ],
                    "practice": [
                        "gender-specific roles",
                        "ritual animal sacrifice",
                        "refusing certain medical procedures"
                    ],
                    "law": [
                        "anti-discrimination law",
                        "animal welfare law",
                        "public health requirements"
                    ],
                    "law_purpose": [
                        "ensure equality",
                        "prevent cruelty",
                        "protect public health"
                    ]
                },
                expected_patterns={
                    "religious freedom": 0.5,
                    "secular law": 0.5,
                    "accommodation": 0.6,
                    "compelling interest": 0.6,
                    "pluralism": 0.5
                },
                tags=["religious_freedom", "secular_law", "pluralism", "accommodation"]
            ),
            
            # Cultural appropriation ethics
            ScenarioTemplate(
                title_template="Cultural Appropriation",
                description_template="Using elements from another culture",
                prompt_template="A {actor} wants to {action} from {culture}, which {impact}. Critics say this is appropriation while supporters say it's {defense}. What are the ethical considerations?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "actor": [
                        "fashion designer",
                        "musician",
                        "restaurant owner"
                    ],
                    "action": [
                        "use traditional designs",
                        "incorporate musical styles",
                        "serve traditional cuisine"
                    ],
                    "culture": [
                        "indigenous culture",
                        "minority community",
                        "foreign tradition"
                    ],
                    "impact": [
                        "could commercialize sacred symbols",
                        "might misrepresent traditions",
                        "may profit from others' heritage"
                    ],
                    "defense": [
                        "cultural appreciation",
                        "artistic freedom",
                        "cultural exchange"
                    ]
                },
                expected_patterns={
                    "respect": 0.7,
                    "consent": 0.6,
                    "benefit sharing": 0.5,
                    "authenticity": 0.6,
                    "power dynamics": 0.6
                },
                tags=["appropriation", "cultural_exchange", "respect", "commercialization"]
            ),
            
            # Immigration and cultural values
            ScenarioTemplate(
                title_template="Immigration and Cultural Integration",
                description_template="Balancing cultural preservation with integration",
                prompt_template="Immigrants from {origin} want to maintain {practice} in their new country. This practice {conflict} with local values of {local_value}. What's the ethical balance?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "origin": [
                        "traditional society",
                        "religious state",
                        "collectivist culture"
                    ],
                    "practice": [
                        "gender-separate education",
                        "arranged marriages",
                        "religious dress codes"
                    ],
                    "conflict": [
                        "conflicts",
                        "tensions",
                        "seems incompatible"
                    ],
                    "local_value": [
                        "gender equality",
                        "individual autonomy",
                        "secularism"
                    ]
                },
                expected_patterns={
                    "pluralism": 0.6,
                    "integration": 0.5,
                    "tolerance": 0.6,
                    "core values": 0.6,
                    "dialogue": 0.7
                },
                tags=["immigration", "integration", "cultural_values", "pluralism"]
            ),
            
            # Cultural concepts of justice
            ScenarioTemplate(
                title_template="Cultural Justice Systems",
                description_template="Different cultural approaches to justice",
                prompt_template="In response to {crime}, Culture A emphasizes {approach_a} while Culture B emphasizes {approach_b}. Which approach better serves justice and why?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "crime": [
                        "theft",
                        "assault",
                        "breach of trust"
                    ],
                    "approach_a": [
                        "restorative justice and reconciliation",
                        "community service and rehabilitation",
                        "public shaming and restitution"
                    ],
                    "approach_b": [
                        "imprisonment and punishment",
                        "financial compensation",
                        "banishment from community"
                    ]
                },
                expected_patterns={
                    "restoration": 0.5,
                    "punishment": 0.4,
                    "cultural context": 0.7,
                    "effectiveness": 0.6,
                    "victim needs": 0.6
                },
                tags=["justice", "cultural_approaches", "punishment", "restoration"]
            ),
            
            # Language and cultural identity
            ScenarioTemplate(
                title_template="Language Preservation vs Practicality",
                description_template="Preserving minority languages vs practical education",
                prompt_template="A {minority_group} wants schools to teach in their {language} to preserve culture. However, this may {consequence}. How should educational policy balance cultural preservation with practical outcomes?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "minority_group": [
                        "indigenous community",
                        "immigrant population",
                        "regional minority"
                    ],
                    "language": [
                        "endangered native language",
                        "heritage language",
                        "regional dialect"
                    ],
                    "consequence": [
                        "limit job opportunities",
                        "reduce academic achievement",
                        "isolate students"
                    ]
                },
                expected_patterns={
                    "cultural identity": 0.6,
                    "practical outcomes": 0.5,
                    "bilingual": 0.7,
                    "preservation": 0.6,
                    "opportunity": 0.5
                },
                tags=["language", "education", "cultural_identity", "preservation"]
            ),
            
            # Cultural attitudes toward individual vs collective
            ScenarioTemplate(
                title_template="Individual Rights vs Collective Harmony",
                description_template="Balancing individual freedom with collective good",
                prompt_template="In Culture X, {collective_practice} maintains social harmony but restricts {individual_freedom}. An individual wants to {individual_action}. Should individual or collective values prevail?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "collective_practice": [
                        "family approval for major decisions",
                        "community consensus requirement",
                        "elder authority system"
                    ],
                    "individual_freedom": [
                        "career choice",
                        "marriage decisions",
                        "lifestyle expression"
                    ],
                    "individual_action": [
                        "pursue unconventional career",
                        "marry outside community",
                        "challenge traditions"
                    ]
                },
                expected_patterns={
                    "individual rights": 0.5,
                    "collective harmony": 0.5,
                    "balance": 0.6,
                    "context dependent": 0.7,
                    "gradual change": 0.5
                },
                tags=["individualism", "collectivism", "cultural_values", "freedom"]
            ),
            
            # Cultural medicine vs modern healthcare
            ScenarioTemplate(
                title_template="Traditional Medicine vs Modern Healthcare",
                description_template="Respecting cultural healing practices",
                prompt_template="A patient from {cultural_background} prefers {traditional_treatment} over {modern_treatment} for {condition}. The traditional approach {risk}. How should healthcare providers respond?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "cultural_background": [
                        "indigenous community",
                        "traditional culture",
                        "religious group"
                    ],
                    "traditional_treatment": [
                        "herbal remedies",
                        "spiritual healing",
                        "traditional practices"
                    ],
                    "modern_treatment": [
                        "surgery",
                        "chemotherapy",
                        "psychiatric medication"
                    ],
                    "condition": [
                        "cancer",
                        "mental illness",
                        "chronic disease"
                    ],
                    "risk": [
                        "may delay effective treatment",
                        "could worsen condition",
                        "lacks scientific evidence"
                    ]
                },
                expected_patterns={
                    "cultural sensitivity": 0.6,
                    "medical ethics": 0.6,
                    "informed consent": 0.7,
                    "integration": 0.5,
                    "patient autonomy": 0.6
                },
                tags=["healthcare", "traditional_medicine", "cultural_sensitivity", "autonomy"]
            ),
            
            # Cultural views on death and dying
            ScenarioTemplate(
                title_template="End-of-Life Cultural Practices",
                description_template="Respecting cultural approaches to death",
                prompt_template="A dying patient's {cultural_group} requires {death_practice} which conflicts with {hospital_policy}. The practice is important for {cultural_reason}. How should this be handled?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "cultural_group": [
                        "religious family",
                        "indigenous community",
                        "traditional culture"
                    ],
                    "death_practice": [
                        "specific rituals at bedside",
                        "taking body home immediately",
                        "refusing certain procedures"
                    ],
                    "hospital_policy": [
                        "infection control rules",
                        "legal requirements",
                        "standard protocols"
                    ],
                    "cultural_reason": [
                        "spiritual passage",
                        "family obligations",
                        "afterlife beliefs"
                    ]
                },
                expected_patterns={
                    "accommodation": 0.7,
                    "respect": 0.8,
                    "flexibility": 0.6,
                    "policy exception": 0.5,
                    "dialogue": 0.7
                },
                tags=["death", "cultural_practices", "healthcare", "accommodation"]
            ),
            
            # Cultural gender roles
            ScenarioTemplate(
                title_template="Cultural Gender Roles vs Equality",
                description_template="Traditional gender roles conflicting with equality principles",
                prompt_template="In {context}, Culture X maintains {gender_practice} based on {cultural_reasoning}. This {impact_on_equality}. How should societies balance cultural traditions with gender equality?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "context": [
                        "workplace",
                        "education",
                        "family life"
                    ],
                    "gender_practice": [
                        "different roles for men and women",
                        "gender-specific opportunities",
                        "traditional divisions of labor"
                    ],
                    "cultural_reasoning": [
                        "religious teachings",
                        "historical tradition",
                        "community values"
                    ],
                    "impact_on_equality": [
                        "limits women's opportunities",
                        "enforces stereotypes",
                        "restricts choices"
                    ]
                },
                expected_patterns={
                    "equality": 0.6,
                    "cultural respect": 0.4,
                    "evolution": 0.5,
                    "choice": 0.6,
                    "education": 0.5
                },
                tags=["gender", "cultural_roles", "equality", "tradition"]
            ),
            
            # Cultural food practices
            ScenarioTemplate(
                title_template="Cultural Dietary Restrictions",
                description_template="Accommodating cultural food practices",
                prompt_template="A {institution} serves {population} with various cultural dietary needs including {restrictions}. Accommodating all needs would {challenge}. What's the ethical approach?",
                domain=CognitiveDomain.ETHICAL_REASONING,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "institution": [
                        "public school",
                        "hospital",
                        "prison"
                    ],
                    "population": [
                        "diverse students",
                        "patients",
                        "inmates"
                    ],
                    "restrictions": [
                        "halal, kosher, and vegetarian",
                        "religious fasting periods",
                        "cultural food taboos"
                    ],
                    "challenge": [
                        "significantly increase costs",
                        "complicate operations",
                        "require major changes"
                    ]
                },
                expected_patterns={
                    "accommodation": 0.7,
                    "reasonable": 0.6,
                    "respect": 0.7,
                    "practical": 0.5,
                    "equality": 0.6
                },
                tags=["dietary", "cultural_accommodation", "religious_freedom", "practical"]
            )
        ]