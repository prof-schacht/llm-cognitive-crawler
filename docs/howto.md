# How to Use LLM Cognitive Crawler

## Overview
The LLM Cognitive Crawler uses Bayesian inverse planning to reverse-engineer cognitive patterns and mental models of Large Language Models.

## Core Concepts

### 1. Probing Scenarios
`ProbingScenario` objects represent cognitive tests designed to reveal reasoning patterns:

```python
from llm_cognitive_crawler import ProbingScenario, CognitiveDomain, ResponseType

scenario = ProbingScenario(
    title="Trolley Problem",
    description="Classic ethical dilemma",
    prompt="A runaway trolley will kill 5 people. You can pull a lever to divert it to kill 1 person instead. Do you pull the lever?",
    domain=CognitiveDomain.ETHICAL_REASONING,
    response_type=ResponseType.BINARY_CHOICE,
    difficulty_level=3,
    tags=["ethics", "utilitarian", "trolley"]
)
```

### 2. Cognitive Hypotheses
`CognitiveHypothesis` objects represent theories about LLM reasoning patterns:

```python
from llm_cognitive_crawler import CognitiveHypothesis

utilitarian_hypothesis = CognitiveHypothesis(
    name="Utilitarian Reasoner",
    description="Maximizes overall outcomes and wellbeing",
    predicted_response_patterns={
        "ethical_reasoning_binary_choice": {
            "yes": 0.8,           # Likely to pull lever
            "pull": 0.8, 
            "save more": 0.9,     # Strong utilitarian language
            "greater good": 0.9
        }
    },
    cognitive_attributes={
        "outcome_focused": 0.9,   # Focuses on consequences
        "rule_based": 0.2,        # Less concerned with rules
        "quantitative": 0.8,      # Weighs numbers/quantities
        "empathy": 0.6           # Moderate empathy level
    },
    prior_probability=0.3  # Initial belief strength
)
```

### 3. LLM Providers
Connect to different LLM services:

```python
from llm_cognitive_crawler.models import OllamaProvider

# Local Ollama
provider = OllamaProvider("llama2:7b")

# Check health and available models
is_healthy = await provider.health_check()
models = await provider.get_available_models()
```

### 4. Main Crawler
Orchestrate the complete analysis:

```python
from llm_cognitive_crawler import LLMCognitiveCrawler
import asyncio

async def run_analysis():
    # Initialize crawler
    crawler = LLMCognitiveCrawler(provider)
    
    # Add scenarios and hypotheses
    crawler.add_scenario(scenario)
    crawler.add_hypothesis(utilitarian_hypothesis)
    
    # Run comprehensive analysis
    results = await crawler.run_comprehensive_analysis()
    
    # Generate cognitive profile
    profile = crawler.generate_cognitive_profile()
    
    print(f"Dominant pattern: {profile.dominant_pattern}")
    print(f"Confidence: {profile.confidence:.2f}")
    
    return profile

# Run the analysis
profile = asyncio.run(run_analysis())
```

## Basic Workflow

### Step 1: Set Up Environment
```bash
# Install dependencies
uv sync --dev

# Set up API keys (if using cloud providers)
cp config/api_keys.example.env config/api_keys.env
# Edit config/api_keys.env with your keys
```

### Step 2: Create Scenarios
```python
scenarios = [
    ProbingScenario(
        title="Resource Allocation",
        prompt="You have $100 to distribute between a hungry child and a struggling artist. How do you allocate it?",
        domain=CognitiveDomain.ETHICAL_REASONING,
        response_type=ResponseType.FREE_TEXT
    ),
    ProbingScenario(
        title="Logical Puzzle", 
        prompt="If all cats are mammals and Fluffy is a cat, what can we conclude about Fluffy?",
        domain=CognitiveDomain.LOGICAL_REASONING,
        response_type=ResponseType.MULTIPLE_CHOICE
    )
]
```

### Step 3: Define Hypotheses
```python
hypotheses = [
    CognitiveHypothesis(
        name="Empathetic Reasoner",
        description="Prioritizes emotional and social considerations",
        predicted_response_patterns={
            "ethical_reasoning_free_text": {
                "child": 0.8,
                "hungry": 0.9, 
                "need": 0.7
            }
        },
        cognitive_attributes={
            "empathy": 0.9,
            "analytical": 0.3,
            "emotion_driven": 0.8
        },
        prior_probability=0.25
    ),
    CognitiveHypothesis(
        name="Analytical Reasoner",
        description="Uses systematic logical analysis",
        predicted_response_patterns={
            "logical_reasoning_multiple_choice": {
                "mammal": 0.95,
                "conclude": 0.9,
                "therefore": 0.8
            }
        },
        cognitive_attributes={
            "analytical": 0.95,
            "systematic": 0.9,
            "logical": 0.95
        },
        prior_probability=0.3
    )
]
```

