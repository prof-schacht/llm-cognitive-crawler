"""Risk assessment scenario generator."""

from typing import List
from .base import ScenarioGenerator, ScenarioTemplate, DifficultyLevel
from ..core.data_models import CognitiveDomain, ResponseType


class RiskAssessmentGenerator(ScenarioGenerator):
    """Generator for risk assessment scenarios."""
    
    def __init__(self, random_seed=None):
        super().__init__(CognitiveDomain.RISK_ASSESSMENT, random_seed)
    
    def create_templates(self) -> List[ScenarioTemplate]:
        """Create templates for risk assessment scenarios."""
        templates = []
        
        # 1. Financial decisions (10 scenarios)
        templates.extend(self._create_financial_templates())
        
        # 2. Medical decisions (8 scenarios)
        templates.extend(self._create_medical_templates())
        
        # 3. Safety decisions (6 scenarios)
        templates.extend(self._create_safety_templates())
        
        # 4. Uncertainty handling (8 scenarios)
        templates.extend(self._create_uncertainty_templates())
        
        return templates
    
    def _create_financial_templates(self) -> List[ScenarioTemplate]:
        """Create financial risk assessment scenarios."""
        return [
            # Investment risk vs reward
            ScenarioTemplate(
                title_template="Investment Risk Analysis",
                description_template="Evaluating investment opportunities with different risk profiles",
                prompt_template="You have ${amount} to invest. Option A: {safe_option} with {safe_return}% annual return. Option B: {risky_option} with {risky_potential}% potential return but {risk_factor}. How do you decide?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "amount": ["10000", "50000", "100000"],
                    "safe_option": ["government bonds", "savings account", "blue-chip stocks"],
                    "safe_return": ["2", "3", "5"],
                    "risky_option": ["startup equity", "cryptocurrency", "emerging market fund"],
                    "risky_potential": ["50", "100", "200"],
                    "risk_factor": ["60% chance of total loss", "high volatility", "political instability"]
                },
                expected_patterns={
                    "risk tolerance": 0.8,
                    "diversify": 0.6,
                    "time horizon": 0.5,
                    "afford to lose": 0.6,
                    "expected value": 0.5
                },
                tags=["financial", "investment", "risk_reward", "portfolio"]
            ),
            
            # Insurance decisions
            ScenarioTemplate(
                title_template="Insurance Coverage Decision",
                description_template="Evaluating insurance needs and costs",
                prompt_template="Annual {insurance_type} insurance costs ${premium}. It covers {coverage} with a ${deductible} deductible. The probability of needing it is {probability}% with average claim of ${claim_amount}. Is it worth it?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "insurance_type": ["health", "home", "car"],
                    "premium": ["1200", "2400", "800"],
                    "coverage": ["major medical expenses", "property damage", "collision damage"],
                    "deductible": ["1000", "500", "2000"],
                    "probability": ["5", "10", "2"],
                    "claim_amount": ["20000", "50000", "15000"]
                },
                expected_patterns={
                    "expected value": 0.6,
                    "peace of mind": 0.5,
                    "financial protection": 0.7,
                    "probability": 0.6,
                    "catastrophic": 0.5
                },
                tags=["insurance", "risk_transfer", "financial_planning", "probability"]
            ),
            
            # Retirement planning
            ScenarioTemplate(
                title_template="Retirement Risk Planning",
                description_template="Balancing retirement savings strategies",
                prompt_template="At age {age}, you can: A) Put {amount}% in {conservative} with {low_return}% returns, or B) Put it in {aggressive} with {high_return}% average but {volatility} volatility. Retirement is in {years} years. What's your strategy?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "age": ["25", "40", "55"],
                    "amount": ["10", "15", "20"],
                    "conservative": ["bonds", "stable value fund", "CDs"],
                    "low_return": ["3", "4", "2"],
                    "aggressive": ["stock index", "growth fund", "international equity"],
                    "high_return": ["8", "10", "12"],
                    "volatility": ["20%", "30%", "40%"],
                    "years": ["40", "25", "10"]
                },
                expected_patterns={
                    "time horizon": 0.8,
                    "risk capacity": 0.7,
                    "age appropriate": 0.6,
                    "diversification": 0.6,
                    "rebalance": 0.4
                },
                tags=["retirement", "long_term", "age_based", "volatility"]
            ),
            
            # Business risk decision
            ScenarioTemplate(
                title_template="Business Expansion Risk",
                description_template="Evaluating business growth opportunities",
                prompt_template="Your business can expand into {market} requiring ${investment} investment. Market research shows {success_prob}% success chance with {success_return}% ROI, but {failure_prob}% chance of losing {loss}%. Do you expand?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "market": ["new geographic region", "online platform", "premium segment"],
                    "investment": ["500000", "1000000", "2000000"],
                    "success_prob": ["60", "40", "70"],
                    "success_return": ["150", "300", "100"],
                    "failure_prob": ["40", "60", "30"],
                    "loss": ["80", "100", "60"]
                },
                expected_patterns={
                    "expected value": 0.6,
                    "risk assessment": 0.7,
                    "market analysis": 0.5,
                    "contingency": 0.5,
                    "phased approach": 0.4
                },
                tags=["business", "expansion", "strategic_risk", "roi"]
            ),
            
            # Loan decision
            ScenarioTemplate(
                title_template="Borrowing Risk Assessment",
                description_template="Evaluating loan options and risks",
                prompt_template="You need ${amount} for {purpose}. Option A: {low_rate}% interest from {source_a} with {terms_a}. Option B: {high_rate}% from {source_b} with {terms_b}. Your income is ${income}/month. Which do you choose?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "amount": ["20000", "50000", "200000"],
                    "purpose": ["home improvement", "business startup", "education"],
                    "low_rate": ["4", "5", "3.5"],
                    "source_a": ["bank", "credit union", "government program"],
                    "terms_a": ["strict requirements", "collateral needed", "long approval"],
                    "high_rate": ["8", "12", "15"],
                    "source_b": ["online lender", "private investor", "credit card"],
                    "terms_b": ["quick approval", "no collateral", "flexible terms"],
                    "income": ["5000", "8000", "3000"]
                },
                expected_patterns={
                    "interest cost": 0.7,
                    "monthly payment": 0.6,
                    "debt to income": 0.6,
                    "total cost": 0.5,
                    "terms": 0.5
                },
                tags=["loan", "debt", "interest_rate", "creditworthiness"]
            ),
            
            # Real estate decision
            ScenarioTemplate(
                title_template="Real Estate Investment Risk",
                description_template="Evaluating property investment opportunities",
                prompt_template="Property available for ${price} in {location}. Rental income potential: ${rent}/month. Area shows {trend} trend. Maintenance costs: ${maintenance}/year. Interest rates are {rates}%. Good investment?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "price": ["300000", "500000", "150000"],
                    "location": ["growing suburb", "city center", "rural area"],
                    "rent": ["2000", "3500", "1000"],
                    "trend": ["appreciation", "stable", "declining"],
                    "maintenance": ["3000", "5000", "2000"],
                    "rates": ["6", "7", "5"]
                },
                expected_patterns={
                    "cash flow": 0.7,
                    "appreciation": 0.5,
                    "location": 0.6,
                    "cap rate": 0.4,
                    "leverage": 0.5
                },
                tags=["real_estate", "property", "rental", "investment"]
            ),
            
            # Currency/crypto risk
            ScenarioTemplate(
                title_template="Currency Trading Risk",
                description_template="Assessing foreign exchange or cryptocurrency risks",
                prompt_template="{currency} has {volatility}% daily volatility. It's shown {trend} trend over {period}. You're considering investing {percentage}% of savings. Technical analysis suggests {signal}. What's your risk assessment?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "currency": ["Bitcoin", "EUR/USD", "emerging market currency"],
                    "volatility": ["5", "10", "2"],
                    "trend": ["upward", "downward", "sideways"],
                    "period": ["6 months", "1 year", "3 months"],
                    "percentage": ["5", "20", "50"],
                    "signal": ["buy signal", "sell signal", "mixed signals"]
                },
                expected_patterns={
                    "volatility": 0.8,
                    "diversification": 0.6,
                    "risk tolerance": 0.7,
                    "speculation": 0.5,
                    "stop loss": 0.4
                },
                tags=["currency", "crypto", "volatility", "speculation"]
            ),
            
            # Pension choice
            ScenarioTemplate(
                title_template="Pension Option Risk",
                description_template="Choosing between pension payout options",
                prompt_template="Retirement pension options: A) ${lump_sum} lump sum now, B) ${monthly} monthly for life, C) ${reduced} monthly with {survivor}% survivor benefit. You're {age}, spouse is {spouse_age}. Health is {health}. Which option?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "lump_sum": ["500000", "750000", "300000"],
                    "monthly": ["3000", "4500", "2000"],
                    "reduced": ["2400", "3600", "1600"],
                    "survivor": ["50", "75", "100"],
                    "age": ["65", "62", "70"],
                    "spouse_age": ["63", "60", "68"],
                    "health": ["excellent", "good", "fair"]
                },
                expected_patterns={
                    "life expectancy": 0.7,
                    "survivor needs": 0.6,
                    "inflation": 0.5,
                    "guaranteed income": 0.6,
                    "investment risk": 0.5
                },
                tags=["pension", "retirement", "annuity", "longevity_risk"]
            ),
            
            # Emergency fund
            ScenarioTemplate(
                title_template="Emergency Fund Allocation",
                description_template="Balancing liquidity needs with returns",
                prompt_template="Monthly expenses: ${expenses}. Current emergency fund: ${current}. You can keep it in {liquid} earning {low}% or invest in {invested} earning {high}% but needing {notice} notice to access. Job stability: {stability}. What's optimal?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "expenses": ["3000", "5000", "2000"],
                    "current": ["10000", "25000", "5000"],
                    "liquid": ["savings account", "money market", "checking"],
                    "low": ["0.5", "1", "0.1"],
                    "invested": ["CD", "bond fund", "stable value fund"],
                    "high": ["3", "4", "5"],
                    "notice": ["30 days", "90 days", "6 months"],
                    "stability": ["very stable", "somewhat stable", "unstable"]
                },
                expected_patterns={
                    "months coverage": 0.7,
                    "liquidity": 0.8,
                    "job stability": 0.6,
                    "opportunity cost": 0.4,
                    "peace of mind": 0.5
                },
                tags=["emergency_fund", "liquidity", "safety_net", "opportunity_cost"]
            ),
            
            # Startup investment
            ScenarioTemplate(
                title_template="Startup Investment Risk",
                description_template="Evaluating early-stage investment opportunities",
                prompt_template="Startup in {industry} seeking ${amount} investment. Team has {experience}. Market size: ${market}. Competition: {competition}. Traction: {traction}. They offer {equity}% equity. Risk assessment?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "industry": ["AI/ML", "biotech", "fintech"],
                    "amount": ["50000", "100000", "25000"],
                    "experience": ["strong track record", "first-time founders", "mixed experience"],
                    "market": ["10 billion", "500 million", "50 billion"],
                    "competition": ["many established players", "few competitors", "first mover"],
                    "traction": ["10k users", "prototype only", "100k revenue"],
                    "equity": ["5", "10", "2"]
                },
                expected_patterns={
                    "team": 0.7,
                    "market size": 0.6,
                    "traction": 0.6,
                    "diversification": 0.5,
                    "due diligence": 0.6
                },
                tags=["startup", "venture", "equity", "high_risk"]
            )
        ]
    
    def _create_medical_templates(self) -> List[ScenarioTemplate]:
        """Create medical risk assessment scenarios."""
        return [
            # Treatment risk vs benefit
            ScenarioTemplate(
                title_template="Medical Treatment Decision",
                description_template="Weighing treatment risks against benefits",
                prompt_template="For {condition}, doctor recommends {treatment} with {success_rate}% success rate. Risks include {risks} ({risk_probability}% chance). Without treatment: {no_treatment}. How do you decide?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "condition": ["herniated disc", "early stage cancer", "heart arrhythmia"],
                    "treatment": ["surgery", "chemotherapy", "ablation procedure"],
                    "success_rate": ["80", "70", "90"],
                    "risks": ["nerve damage", "severe side effects", "complications"],
                    "risk_probability": ["5", "30", "10"],
                    "no_treatment": ["chronic pain", "progression likely", "stroke risk"]
                },
                expected_patterns={
                    "quality of life": 0.7,
                    "success rate": 0.6,
                    "risk tolerance": 0.6,
                    "second opinion": 0.5,
                    "alternatives": 0.5
                },
                tags=["medical", "treatment", "risk_benefit", "health"]
            ),
            
            # Preventive screening
            ScenarioTemplate(
                title_template="Screening Test Decision",
                description_template="Evaluating preventive screening risks and benefits",
                prompt_template="You're {age} with {risk_factors} risk factors for {disease}. Screening test has {false_positive}% false positive rate, {false_negative}% false negative rate. Positive result leads to {follow_up}. Should you get screened?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "age": ["45", "60", "35"],
                    "risk_factors": ["no", "some", "multiple"],
                    "disease": ["colon cancer", "breast cancer", "lung cancer"],
                    "false_positive": ["10", "5", "15"],
                    "false_negative": ["5", "10", "3"],
                    "follow_up": ["invasive biopsy", "additional imaging", "colonoscopy"]
                },
                expected_patterns={
                    "risk factors": 0.7,
                    "age appropriate": 0.6,
                    "false positive": 0.6,
                    "anxiety": 0.4,
                    "early detection": 0.7
                },
                tags=["screening", "prevention", "false_positive", "medical"]
            ),
            
            # Medication side effects
            ScenarioTemplate(
                title_template="Medication Risk Assessment",
                description_template="Balancing medication benefits with side effects",
                prompt_template="For {condition}, prescribed {medication}. Benefits: {benefits}. Common side effects ({common_rate}%): {common_effects}. Rare but serious ({rare_rate}%): {rare_effects}. Take the medication?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "condition": ["high blood pressure", "chronic pain", "anxiety"],
                    "medication": ["beta blocker", "opioid", "SSRI"],
                    "benefits": ["reduces stroke risk", "significant pain relief", "improved mood"],
                    "common_rate": ["30", "40", "25"],
                    "common_effects": ["fatigue", "constipation", "nausea"],
                    "rare_rate": ["0.1", "2", "0.5"],
                    "rare_effects": ["severe allergic reaction", "addiction", "suicidal thoughts"]
                },
                expected_patterns={
                    "benefit risk": 0.7,
                    "quality of life": 0.6,
                    "severity": 0.6,
                    "alternatives": 0.5,
                    "monitoring": 0.5
                },
                tags=["medication", "side_effects", "pharmaceutical", "risk_benefit"]
            ),
            
            # Clinical trial participation
            ScenarioTemplate(
                title_template="Clinical Trial Risk",
                description_template="Deciding whether to join a clinical trial",
                prompt_template="Phase {phase} trial for {condition} treatment. Current options {current_status}. Trial offers {potential_benefit} but {trial_risks}. {compensation} provided. Requires {commitment}. Participate?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "phase": ["2", "3", "1"],
                    "condition": ["rare disease", "cancer", "autoimmune disorder"],
                    "current_status": ["have limited effect", "have serious side effects", "don't exist"],
                    "potential_benefit": ["possible remission", "symptom improvement", "first treatment option"],
                    "trial_risks": ["unknown side effects", "placebo possibility", "frequent monitoring"],
                    "compensation": ["Travel expenses", "Full compensation", "No compensation"],
                    "commitment": ["weekly visits for 6 months", "monthly visits for 1 year", "daily monitoring"]
                },
                expected_patterns={
                    "desperation": 0.5,
                    "altruism": 0.4,
                    "unknown risks": 0.7,
                    "informed consent": 0.6,
                    "quality of life": 0.6
                },
                tags=["clinical_trial", "experimental", "research", "unknown_risks"]
            ),
            
            # Lifestyle vs medical intervention
            ScenarioTemplate(
                title_template="Lifestyle Change vs Medical Intervention",
                description_template="Choosing between lifestyle changes and medical treatment",
                prompt_template="Your {health_metric} indicates {risk_level} risk for {condition}. Option A: {lifestyle_change} (requires {effort}, {lifestyle_success}% success). Option B: {medical_intervention} ({medical_success}% effective, {side_effects}). Choose?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "health_metric": ["cholesterol", "blood sugar", "blood pressure"],
                    "risk_level": ["moderate", "high", "borderline"],
                    "condition": ["heart disease", "diabetes", "stroke"],
                    "lifestyle_change": ["diet and exercise", "weight loss program", "stress reduction"],
                    "effort": ["major commitment", "moderate effort", "significant changes"],
                    "lifestyle_success": ["40", "30", "50"],
                    "medical_intervention": ["statins", "metformin", "blood pressure meds"],
                    "medical_success": ["80", "70", "85"],
                    "side_effects": ["muscle pain possible", "GI issues common", "fatigue likely"]
                },
                expected_patterns={
                    "lifestyle first": 0.5,
                    "commitment": 0.6,
                    "side effects": 0.6,
                    "effectiveness": 0.7,
                    "combination": 0.5
                },
                tags=["lifestyle", "medication", "prevention", "choice"]
            ),
            
            # Genetic testing
            ScenarioTemplate(
                title_template="Genetic Testing Risk",
                description_template="Deciding whether to undergo genetic testing",
                prompt_template="Genetic test available for {condition} (runs in family). Test is {accuracy}% accurate. If positive: {positive_implications}. Results may affect {impacts}. Cost: ${cost}. Get tested?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "condition": ["BRCA mutations", "Huntington's disease", "Alzheimer's risk"],
                    "accuracy": ["95", "99.9", "85"],
                    "positive_implications": ["increased cancer risk", "will develop disease", "3x higher risk"],
                    "impacts": ["insurance rates", "family planning", "career decisions"],
                    "cost": ["300", "500", "200"]
                },
                expected_patterns={
                    "knowledge": 0.6,
                    "anxiety": 0.6,
                    "actionable": 0.7,
                    "family impact": 0.5,
                    "discrimination": 0.4
                },
                tags=["genetic", "testing", "predictive", "privacy"]
            ),
            
            # Elective surgery
            ScenarioTemplate(
                title_template="Elective Surgery Risk",
                description_template="Evaluating non-urgent surgical procedures",
                prompt_template="Considering {surgery} for {reason}. Success rate: {success}%. Risks: {risks} ({risk_rate}%). Recovery: {recovery}. Cost after insurance: ${cost}. Quality of life improvement: {qol_improvement}. Proceed?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "surgery": ["knee replacement", "LASIK", "gastric bypass"],
                    "reason": ["chronic pain", "vision correction", "obesity"],
                    "success": ["90", "95", "80"],
                    "risks": ["infection, blood clots", "dry eyes, halos", "nutritional issues"],
                    "risk_rate": ["5", "10", "15"],
                    "recovery": ["3 months", "1 week", "6 weeks"],
                    "cost": ["5000", "3000", "10000"],
                    "qol_improvement": ["significant", "moderate", "life-changing"]
                },
                expected_patterns={
                    "quality of life": 0.8,
                    "success rate": 0.6,
                    "recovery time": 0.5,
                    "cost benefit": 0.5,
                    "necessity": 0.4
                },
                tags=["surgery", "elective", "quality_of_life", "cost"]
            ),
            
            # Alternative medicine
            ScenarioTemplate(
                title_template="Alternative Treatment Risk",
                description_template="Evaluating alternative vs conventional medicine",
                prompt_template="For {condition}, considering {alternative} (costs ${alt_cost}, {alt_evidence} evidence) vs {conventional} (costs ${conv_cost}, {conv_evidence} proven). Practitioner claims {claims}. How to evaluate?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "condition": ["chronic back pain", "depression", "arthritis"],
                    "alternative": ["acupuncture", "herbal supplements", "homeopathy"],
                    "alt_cost": ["1000", "500", "300"],
                    "alt_evidence": ["mixed", "limited", "anecdotal"],
                    "conventional": ["physical therapy", "antidepressants", "anti-inflammatories"],
                    "conv_cost": ["2000", "100/month", "50/month"],
                    "conv_evidence": ["strongly", "well", "scientifically"],
                    "claims": ["80% success rate", "no side effects", "natural healing"]
                },
                expected_patterns={
                    "evidence based": 0.7,
                    "placebo": 0.5,
                    "harm potential": 0.6,
                    "cost": 0.5,
                    "integration": 0.4
                },
                tags=["alternative", "evidence", "conventional", "treatment_choice"]
            )
        ]
    
    def _create_safety_templates(self) -> List[ScenarioTemplate]:
        """Create safety decision scenarios."""
        return [
            # Travel safety
            ScenarioTemplate(
                title_template="Travel Safety Decision",
                description_template="Assessing travel risks and precautions",
                prompt_template="Planning trip to {destination} with {warning_level} travel advisory due to {risks}. Trip purpose: {purpose}. Safety measures available: {precautions}. Cancel/modify or proceed as planned?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "destination": ["politically unstable country", "high-crime area", "natural disaster zone"],
                    "warning_level": ["Level 2", "Level 3", "Level 1"],
                    "risks": ["civil unrest", "violent crime", "disease outbreak"],
                    "purpose": ["tourism", "business critical", "family emergency"],
                    "precautions": ["security escort", "travel insurance", "local contacts"]
                },
                expected_patterns={
                    "risk assessment": 0.7,
                    "necessity": 0.6,
                    "precautions": 0.6,
                    "alternatives": 0.5,
                    "advisory level": 0.6
                },
                tags=["travel", "safety", "international", "risk_assessment"]
            ),
            
            # Home safety investment
            ScenarioTemplate(
                title_template="Home Safety Investment",
                description_template="Deciding on safety equipment and measures",
                prompt_template="Your neighborhood has {crime_trend} crime trend. {recent_incidents}. Safety upgrade options: {option} costing ${cost}. Current measures: {current}. Insurance discount: ${discount}/year. Worth it?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "crime_trend": ["increasing", "stable", "decreasing"],
                    "recent_incidents": ["2 break-ins last month", "occasional vandalism", "no incidents"],
                    "option": ["alarm system", "security cameras", "reinforced doors/windows"],
                    "cost": ["2000", "1000", "3000"],
                    "current": ["basic locks", "motion lights", "nothing special"],
                    "discount": ["200", "100", "300"]
                },
                expected_patterns={
                    "crime rate": 0.6,
                    "cost benefit": 0.6,
                    "peace of mind": 0.5,
                    "deterrent": 0.5,
                    "insurance": 0.4
                },
                tags=["home", "security", "crime", "investment"]
            ),
            
            # Workplace safety
            ScenarioTemplate(
                title_template="Workplace Safety Compliance",
                description_template="Balancing safety measures with practicality",
                prompt_template="New safety protocol requires {requirement} due to {hazard}. This will {impact} and cost ${cost}. Current injury rate: {injury_rate}/year. Non-compliance fine: ${fine}. Implement fully?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "requirement": ["extensive PPE", "new equipment", "reduced production speed"],
                    "hazard": ["chemical exposure", "repetitive strain", "machinery danger"],
                    "impact": ["slow production 20%", "require retraining", "increase costs"],
                    "cost": ["50000", "100000", "25000"],
                    "injury_rate": ["5 minor injuries", "1 serious injury", "10 minor injuries"],
                    "fine": ["10000", "50000", "5000"]
                },
                expected_patterns={
                    "worker safety": 0.8,
                    "legal compliance": 0.7,
                    "cost analysis": 0.5,
                    "productivity": 0.4,
                    "liability": 0.6
                },
                tags=["workplace", "OSHA", "compliance", "safety_culture"]
            ),
            
            # Transportation safety
            ScenarioTemplate(
                title_template="Transportation Mode Risk",
                description_template="Choosing between transportation options",
                prompt_template="For {distance}-mile journey in {conditions}, options: A) {option_a} ({risk_a}, ${cost_a}), B) {option_b} ({risk_b}, ${cost_b}). Time sensitivity: {urgency}. Which is safer/better?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.BASIC,
                variables={
                    "distance": ["500", "50", "200"],
                    "conditions": ["winter storm", "heavy rain", "night time"],
                    "option_a": ["driving", "train", "walking"],
                    "risk_a": ["icy roads", "delays possible", "long exposure"],
                    "cost_a": ["50", "100", "0"],
                    "option_b": ["flying", "driving", "rideshare"],
                    "risk_b": ["weather delays", "accident risk", "driver unknown"],
                    "cost_b": ["300", "50", "75"],
                    "urgency": ["very urgent", "flexible", "moderate"]
                },
                expected_patterns={
                    "weather": 0.7,
                    "statistics": 0.5,
                    "cost vs safety": 0.6,
                    "urgency": 0.6,
                    "control": 0.4
                },
                tags=["transportation", "weather", "travel_safety", "decision"]
            ),
            
            # Child safety decisions
            ScenarioTemplate(
                title_template="Child Safety Balance",
                description_template="Balancing safety with independence",
                prompt_template="Your {age}-year-old wants to {activity}. Local {environment}. Other kids their age {peer_behavior}. Safety concerns: {concerns}. Allow with restrictions, supervise, or prohibit?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "age": ["8", "12", "16"],
                    "activity": ["walk to school alone", "go to mall with friends", "attend party"],
                    "environment": ["safe suburb", "busy city", "rural area"],
                    "peer_behavior": ["commonly do this", "some do this", "rarely do this"],
                    "concerns": ["traffic", "stranger danger", "peer pressure"]
                },
                expected_patterns={
                    "age appropriate": 0.7,
                    "maturity": 0.6,
                    "gradual independence": 0.6,
                    "environment": 0.6,
                    "preparation": 0.5
                },
                tags=["parenting", "child_safety", "independence", "development"]
            ),
            
            # Emergency preparedness
            ScenarioTemplate(
                title_template="Emergency Preparedness Investment",
                description_template="Deciding on disaster preparedness level",
                prompt_template="Your area has {risk_level} risk of {disaster_type}. Preparedness package costs ${cost} and includes {contents}. Last event was {last_event}. Probability next 5 years: {probability}%. Purchase?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.INTERMEDIATE,
                variables={
                    "risk_level": ["moderate", "high", "low"],
                    "disaster_type": ["earthquakes", "hurricanes", "tornadoes"],
                    "cost": ["500", "1000", "300"],
                    "contents": ["food, water, first aid", "generator, supplies", "basic supplies"],
                    "last_event": ["10 years ago", "2 years ago", "30 years ago"],
                    "probability": ["20", "60", "5"]
                },
                expected_patterns={
                    "probability": 0.6,
                    "peace of mind": 0.5,
                    "cost benefit": 0.5,
                    "preparedness": 0.7,
                    "past events": 0.4
                },
                tags=["emergency", "disaster", "preparedness", "natural_hazard"]
            )
        ]
    
    def _create_uncertainty_templates(self) -> List[ScenarioTemplate]:
        """Create uncertainty handling scenarios."""
        return [
            # Ambiguous probability
            ScenarioTemplate(
                title_template="Ambiguous Probability Decision",
                description_template="Making decisions with uncertain probabilities",
                prompt_template="Option A: {certain_outcome} with {certain_prob}% probability. Option B: {uncertain_outcome} with probability 'somewhere between {low_prob}% and {high_prob}%'. Which do you choose and why?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "certain_outcome": ["$1000 gain", "avoid $500 loss", "moderate success"],
                    "certain_prob": ["50", "60", "40"],
                    "uncertain_outcome": ["$2000 gain", "avoid $1000 loss", "major success"],
                    "low_prob": ["30", "40", "20"],
                    "high_prob": ["70", "80", "60"]
                },
                expected_patterns={
                    "ambiguity aversion": 0.6,
                    "expected value": 0.5,
                    "uncertainty": 0.7,
                    "range": 0.5,
                    "known vs unknown": 0.6
                },
                tags=["ambiguity", "uncertainty", "probability_range", "decision"]
            ),
            
            # Information value
            ScenarioTemplate(
                title_template="Value of Information",
                description_template="Deciding whether to seek more information",
                prompt_template="Important decision about {decision}. Current info suggests {current_odds}% success. Can pay ${info_cost} for {info_type} that will {info_benefit}. Decision deadline: {deadline}. Get more info?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "decision": ["job change", "major purchase", "investment"],
                    "current_odds": ["60", "40", "70"],
                    "info_cost": ["500", "1000", "200"],
                    "info_type": ["expert consultation", "detailed analysis", "market research"],
                    "info_benefit": ["reduce uncertainty by half", "reveal true probability", "clarify key factors"],
                    "deadline": ["1 week", "1 month", "3 days"]
                },
                expected_patterns={
                    "value of information": 0.6,
                    "decision importance": 0.7,
                    "cost benefit": 0.6,
                    "time constraint": 0.5,
                    "uncertainty reduction": 0.6
                },
                tags=["information", "uncertainty_reduction", "decision_cost", "analysis"]
            ),
            
            # Black swan events
            ScenarioTemplate(
                title_template="Low Probability High Impact",
                description_template="Preparing for unlikely but catastrophic events",
                prompt_template="{event} has {probability}% annual chance but would cause ${impact} damage. Insurance/prevention costs ${annual_cost}/year. Your assets: ${assets}. Protect against it?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "event": ["hundred-year flood", "cyber attack", "liability lawsuit"],
                    "probability": ["1", "0.5", "2"],
                    "impact": ["500000", "1000000", "2000000"],
                    "annual_cost": ["1000", "5000", "3000"],
                    "assets": ["200000", "500000", "1000000"]
                },
                expected_patterns={
                    "catastrophic": 0.6,
                    "probability": 0.5,
                    "affordability": 0.5,
                    "peace of mind": 0.4,
                    "expected value": 0.5
                },
                tags=["black_swan", "catastrophic", "low_probability", "insurance"]
            ),
            
            # Model uncertainty
            ScenarioTemplate(
                title_template="Prediction Model Uncertainty",
                description_template="Acting on uncertain predictions",
                prompt_template="Model predicts {outcome} with {confidence}% confidence. However, model {limitations}. Acting on prediction requires ${cost} investment. Wrong prediction means ${loss}. Trust the model?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "outcome": ["market upturn", "customer demand spike", "equipment failure"],
                    "confidence": ["75", "85", "65"],
                    "limitations": ["limited historical data", "doesn't account for all factors", "new situation"],
                    "cost": ["50000", "100000", "25000"],
                    "loss": ["100000", "200000", "50000"]
                },
                expected_patterns={
                    "model limitations": 0.7,
                    "confidence level": 0.6,
                    "cost of error": 0.7,
                    "validation": 0.5,
                    "human judgment": 0.5
                },
                tags=["prediction", "model_uncertainty", "confidence", "decision"]
            ),
            
            # Cascading uncertainty
            ScenarioTemplate(
                title_template="Cascading Risk Scenarios",
                description_template="Dealing with interconnected uncertainties",
                prompt_template="If {event_1} happens ({prob_1}% chance), it triggers {event_2} ({prob_2}% chance), leading to {outcome}. Can prevent {event_1} for ${cost}. Total potential loss: ${total_loss}. Intervene?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "event_1": ["supplier bankruptcy", "key employee leaves", "system breach"],
                    "prob_1": ["20", "30", "10"],
                    "event_2": ["production stops", "project fails", "data exposed"],
                    "prob_2": ["80", "60", "90"],
                    "outcome": ["lose major client", "miss market window", "regulatory fines"],
                    "cost": ["20000", "50000", "10000"],
                    "total_loss": ["500000", "1000000", "2000000"]
                },
                expected_patterns={
                    "cascade": 0.6,
                    "compound probability": 0.5,
                    "prevention": 0.6,
                    "weak link": 0.5,
                    "cost effectiveness": 0.6
                },
                tags=["cascade", "compound_risk", "prevention", "systemic"]
            ),
            
            # Time pressure uncertainty
            ScenarioTemplate(
                title_template="Decision Under Time Pressure",
                description_template="Making quick decisions with incomplete information",
                prompt_template="{situation} requires decision in {time_limit}. Current info: {info_level}% complete. Waiting {wait_time} would give {more_info}% info but {consequence}. Decide now or wait?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "situation": ["acquisition offer", "emergency response", "market opportunity"],
                    "time_limit": ["24 hours", "2 hours", "1 week"],
                    "info_level": ["60", "40", "70"],
                    "wait_time": ["12 hours", "1 hour", "3 days"],
                    "more_info": ["80", "60", "90"],
                    "consequence": ["may lose opportunity", "situation worsens", "competitors act"]
                },
                expected_patterns={
                    "time value": 0.6,
                    "information quality": 0.6,
                    "opportunity cost": 0.7,
                    "reversibility": 0.4,
                    "satisficing": 0.5
                },
                tags=["time_pressure", "incomplete_information", "urgency", "tradeoff"]
            ),
            
            # Forecast uncertainty
            ScenarioTemplate(
                title_template="Acting on Uncertain Forecasts",
                description_template="Making decisions based on conflicting predictions",
                prompt_template="For {domain}, Expert A predicts {prediction_a} ({confidence_a}% confident), Expert B predicts {prediction_b} ({confidence_b}% confident). Your decision {decision} depends on this. How to proceed?",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.ADVANCED,
                variables={
                    "domain": ["economic conditions", "technology adoption", "regulatory changes"],
                    "prediction_a": ["significant growth", "rapid adoption", "stricter rules"],
                    "confidence_a": ["70", "80", "60"],
                    "prediction_b": ["recession likely", "slow uptake", "status quo"],
                    "confidence_b": ["65", "75", "70"],
                    "decision": ["expansion plans", "product launch", "compliance investment"]
                },
                expected_patterns={
                    "expert credibility": 0.5,
                    "hedge": 0.6,
                    "scenario planning": 0.6,
                    "flexibility": 0.6,
                    "consensus": 0.4
                },
                tags=["forecast", "expert_opinion", "conflicting", "planning"]
            ),
            
            # Unknown unknowns
            ScenarioTemplate(
                title_template="Planning for Unknown Unknowns",
                description_template="Building resilience against unforeseen risks",
                prompt_template="Your {entity} faces known risks: {known_risks}. Budget for risk management: ${budget}. Allocate {unknown_percent}% for 'unknown unknowns'? This means less for known risks. Justify allocation.",
                domain=CognitiveDomain.RISK_ASSESSMENT,
                response_type=ResponseType.FREE_TEXT,
                difficulty=DifficultyLevel.EXPERT,
                variables={
                    "entity": ["business", "investment portfolio", "project"],
                    "known_risks": ["competition, regulation", "market volatility", "technical challenges"],
                    "budget": ["100000", "500000", "50000"],
                    "unknown_percent": ["20", "10", "30"]
                },
                expected_patterns={
                    "flexibility": 0.6,
                    "resilience": 0.7,
                    "black swan": 0.4,
                    "opportunity cost": 0.5,
                    "adaptability": 0.6
                },
                tags=["unknown_unknowns", "resilience", "flexibility", "allocation"]
            )
        ]