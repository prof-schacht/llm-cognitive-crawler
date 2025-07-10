# LLM Cognitive Crawler 🧠🔍

**Bayesian Inverse Planning for Reverse Engineering LLM Mental Models and Cognitive Patterns**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Research](https://img.shields.io/badge/Status-Research-orange.svg)]()

## 🎯 Research Objective

This project develops a novel approach to **systematically reverse-engineer the cognitive patterns and mental models of Large Language Models (LLMs)** using Bayesian inverse planning. Instead of treating LLMs as black boxes, we aim to build detailed "cognitive profiles" that reveal how these models reason, make decisions, and exhibit biases.

## 🧭 Core Research Questions

1. **Can we infer LLM "mental models" from response patterns?** 
   - Use Bayesian inverse planning to work backwards from outputs to internal reasoning patterns

2. **How do different LLMs compare cognitively?**
   - Create systematic cognitive fingerprints for model comparison and selection

3. **What cognitive biases and blindspots exist?**
   - Detect harmful biases and reasoning failures before deployment

4. **Can we predict model behavior in novel situations?**
   - Build predictive models of LLM reasoning across domains

## 🔬 Research Methodology

### Theoretical Foundation: Bayesian Inverse Planning

Traditional approach: **Mental State → Actions** (forward planning)
Our approach: **Observed Actions → Inferred Mental State** (inverse planning)

```
P(Mental Model | Response) ∝ P(Response | Mental Model) × P(Mental Model)
```

Where:
- **Mental Model**: Hypotheses about reasoning patterns (utilitarian, cautious, rule-based, etc.)
- **Response**: Observed LLM outputs to structured scenarios
- **Bayesian Update**: Systematically refine beliefs about cognitive patterns

### Research Pipeline

```
Design Probing → Generate Cognitive → Query LLM → Classify → Bayesian → Profile → Validation
Scenarios        Hypotheses         Scenarios    Responses   Update    Analysis   Testing
```

## 🧪 Experimental Design

### Phase 1: Cognitive Dimension Mapping
Systematic probing across key cognitive domains:

| Domain | Scenarios | Target Patterns |
|--------|-----------|----------------|
| **Ethical Reasoning** | Trolley problems, fairness dilemmas | Utilitarian vs. Deontological vs. Virtue ethics |
| **Logical Reasoning** | Syllogisms, probability puzzles | Formal logic vs. Heuristic reasoning |
| **Risk Assessment** | Financial choices, uncertainty | Risk-averse vs. Risk-seeking vs. Optimizing |
| **Social Cognition** | Theory of mind, cultural scenarios | Empathetic vs. Analytical social reasoning |
| **Causal Reasoning** | Scientific thinking, counterfactuals | Mechanistic vs. Correlational reasoning |

### Phase 2: Cognitive Hypothesis Framework
Generate structured hypotheses about LLM reasoning patterns:

**Example Cognitive Hypotheses:**
- **Utilitarian Reasoner**: Maximizes outcomes, ignores rules (P=0.7 for pulling trolley lever)
- **Cautious Reasoner**: Seeks information, expresses uncertainty (P=0.6 for "need more info")
- **Rule-Based Reasoner**: Follows principles over consequences (P=0.1 for rule violations)
- **Optimistic Bias**: Overestimates positive outcomes (P=0.7 for risky choices with upside)

### Phase 3: Multi-Model Comparative Analysis
Compare cognitive patterns across different LLMs:
- GPT-4, Claude-3, LLaMA-2, Gemma, Mixtral
- Domain-specific reasoning differences
- Bias detection and quantification
- Capability profiling and recommendations

## 🛠️ Technical Architecture

### Core Components

```python
# Main System Architecture
class LLMCognitiveCrawler:
    - scenario_generator: Creates systematic probing tests
    - hypothesis_framework: Defines cognitive pattern hypotheses  
    - llm_interface: Queries target LLMs
    - response_classifier: Categorizes LLM outputs
    - bayesian_engine: Updates beliefs using inverse planning
    - profile_analyzer: Generates cognitive insights
```

### Key Features
- **Scenario Generation**: 500+ carefully designed cognitive probes
- **Response Classification**: NLP-based categorization of LLM outputs
- **Bayesian Inference**: Principled belief updating over cognitive hypotheses
- **Visualization Tools**: Interactive cognitive profile plotting
- **Multi-Model Support**: Parallel analysis across different LLMs
- **Temporal Tracking**: Monitor cognitive consistency over time

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/prof-schacht/llm-cognitive-crawler.git
cd llm-cognitive-crawler

# Install dependencies
pip install -r requirements.txt

# Set up API keys (see config/api_keys.example.env)
cp config/api_keys.example.env config/api_keys.env
# Edit config/api_keys.env with your LLM API keys
```

### Basic Usage
```python
from llm_cognitive_crawler import LLMCognitiveCrawler
from scenario_generators import EthicalScenarios, ReasoningScenarios
from hypothesis_generators import ReasoningStyleHypotheses

# Initialize crawler
crawler = LLMCognitiveCrawler("gpt-4")

# Add probing scenarios
crawler.add_scenarios(EthicalScenarios.generate_all())
crawler.add_scenarios(ReasoningScenarios.generate_all())

# Add cognitive hypotheses
crawler.add_hypotheses(ReasoningStyleHypotheses.generate_all())

# Run analysis
results = crawler.run_comprehensive_analysis()

# Generate cognitive profile
profile = crawler.generate_cognitive_profile()
print(f"Dominant reasoning pattern: {profile.dominant_pattern}")
print(f"Confidence: {profile.confidence}")
```

## 📊 Expected Outcomes

### 1. Cognitive Fingerprinting
Create unique "cognitive fingerprints" for each LLM:
```python
gpt4_profile = {
    "utilitarian_reasoning": 0.72,
    "risk_aversion": 0.45, 
    "uncertainty_tolerance": 0.83,
    "rule_following": 0.38,
    "empathy_bias": 0.67
}
```

### 2. Bias Detection Dashboard
Systematic identification of problematic patterns:
- Gender bias in professional scenarios
- Cultural bias in moral reasoning
- Age bias in resource allocation
- Socioeconomic bias in fairness judgments

### 3. Model Selection Framework
Data-driven recommendations for model deployment:
- "Use Claude-3 for ethical AI applications (high deontological reasoning)"
- "Use GPT-4 for analytical tasks (high logical consistency)"
- "Avoid Model-X for financial advice (exhibits optimism bias)"

### 4. Predictive Cognitive Models
Predict LLM behavior in novel situations based on cognitive profile.

## 🔬 Research Validation

### Validation Strategy
1. **Human Baseline Comparison**: Compare LLM cognitive patterns with human reasoning studies
2. **Cross-Validation**: Test cognitive predictions on held-out scenarios
3. **Expert Review**: Cognitive scientists validate hypothesis framework
4. **Behavioral Prediction**: Test if profiles predict real-world usage patterns
5. **Adversarial Testing**: Probe robustness of cognitive assessments

### Success Metrics
- **Predictive Accuracy**: >80% accuracy in predicting responses to novel scenarios
- **Inter-Model Discrimination**: Clear cognitive differences between models
- **Bias Detection**: Identify known biases with >90% sensitivity
- **Human Alignment**: Cognitive patterns correlate with human expert assessments

## 🌟 Research Impact & Applications

### AI Safety & Alignment
- **Pre-deployment screening**: Identify harmful reasoning patterns before release
- **Alignment assessment**: Quantify adherence to human values
- **Robustness testing**: Find cognitive vulnerabilities and edge cases

### Model Development
- **Cognitive fine-tuning**: Train models to exhibit desired reasoning patterns
- **Bias mitigation**: Targeted interventions for specific cognitive biases
- **Capability assessment**: Systematic evaluation of reasoning abilities

### AI Governance & Policy
- **Regulatory compliance**: Standardized cognitive assessment frameworks
- **Transparency requirements**: Explainable AI through cognitive profiling
- **Risk assessment**: Quantified cognitive risk metrics for different applications

## 📚 Research Timeline

### Phase 1: Foundation (Months 1-3)
- [ ] Core architecture implementation
- [ ] Basic scenario and hypothesis frameworks
- [ ] Proof-of-concept with 2-3 models

### Phase 2: Expansion (Months 4-6)
- [ ] Comprehensive scenario database (500+ scenarios)
- [ ] Multi-model comparative analysis
- [ ] Advanced visualization and analysis tools

### Phase 3: Validation (Months 7-9)
- [ ] Human baseline studies
- [ ] Expert validation of cognitive hypotheses
- [ ] Predictive model validation

### Phase 4: Applications (Months 10-12)
- [ ] Bias detection applications
- [ ] Model selection frameworks
- [ ] Safety assessment tools

## 🤝 Contributing

We welcome contributions from researchers in:
- **Cognitive Science**: Expertise in human reasoning patterns
- **AI Safety**: Experience with model evaluation and alignment
- **Machine Learning**: Technical implementation and optimization
- **Philosophy**: Theoretical frameworks for reasoning and ethics
- **Psychology**: Experimental design and validation methodologies

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Principal Investigator**: [Prof. Schacht](https://github.com/prof-schacht)

For research collaborations, questions, or suggestions:
- 📧 Email: [Create an issue](https://github.com/prof-schacht/llm-cognitive-crawler/issues/new)
- 💬 Discussions: [GitHub Discussions](https://github.com/prof-schacht/llm-cognitive-crawler/discussions)

## 📖 Citation

If you use this work in your research, please cite:

```bibtex
@misc{schacht2024llmcognitivecrawler,
  title={LLM Cognitive Crawler: Bayesian Inverse Planning for Reverse Engineering AI Mental Models},
  author={Schacht, [First Name]},
  year={2024},
  url={https://github.com/prof-schacht/llm-cognitive-crawler},
  note={Research in progress}
}
```

## 🔗 Related Work

### Foundational Papers
- Baker et al. (2017). "Rational quantitative attribution of beliefs, desires and percepts in human mentalizing"
- Jara-Ettinger (2019). "Theory of mind as inverse reinforcement learning"
- Gelpi et al. (2025). "Towards Machine Theory of Mind with Large Language Model-Augmented Inverse Planning"

### AI Interpretability
- Anthropic Constitutional AI papers
- OpenAI Model behavior research
- Mechanistic interpretability research

---

*"Understanding the minds of machines to build better, safer, and more aligned AI systems."*
