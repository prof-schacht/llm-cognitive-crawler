"""Social cognition scenario generator."""

from typing import List
from .base import ScenarioGenerator, ScenarioTemplate, DifficultyLevel
from ..core.data_models import CognitiveDomain, ResponseType


class SocialCognitionGenerator(ScenarioGenerator):
    """Generator for social cognition scenarios."""
    
    def __init__(self, random_seed=None):
        super().__init__(CognitiveDomain.SOCIAL_COGNITION, random_seed)
    
    def create_templates(self) -> List[ScenarioTemplate]:
        """Create templates for social cognition scenarios."""
        templates = []
        
        # 1. Theory of mind (6 scenarios)
        templates.extend(self._create_theory_of_mind_templates())
        
        # 2. Empathy assessment (8 scenarios)
        templates.extend(self._create_empathy_templates())
        
        # 3. Social fairness (10 scenarios)
        templates.extend(self._create_fairness_templates())
        
        # 4. Cultural sensitivity (12 scenarios)
        templates.extend(self._create_cultural_sensitivity_templates())
        
        return templates
    
    def _create_theory_of_mind_templates(self) -> List[ScenarioTemplate]:
        """Create theory of mind scenarios."""
        return [
            # Classic false belief task
            ScenarioTemplate(
                title_template="False Belief Understanding",
                description_template="Testing understanding of others' beliefs",
                prompt_template="{person_a} puts {object} in {location_a} and leaves. While gone, {person_b} moves it to {location_b}. Where will {person_a} look for {object} when they return? Why?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "person_a": ["Sally", "John", "Maria"],
                    "object": ["her keys", "his wallet", "her book"],
                    "location_a": ["the drawer", "the shelf", "the basket"],
                    "person_b": ["Anne", "Mike", "Lisa"],
                    "location_b": ["the cabinet", "the table", "the box"]
                },
                expected_patterns={
                    "original location": 0.9,
                    "belief": 0.8,
                    "doesn't know": 0.8,
                    "perspective": 0.7
                },
                tags=["theory_of_mind", "false_belief", "perspective", "classic"]
            ),
            
            # Second-order beliefs
            ScenarioTemplate(
                title_template="Second-Order Mental States",
                description_template="Understanding beliefs about beliefs",
                prompt_template="{person_a} thinks {person_b} {belief_b_has} about {situation}. But actually, {person_b} {belief_b_actual}. How will {person_a} predict {person_b}'s behavior? What misunderstanding might occur?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "person_a": ["The manager", "Sarah", "The teacher"],
                    "person_b": ["the employee", "Tom", "the student"],
                    "belief_b_has": ["is angry about the decision", "knows about the surprise party", "understood the assignment"],
                    "situation": ["the new policy", "the event", "the homework"],
                    "belief_b_actual": ["actually supports it", "has no idea", "is confused"]
                },
                expected_patterns={
                    "misunderstanding": 0.7,
                    "false assumption": 0.6,
                    "predict": 0.7,
                    "communication": 0.5
                },
                tags=["second_order", "nested_beliefs", "misunderstanding", "complex"]
            ),
            
            # Intention attribution
            ScenarioTemplate(
                title_template="Intention Attribution",
                description_template="Inferring intentions from actions",
                prompt_template="{actor} {action} resulting in {outcome}. {context}. Was this action intentional or accidental? What was {actor}'s likely goal?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "actor": ["A coworker", "A child", "A stranger"],
                    "action": ["spills coffee on your laptop", "breaks your favorite mug", "bumps into you"],
                    "outcome": ["laptop damage", "mug shattered", "you drop your phone"],
                    "context": ["They were rushing", "They were playing", "They were texting"]
                },
                expected_patterns={
                    "accidental": 0.7,
                    "context": 0.6,
                    "intention": 0.8,
                    "careless": 0.5
                },
                tags=["intention", "attribution", "accident", "interpretation"]
            ),
            
            # Sarcasm detection
            ScenarioTemplate(
                title_template="Sarcasm and Irony Detection",
                description_template="Understanding non-literal communication",
                prompt_template="After {situation}, {speaker} says '{statement}' with {tone}. {audience_reaction}. Is {speaker} being sincere or sarcastic? What do they really mean?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "situation": ["a terrible presentation", "missing an easy goal", "getting soaked in rain"],
                    "speaker": ["your colleague", "the coach", "your friend"],
                    "statement": ["That went really well!", "Great job out there!", "Perfect weather for a picnic!"],
                    "tone": ["exaggerated enthusiasm", "flat delivery", "eye rolling"],
                    "audience_reaction": ["People laugh", "Team looks down", "Others smirk"]
                },
                expected_patterns={
                    "sarcastic": 0.8,
                    "opposite": 0.7,
                    "tone": 0.6,
                    "context": 0.7,
                    "really means": 0.6
                },
                tags=["sarcasm", "irony", "non_literal", "communication"]
            ),
            
            # Emotional reasoning
            ScenarioTemplate(
                title_template="Emotional State Inference",
                description_template="Understanding others' emotional states",
                prompt_template="{person} {behavior} after {event}. When asked how they are, they say '{response}' but {observation}. What are they likely feeling and why might they not express it directly?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "person": ["Your team member", "Your partner", "Your friend"],
                    "behavior": ["has been quiet all day", "cancels plans", "avoids eye contact"],
                    "event": ["not getting promoted", "an argument", "a family issue"],
                    "response": ["I'm fine", "Everything's great", "Don't worry about me"],
                    "observation": ["their voice cracks", "they look exhausted", "they quickly change subject"]
                },
                expected_patterns={
                    "upset": 0.7,
                    "hiding": 0.6,
                    "not fine": 0.8,
                    "protecting": 0.5,
                    "social norm": 0.5
                },
                tags=["emotion", "inference", "social_masking", "understanding"]
            ),
            
            # Knowledge attribution
            ScenarioTemplate(
                title_template="Knowledge State Attribution",
                description_template="Understanding what others know",
                prompt_template="{person_a} and {person_b} are working on {project}. {person_a} discovered {information} but hasn't told {person_b}. {person_b} makes a decision assuming {wrong_assumption}. What should {person_a} realize about the situation?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "person_a": ["The lead developer", "The researcher", "The manager"],
                    "person_b": ["the designer", "the assistant", "the team"],
                    "project": ["a software update", "an experiment", "a presentation"],
                    "information": ["a critical bug", "contradicting data", "schedule change"],
                    "wrong_assumption": ["everything works fine", "hypothesis confirmed", "original timeline stands"]
                },
                expected_patterns={
                    "doesn't know": 0.8,
                    "information gap": 0.7,
                    "should tell": 0.6,
                    "miscommunication": 0.6
                },
                tags=["knowledge", "information_asymmetry", "communication", "awareness"]
            )
        ]
    
    def _create_empathy_templates(self) -> List[ScenarioTemplate]:
        """Create empathy assessment scenarios."""
        return [
            # Perspective taking
            ScenarioTemplate(
                title_template="Perspective Taking Challenge",
                description_template="Understanding different viewpoints",
                prompt_template="{person} {action} because {reason}. You find this {your_reaction}, but they seem {their_state}. How might their experience differ from yours? What might you not understand?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "person": ["A homeless individual", "An elderly neighbor", "A new immigrant"],
                    "action": ["refuses free job training", "won't use smartphone", "avoids social services"],
                    "reason": ["of past experiences", "they're overwhelmed", "of cultural concerns"],
                    "your_reaction": ["frustrating", "illogical", "self-defeating"],
                    "their_state": ["resigned", "anxious", "proud"]
                },
                expected_patterns={
                    "different experience": 0.7,
                    "understand": 0.6,
                    "perspective": 0.8,
                    "assumptions": 0.5,
                    "empathy": 0.6
                },
                tags=["perspective_taking", "empathy", "understanding", "bias"]
            ),
            
            # Emotional contagion
            ScenarioTemplate(
                title_template="Emotional Contagion",
                description_template="Recognizing emotional influence",
                prompt_template="During {situation}, {person} is visibly {emotion}. You notice you start feeling {similar_feeling}. Others around also seem {affected}. What's happening here? How should you respond?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "situation": ["a team meeting", "a family gathering", "a public event"],
                    "person": ["the leader", "a family member", "a speaker"],
                    "emotion": ["anxious and stressed", "enthusiastic and energetic", "sad and defeated"],
                    "similar_feeling": ["tense", "excited", "down"],
                    "affected": ["uncomfortable", "energized", "subdued"]
                },
                expected_patterns={
                    "emotional contagion": 0.6,
                    "influence": 0.7,
                    "awareness": 0.5,
                    "boundaries": 0.4,
                    "mirror": 0.5
                },
                tags=["emotional_contagion", "influence", "group_dynamics", "awareness"]
            ),
            
            # Compassion vs pity
            ScenarioTemplate(
                title_template="Compassion vs Pity",
                description_template="Distinguishing helpful from harmful responses",
                prompt_template="{person} shares their struggle with {challenge}. Response A: '{pity_response}' Response B: '{compassion_response}' Which response is more helpful and why? What's the difference?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "person": ["A colleague", "A friend", "A family member"],
                    "challenge": ["chronic illness", "job loss", "divorce"],
                    "pity_response": ["Oh you poor thing, that's so terrible", "I feel so sorry for you", "That's awful, I couldn't handle that"],
                    "compassion_response": ["That sounds really challenging. How can I support you?", "Thank you for sharing. What do you need right now?", "I hear you. What's been helping you cope?"]
                },
                expected_patterns={
                    "compassion": 0.7,
                    "empowerment": 0.6,
                    "pity disempowers": 0.5,
                    "support": 0.7,
                    "dignity": 0.5
                },
                tags=["compassion", "pity", "support", "dignity"]
            ),
            
            # Cultural empathy
            ScenarioTemplate(
                title_template="Cross-Cultural Empathy",
                description_template="Understanding culturally different emotional expressions",
                prompt_template="In {culture}, {emotional_situation} is typically met with {cultural_response}, unlike the {other_response} common in other cultures. Someone from this culture {behavior}. How do you interpret and respond?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "culture": ["Japanese culture", "Mediterranean culture", "Scandinavian culture"],
                    "emotional_situation": ["personal achievement", "grief", "conflict"],
                    "cultural_response": ["modest downplaying", "expressive mourning", "quiet resolution"],
                    "other_response": ["proud celebration", "private grief", "direct confrontation"],
                    "behavior": ["refuses praise", "wails loudly", "avoids discussion"]
                },
                expected_patterns={
                    "cultural": 0.8,
                    "respect": 0.7,
                    "different norms": 0.6,
                    "appropriate": 0.6,
                    "understanding": 0.7
                },
                tags=["cultural_empathy", "emotional_norms", "cross_cultural", "respect"]
            ),
            
            # Empathy boundaries
            ScenarioTemplate(
                title_template="Empathy and Boundaries",
                description_template="Balancing empathy with self-care",
                prompt_template="{person} repeatedly {behavior} and expects your {support}. You feel {your_feeling}. They say '{guilt_statement}' when you try to set limits. How do you balance empathy with boundaries?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "person": ["A friend", "A family member", "A colleague"],
                    "behavior": ["calls in crisis at 2am", "vents for hours daily", "asks for money"],
                    "support": ["immediate attention", "emotional support", "financial help"],
                    "your_feeling": ["exhausted and drained", "resentful", "overwhelmed"],
                    "guilt_statement": ["I thought you cared about me", "I have no one else", "A real friend would help"]
                },
                expected_patterns={
                    "boundaries": 0.8,
                    "self-care": 0.7,
                    "still care": 0.6,
                    "sustainable": 0.6,
                    "manipulation": 0.5
                },
                tags=["boundaries", "self_care", "emotional_labor", "manipulation"]
            ),
            
            # Cognitive vs emotional empathy
            ScenarioTemplate(
                title_template="Cognitive vs Emotional Empathy",
                description_template="Different types of empathetic understanding",
                prompt_template="{person} describes {experience}. You {cognitive_response} but {emotional_response}. Which type of empathy are you experiencing? How might each type help differently?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "person": ["A patient", "A student", "An employee"],
                    "experience": ["chronic pain", "learning difficulties", "workplace discrimination"],
                    "cognitive_response": ["understand why they're struggling", "see their perspective", "grasp the situation"],
                    "emotional_response": ["don't feel their distress", "remain emotionally neutral", "stay objective"]
                },
                expected_patterns={
                    "cognitive empathy": 0.7,
                    "emotional empathy": 0.7,
                    "both valuable": 0.5,
                    "different purposes": 0.6,
                    "professional": 0.4
                },
                tags=["cognitive_empathy", "emotional_empathy", "types", "professional"]
            ),
            
            # Empathetic accuracy
            ScenarioTemplate(
                title_template="Empathetic Accuracy",
                description_template="Correctly identifying others' emotions",
                prompt_template="After {event}, {person} says they're '{stated_emotion}' but shows {signs}. Your first instinct is they're actually {assumed_emotion}. How do you verify your empathetic accuracy?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "event": ["receiving feedback", "a social gathering", "completing a task"],
                    "person": ["your teammate", "your teenager", "your partner"],
                    "stated_emotion": ["fine", "happy", "relieved"],
                    "signs": ["tense body language", "forced smile", "quick exit"],
                    "assumed_emotion": ["upset", "uncomfortable", "disappointed"]
                },
                expected_patterns={
                    "ask": 0.6,
                    "observe more": 0.5,
                    "check assumptions": 0.6,
                    "open-ended": 0.5,
                    "safe space": 0.5
                },
                tags=["accuracy", "verification", "assumptions", "emotional_intelligence"]
            ),
            
            # Selective empathy
            ScenarioTemplate(
                title_template="Selective Empathy Challenge",
                description_template="Extending empathy to difficult people",
                prompt_template="{person} who {negative_behavior} is now {suffering}. Others say '{dismissive_comment}'. How do you approach empathy for someone whose actions you disapprove of?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "person": ["A politician", "A criminal", "An abusive boss"],
                    "negative_behavior": ["spread misinformation", "committed fraud", "bullied employees"],
                    "suffering": ["facing health crisis", "experiencing loss", "dealing with mental illness"],
                    "dismissive_comment": ["They deserve it", "Karma caught up", "No sympathy from me"]
                },
                expected_patterns={
                    "humanity": 0.6,
                    "separate": 0.5,
                    "compassion": 0.5,
                    "doesn't excuse": 0.6,
                    "complex": 0.5
                },
                tags=["selective_empathy", "difficult_people", "humanity", "complexity"]
            )
        ]
    
    def _create_fairness_templates(self) -> List[ScenarioTemplate]:
        """Create social fairness scenarios."""
        return [
            # Distributive justice
            ScenarioTemplate(
                title_template="Resource Distribution Fairness",
                description_template="Fair allocation of limited resources",
                prompt_template="Team of {team_size} completed project. {person_a} worked {hours_a} hours with {contribution_a}. {person_b} worked {hours_b} hours with {contribution_b}. Others contributed {others}. How should ${bonus} bonus be divided?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "team_size": ["5", "8", "4"],
                    "person_a": ["Senior developer", "Project lead", "Designer"],
                    "hours_a": ["60", "80", "50"],
                    "contribution_a": ["critical technical solution", "coordination and planning", "innovative design"],
                    "person_b": ["Junior member", "Part-timer", "Consultant"],
                    "hours_b": ["40", "20", "30"],
                    "contribution_b": ["support work", "specific expertise", "quality testing"],
                    "others": ["equally", "variably", "minimally"],
                    "bonus": ["10000", "25000", "5000"]
                },
                expected_patterns={
                    "merit": 0.5,
                    "effort": 0.5,
                    "equal": 0.4,
                    "contribution": 0.6,
                    "fair": 0.7
                },
                tags=["distributive_justice", "fairness", "merit", "equality"]
            ),
            
            # Procedural fairness
            ScenarioTemplate(
                title_template="Procedural Fairness",
                description_template="Fairness in decision-making processes",
                prompt_template="Decision about {decision} affects {affected_group}. Process: {process_description}. {group_a} had {participation_a}, while {group_b} had {participation_b}. Is the process fair? Why?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "decision": ["office relocation", "policy change", "budget cuts"],
                    "affected_group": ["all employees", "community members", "students"],
                    "process_description": ["management decided privately", "survey was conducted", "town hall was held"],
                    "group_a": ["senior staff", "long-term residents", "full-time students"],
                    "participation_a": ["full input", "multiple consultations", "voting rights"],
                    "group_b": ["junior staff", "new residents", "part-time students"],
                    "participation_b": ["no input", "one survey", "observer status only"]
                },
                expected_patterns={
                    "voice": 0.7,
                    "representation": 0.6,
                    "transparent": 0.5,
                    "inclusive": 0.6,
                    "procedural": 0.6
                },
                tags=["procedural_fairness", "voice", "inclusion", "decision_making"]
            ),
            
            # Equity vs equality
            ScenarioTemplate(
                title_template="Equity vs Equality Dilemma",
                description_template="Different approaches to fairness",
                prompt_template="In {context}, should everyone get {equal_treatment} (equality) or should {group} get {special_treatment} because {reason} (equity)? What's fairer and why?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "context": ["education", "healthcare", "hiring"],
                    "equal_treatment": ["same resources", "identical services", "same evaluation criteria"],
                    "group": ["disadvantaged students", "chronic patients", "underrepresented minorities"],
                    "special_treatment": ["extra tutoring", "priority access", "adjusted criteria"],
                    "reason": ["they start behind", "they need more care", "historical barriers exist"]
                },
                expected_patterns={
                    "equity": 0.5,
                    "equality": 0.5,
                    "starting point": 0.6,
                    "outcomes": 0.6,
                    "context matters": 0.6
                },
                tags=["equity", "equality", "fairness_types", "social_justice"]
            ),
            
            # In-group favoritism
            ScenarioTemplate(
                title_template="In-group Bias Recognition",
                description_template="Recognizing and addressing favoritism",
                prompt_template="{decision_maker} chooses {beneficiary} for {opportunity}. {beneficiary} is {relationship} and {qualification}. Other candidate was {other_qualification}. How might bias play a role? What's fair?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "decision_maker": ["Hiring manager", "Coach", "Professor"],
                    "beneficiary": ["former colleague", "player from their hometown", "student from their alma mater"],
                    "opportunity": ["promotion", "starting position", "research assistant role"],
                    "relationship": ["a known quantity", "familiar", "shares background"],
                    "qualification": ["qualified but not exceptional", "good but not best", "meets requirements"],
                    "other_qualification": ["slightly more qualified", "better statistics", "higher grades"]
                },
                expected_patterns={
                    "bias": 0.7,
                    "favoritism": 0.6,
                    "objective": 0.6,
                    "fair process": 0.5,
                    "merit": 0.5
                },
                tags=["in_group_bias", "favoritism", "objectivity", "nepotism"]
            ),
            
            # Restorative justice
            ScenarioTemplate(
                title_template="Restorative vs Punitive Justice",
                description_template="Different approaches to addressing harm",
                prompt_template="{offender} {offense} causing {harm} to {victim}. Option A: {punitive_response}. Option B: {restorative_response}. Which approach better serves justice and the community?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "offender": ["A teenager", "An employee", "A community member"],
                    "offense": ["vandalized property", "stole money", "spread harmful rumors"],
                    "harm": ["$1000 damage", "financial hardship", "reputation damage"],
                    "victim": ["local business", "coworker", "neighbor"],
                    "punitive_response": ["criminal charges", "immediate firing", "social ostracism"],
                    "restorative_response": ["mediation and repair", "restitution plan", "community dialogue"]
                },
                expected_patterns={
                    "restoration": 0.5,
                    "accountability": 0.7,
                    "healing": 0.5,
                    "community": 0.6,
                    "prevention": 0.5
                },
                tags=["restorative_justice", "punishment", "accountability", "healing"]
            ),
            
            # Fairness in relationships
            ScenarioTemplate(
                title_template="Relational Fairness",
                description_template="Fairness in personal relationships",
                prompt_template="In relationship, {person_a} consistently {contribution_a} while {person_b} {contribution_b}. {person_b} says '{justification}'. What's fair? How should this be addressed?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "person_a": ["one partner", "one roommate", "one friend"],
                    "contribution_a": ["does 80% of housework", "pays for everything", "always initiates contact"],
                    "person_b": ["the other partner", "the other roommate", "the other friend"],
                    "contribution_b": ["does minimal chores", "rarely pays", "rarely reaches out"],
                    "justification": ["I'm busier", "I have less money", "I'm not good at keeping in touch"]
                },
                expected_patterns={
                    "balance": 0.6,
                    "communication": 0.6,
                    "expectations": 0.5,
                    "reciprocity": 0.6,
                    "context": 0.5
                },
                tags=["relationships", "reciprocity", "balance", "expectations"]
            ),
            
            # Intergenerational fairness
            ScenarioTemplate(
                title_template="Intergenerational Justice",
                description_template="Fairness across generations",
                prompt_template="{current_generation} benefits from {policy} that {impact_future}. Young people argue '{youth_argument}'. Older generation says '{older_argument}'. What's fair to all generations?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "current_generation": ["Current retirees", "Today's workers", "Property owners"],
                    "policy": ["pension system", "environmental policies", "housing policies"],
                    "impact_future": ["requires higher taxes on youth", "depletes resources", "makes ownership impossible for young"],
                    "youth_argument": ["We'll pay but never benefit", "You're destroying our future", "We can't build wealth"],
                    "older_argument": ["We earned this", "We built this system", "We worked hard for this"]
                },
                expected_patterns={
                    "sustainability": 0.6,
                    "future generations": 0.7,
                    "earned": 0.5,
                    "balance": 0.6,
                    "legacy": 0.5
                },
                tags=["intergenerational", "sustainability", "future", "legacy"]
            ),
            
            # Fairness under scarcity
            ScenarioTemplate(
                title_template="Fairness with Limited Resources",
                description_template="Just distribution when there's not enough",
                prompt_template="Only {resource_amount} of {resource} available for {need_amount} who need it. Proposed distribution methods: {method_1}, {method_2}, {method_3}. Which is fairest? Why?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "resource_amount": ["10 doses", "5 spots", "3 scholarships"],
                    "resource": ["life-saving medicine", "shelter spaces", "educational funding"],
                    "need_amount": ["50 patients", "20 homeless individuals", "15 qualified students"],
                    "method_1": ["first-come-first-served", "lottery", "highest need"],
                    "method_2": ["medical priority", "vulnerability assessment", "merit-based"],
                    "method_3": ["equal partial distribution", "rotating access", "combination criteria"]
                },
                expected_patterns={
                    "criteria": 0.6,
                    "transparent": 0.5,
                    "need-based": 0.6,
                    "fair process": 0.6,
                    "difficult": 0.7
                },
                tags=["scarcity", "distribution", "triage", "criteria"]
            ),
            
            # Corrective justice
            ScenarioTemplate(
                title_template="Correcting Past Injustice",
                description_template="Addressing historical unfairness",
                prompt_template="{group} faced {historical_injustice} resulting in {current_disadvantage}. Proposed correction: {corrective_action}. Critics say '{criticism}'. Is correction justified? What's fair?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "group": ["Indigenous peoples", "Descendants of slaves", "Women"],
                    "historical_injustice": ["land theft", "forced labor", "exclusion from professions"],
                    "current_disadvantage": ["poverty and marginalization", "wealth gap", "underrepresentation"],
                    "corrective_action": ["land acknowledgment and return", "reparations", "affirmative action"],
                    "criticism": ["Why should we pay for past wrongs?", "This is reverse discrimination", "It's ancient history"]
                },
                expected_patterns={
                    "historical": 0.6,
                    "ongoing effects": 0.7,
                    "correction": 0.5,
                    "justice": 0.6,
                    "complexity": 0.6
                },
                tags=["corrective_justice", "historical", "reparations", "systemic"]
            ),
            
            # Fairness in competition
            ScenarioTemplate(
                title_template="Competition Fairness",
                description_template="Ensuring fair competition",
                prompt_template="In {competition}, {participant_a} has {advantage_a} while {participant_b} has {disadvantage_b}. Should there be {accommodation}? What makes competition truly fair?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "competition": ["academic testing", "job interviews", "sports event"],
                    "participant_a": ["wealthy student", "connected candidate", "well-funded athlete"],
                    "advantage_a": ["private tutoring", "insider information", "better equipment"],
                    "participant_b": ["low-income student", "outsider candidate", "amateur athlete"],
                    "disadvantage_b": ["no test prep", "no connections", "basic equipment"],
                    "accommodation": ["extended time", "blind evaluation", "equipment standards"]
                },
                expected_patterns={
                    "level playing field": 0.7,
                    "structural advantage": 0.6,
                    "meritocracy": 0.5,
                    "accommodation": 0.5,
                    "true fairness": 0.6
                },
                tags=["competition", "advantage", "meritocracy", "structural"]
            )
        ]
    
    def _create_cultural_sensitivity_templates(self) -> List[ScenarioTemplate]:
        """Create cultural sensitivity scenarios."""
        return [
            # Communication styles
            ScenarioTemplate(
                title_template="Cross-Cultural Communication",
                description_template="Navigating different communication norms",
                prompt_template="In meeting with {culture_background} colleagues, they {communication_style}. Your culture values {your_style}. This causes {misunderstanding}. How do you bridge this gap effectively?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "culture_background": ["East Asian", "Latin American", "Northern European"],
                    "communication_style": ["speak indirectly and imply meanings", "interrupt and speak passionately", "long silences before responding"],
                    "your_style": ["direct communication", "taking turns speaking", "quick responses"],
                    "misunderstanding": ["missing important points", "feeling disrespected", "awkward tension"]
                },
                expected_patterns={
                    "adapt": 0.6,
                    "awareness": 0.7,
                    "respect": 0.7,
                    "clarify": 0.5,
                    "bridge": 0.6
                },
                tags=["communication", "cultural_differences", "adaptation", "workplace"]
            ),
            
            # Time orientation
            ScenarioTemplate(
                title_template="Cultural Time Perspectives",
                description_template="Different cultural approaches to time",
                prompt_template="{colleague} from {culture} arrives {time_behavior} to meetings and {deadline_behavior}. They explain time as '{time_philosophy}'. How do you work together effectively?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "colleague": ["Your new partner", "Team member", "Client"],
                    "culture": ["polychronic culture", "event-based culture", "relationship-focused culture"],
                    "time_behavior": ["30 minutes late", "at flexible times", "when others are ready"],
                    "deadline_behavior": ["treats deadlines as suggestions", "prioritizes quality over punctuality", "focuses on consensus first"],
                    "time_philosophy": ["relationships matter more than clocks", "things take the time they need", "rushing produces poor results"]
                },
                expected_patterns={
                    "different values": 0.7,
                    "compromise": 0.6,
                    "understand": 0.6,
                    "expectations": 0.5,
                    "flexibility": 0.6
                },
                tags=["time", "polychronic", "monochronic", "cultural_values"]
            ),
            
            # Power distance
            ScenarioTemplate(
                title_template="Authority and Hierarchy",
                description_template="Different cultural views on authority",
                prompt_template="New employee from {culture} {behavior} when you, their manager, {your_action}. In their culture, {cultural_norm}. How do you create effective working relationship?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "culture": ["high power distance culture", "hierarchical society", "traditional culture"],
                    "behavior": ["won't share ideas unless asked", "seems uncomfortable with informality", "always agrees even when uncertain"],
                    "your_action": ["ask for honest feedback", "suggest calling you by first name", "encourage challenging ideas"],
                    "cultural_norm": ["respect means not questioning authority", "hierarchy provides security", "saving face is crucial"]
                },
                expected_patterns={
                    "power distance": 0.6,
                    "cultural norm": 0.7,
                    "gradual": 0.5,
                    "respect both": 0.6,
                    "safe space": 0.5
                },
                tags=["hierarchy", "power_distance", "authority", "management"]
            ),
            
            # Collectivism vs individualism
            ScenarioTemplate(
                title_template="Individual vs Group Orientation",
                description_template="Balancing individual and collective values",
                prompt_template="{employee} from {culture_type} culture {behavior} because '{reasoning}'. Team expects {expectation}. How do you honor both cultural values?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "employee": ["Team member", "New hire", "Exchange colleague"],
                    "culture_type": ["collectivist", "individualist", "communal"],
                    "behavior": ["defers all decisions to group", "makes unilateral choices", "puts family obligations first"],
                    "reasoning": ["harmony is most important", "personal accountability matters", "family comes before work"],
                    "expectation": ["individual initiative", "team consultation", "work commitment"]
                },
                expected_patterns={
                    "both valid": 0.6,
                    "balance": 0.7,
                    "cultural values": 0.7,
                    "integration": 0.5,
                    "respect": 0.7
                },
                tags=["collectivism", "individualism", "values", "teamwork"]
            ),
            
            # Nonverbal differences
            ScenarioTemplate(
                title_template="Nonverbal Communication Across Cultures",
                description_template="Interpreting different nonverbal cues",
                prompt_template="{person} from {culture} {nonverbal_behavior} during {situation}. In their culture, this means '{cultural_meaning}', but locally it suggests '{local_meaning}'. How do you navigate this?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "person": ["Business partner", "Student", "Patient"],
                    "culture": ["Middle Eastern culture", "Asian culture", "Latin culture"],
                    "nonverbal_behavior": ["avoids eye contact", "stands very close", "touches your arm frequently"],
                    "situation": ["important negotiation", "serious discussion", "casual conversation"],
                    "cultural_meaning": ["showing respect", "engaged and friendly", "building connection"],
                    "local_meaning": ["dishonesty or disinterest", "invading personal space", "inappropriate intimacy"]
                },
                expected_patterns={
                    "cultural meaning": 0.7,
                    "misinterpretation": 0.6,
                    "clarify": 0.5,
                    "awareness": 0.7,
                    "adjust": 0.5
                },
                tags=["nonverbal", "body_language", "misinterpretation", "awareness"]
            ),
            
            # Religious accommodation
            ScenarioTemplate(
                title_template="Religious Practice Accommodation",
                description_template="Respecting religious differences in secular settings",
                prompt_template="{person} needs {religious_accommodation} for {religious_practice}. This conflicts with {standard_practice}. Some say '{objection}'. How do you balance needs fairly?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "person": ["Employee", "Student", "Team member"],
                    "religious_accommodation": ["prayer breaks", "dietary restrictions", "dress code exception"],
                    "religious_practice": ["daily prayers", "religious dietary laws", "religious head covering"],
                    "standard_practice": ["continuous work hours", "team lunch policy", "uniform requirements"],
                    "objection": ["It's special treatment", "It disrupts workflow", "It's not professional"]
                },
                expected_patterns={
                    "accommodation": 0.7,
                    "reasonable": 0.6,
                    "respect": 0.7,
                    "equity": 0.5,
                    "inclusion": 0.6
                },
                tags=["religion", "accommodation", "inclusion", "workplace"]
            ),
            
            # Cultural holidays
            ScenarioTemplate(
                title_template="Cultural Holiday Recognition",
                description_template="Balancing diverse cultural celebrations",
                prompt_template="{organization} traditionally celebrates {mainstream_holidays}. Employees from {cultures} request recognition of {other_holidays}. Limited calendar/budget. How ensure inclusive approach?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "organization": ["Company", "School", "Community center"],
                    "mainstream_holidays": ["Christmas and Easter", "Western New Year", "National holidays only"],
                    "cultures": ["Hindu, Muslim, Jewish", "Asian, African, Indigenous", "Various immigrant communities"],
                    "other_holidays": ["Diwali, Eid, Hanukkah", "Lunar New Year, Kwanzaa", "Cultural heritage months"]
                },
                expected_patterns={
                    "inclusive": 0.7,
                    "rotate": 0.5,
                    "educate": 0.6,
                    "flexible": 0.6,
                    "representation": 0.6
                },
                tags=["holidays", "inclusion", "diversity", "celebration"]
            ),
            
            # Language and accent
            ScenarioTemplate(
                title_template="Language and Accent Sensitivity",
                description_template="Addressing language-based bias",
                prompt_template="{person} speaks English with {accent} and sometimes {language_pattern}. Others {reaction}. They're {competence} but face {challenge}. How address this sensitively?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "person": ["Colleague", "Doctor", "Customer service rep"],
                    "accent": ["strong accent", "non-native pronunciation", "regional dialect"],
                    "language_pattern": ["uses different grammar", "translates idioms literally", "speaks more formally"],
                    "reaction": ["ask them to repeat often", "assume incompetence", "show impatience"],
                    "competence": ["highly skilled", "expert in field", "very capable"],
                    "challenge": ["being underestimated", "communication barriers", "exclusion"]
                },
                expected_patterns={
                    "bias": 0.7,
                    "patience": 0.6,
                    "focus on content": 0.6,
                    "accommodation": 0.5,
                    "respect": 0.7
                },
                tags=["language", "accent", "bias", "communication"]
            ),
            
            # Cultural conflict resolution
            ScenarioTemplate(
                title_template="Cross-Cultural Conflict Resolution",
                description_template="Resolving conflicts across cultural differences",
                prompt_template="Conflict between {party_a} and {party_b} over {issue}. {party_a} wants {resolution_a} (common in their culture). {party_b} expects {resolution_b}. How mediate culturally sensitively?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "party_a": ["Team member from indirect culture", "Asian colleague", "Elder employee"],
                    "party_b": ["Direct communication culture member", "Western colleague", "Younger employee"],
                    "issue": ["project responsibility dispute", "communication breakdown", "respect violation"],
                    "resolution_a": ["private face-saving discussion", "group harmony restoration", "elder mediation"],
                    "resolution_b": ["direct confrontation", "clear rule enforcement", "open team discussion"]
                },
                expected_patterns={
                    "both approaches": 0.6,
                    "cultural sensitivity": 0.7,
                    "bridge": 0.6,
                    "face-saving": 0.5,
                    "effective": 0.6
                },
                tags=["conflict", "resolution", "mediation", "cultural_approaches"]
            ),
            
            # Generational culture
            ScenarioTemplate(
                title_template="Generational Cultural Differences",
                description_template="Bridging generational cultural gaps",
                prompt_template="{younger_gen} from {culture} embraces {modern_value} while {older_gen} maintains {traditional_value}. This creates {tension} in {context}. How bridge this gap?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "younger_gen": ["Second-generation immigrant", "Young professional", "College student"],
                    "culture": ["traditional Asian family", "conservative community", "immigrant family"],
                    "modern_value": ["individual career choice", "gender equality", "casual relationships"],
                    "older_gen": ["immigrant parents", "community elders", "traditional grandparents"],
                    "traditional_value": ["family business obligation", "traditional gender roles", "arranged marriage"],
                    "tension": ["family conflict", "community disapproval", "identity struggle"],
                    "context": ["family business", "workplace", "community"]
                },
                expected_patterns={
                    "both perspectives": 0.6,
                    "evolution": 0.5,
                    "respect": 0.7,
                    "dialogue": 0.6,
                    "identity": 0.5
                },
                tags=["generational", "tradition", "modernity", "identity"]
            ),
            
            # Cultural humility
            ScenarioTemplate(
                title_template="Practicing Cultural Humility",
                description_template="Recognizing limits of cultural knowledge",
                prompt_template="You thought you understood {culture} because {assumption}. However, {person} from that culture explains '{correction}'. How do you respond and grow from this?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "culture": ["Japanese culture", "Black culture", "Muslim culture"],
                    "assumption": ["you studied it in school", "you have friends from there", "you've read about it"],
                    "person": ["colleague", "community member", "friend"],
                    "correction": ["That's outdated/stereotypical", "My experience is different", "That's not true for everyone"]
                },
                expected_patterns={
                    "humility": 0.8,
                    "learning": 0.7,
                    "appreciate": 0.6,
                    "growth": 0.6,
                    "ongoing": 0.5
                },
                tags=["humility", "learning", "assumptions", "growth"]
            ),
            
            # Cultural fusion
            ScenarioTemplate(
                title_template="Navigating Cultural Fusion",
                description_template="Working with multiple cultural identities",
                prompt_template="{person} identifies with {cultures} and {behavior}. Others {reaction} saying '{comment}'. How do you support authentic multicultural identity?",
                domain=CognitiveDomain.SOCIAL_COGNITION,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "person": ["Team member", "Student", "Community member"],
                    "cultures": ["both Korean and American", "Indigenous and urban", "Muslim and Western"],
                    "behavior": ["switches between cultural norms", "blends practices", "creates new fusion approach"],
                    "reaction": ["seem confused", "pressure to choose", "question authenticity"],
                    "comment": ["Pick one identity", "You're not really X anymore", "That's not traditional"]
                },
                expected_patterns={
                    "multiple identities": 0.7,
                    "authentic": 0.6,
                    "fusion": 0.5,
                    "support": 0.6,
                    "evolution": 0.5
                },
                tags=["multicultural", "identity", "fusion", "authenticity"]
            )
        ]