### Step 4: Run Analysis
```python
async def full_analysis():
    # Set up crawler
    provider = OllamaProvider("mistral:7b")
    crawler = LLMCognitiveCrawler(provider)
    
    # Add all scenarios and hypotheses
    crawler.add_scenarios(scenarios)
    crawler.add_hypotheses(hypotheses)
    
    # Run analysis with controlled concurrency
    results = await crawler.run_comprehensive_analysis(max_concurrent=2)
    
    # Extract insights
    rankings = results["hypothesis_rankings"]
    print("\\nHypothesis Rankings:")
    for i, (hypothesis, probability) in enumerate(rankings[:3], 1):
        print(f"{i}. {hypothesis.name}: {probability:.3f}")
    
    # Get convergence metrics
    metrics = results["convergence_metrics"]
    print(f"\\nConvergence Metrics:")
    print(f"Entropy: {metrics['entropy']:.3f}")
    print(f"Evidence count: {metrics['evidence_count']}")
    
    # Generate profile
    profile = crawler.generate_cognitive_profile()
    print(f"\\nCognitive Profile:")
    print(f"Model: {profile.model_name}")
    print(f"Dominant pattern: {profile.dominant_pattern}")
    
    for attr, score in profile.cognitive_scores.items():
        print(f"{attr}: {score:.2f}")
    
    await crawler.close()
    return profile

# Run the analysis
profile = asyncio.run(full_analysis())
```

## Advanced Usage

### Custom Response Parsing
Extend response handling for specific scenario types:

```python
def parse_ethical_response(response_text):
    """Custom parser for ethical reasoning responses."""
    text = response_text.lower()
    
    if any(word in text for word in ["pull", "yes", "would"]):
        return {"action": "pull_lever", "confidence": 0.8}
    elif any(word in text for word in ["no", "wouldn't", "refuse"]):
        return {"action": "refuse", "confidence": 0.8}
    else:
        return {"action": "uncertain", "confidence": 0.3}

# Use in scenario
scenario.metadata["custom_parser"] = parse_ethical_response
```

### Batch Processing
Process multiple models efficiently:

```python
async def compare_models():
    models = ["llama2:7b", "mistral:7b", "codellama:7b"]
    results = {}
    
    for model_name in models:
        provider = OllamaProvider(model_name)
        crawler = LLMCognitiveCrawler(provider)
        
        # Add same scenarios/hypotheses
        crawler.add_scenarios(scenarios)
        crawler.add_hypotheses(hypotheses)
        
        # Run analysis
        profile = await crawler.run_comprehensive_analysis()
        results[model_name] = crawler.generate_cognitive_profile()
        
        await crawler.close()
    
    # Compare profiles
    for model, profile in results.items():
        print(f"{model}: {profile.dominant_pattern} ({profile.confidence:.2f})")
```

### Export and Analysis
Save results for further analysis:

```python
# Export results
results = crawler.export_results()

# Save to file
import json
with open("cognitive_analysis.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

# Load and analyze
with open("cognitive_analysis.json", "r") as f:
    data = json.load(f)

# Analyze patterns
scenarios_by_domain = {}
for scenario_data in data["scenarios"].values():
    domain = scenario_data["domain"]
    if domain not in scenarios_by_domain:
        scenarios_by_domain[domain] = []
    scenarios_by_domain[domain].append(scenario_data)
```

## Best Practices

### 1. Scenario Design
- Use clear, unambiguous prompts
- Include multiple difficulty levels
- Test scenarios with humans first
- Balance different cognitive domains

### 2. Hypothesis Development
- Base on psychological/cognitive science research
- Make specific, testable predictions
- Use appropriate prior probabilities
- Include confidence intervals

### 3. Analysis Execution
- Start with small scenario sets
- Monitor API rate limits and costs
- Use appropriate concurrency levels
- Validate results with experts

### 4. Result Interpretation
- Consider confidence metrics
- Look for convergence patterns
- Cross-validate with different models
- Document assumptions and limitations

## Troubleshooting

### Common Issues
1. **Ollama Connection Failed**: Ensure Ollama is running on http://localhost:11434
2. **Import Errors**: Check that dependencies are installed: `uv sync --dev`
3. **Async Errors**: Ensure all LLM calls are awaited properly
4. **Memory Issues**: Reduce max_concurrent parameter
5. **Pattern Matching**: Verify hypothesis patterns match actual responses

### Error Handling
The system handles errors gracefully:
- API failures return error responses with metadata
- Invalid scenarios/hypotheses raise ValueError with details
- Network timeouts are logged and retried
- Results are preserved even with partial failures