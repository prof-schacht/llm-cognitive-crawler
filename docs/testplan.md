# Test Plan for LLM Cognitive Crawler Phase 1

## Overview
This document describes how to test the Phase 1 implementation of the LLM Cognitive Crawler core architecture.

## Prerequisites
1. Ensure you have Python 3.11+ installed
2. Install dependencies: `uv sync --dev`
3. (Optional) Install and run Ollama locally: http://localhost:11434

## Core Functionality Tests

### 1. Unit Tests
Run the comprehensive test suite:
```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ -v --cov=src/llm_cognitive_crawler --cov-report=term-missing

# Run specific test modules
uv run pytest tests/test_data_models.py -v
uv run pytest tests/test_bayesian_engine.py -v  
uv run pytest tests/test_ollama_provider.py -v
uv run pytest tests/test_crawler.py -v
```

Expected results: >80% test coverage, all tests passing

### 2. Basic Integration Test
Test the core workflow with mock data:

```python
from llm_cognitive_crawler import (
    LLMCognitiveCrawler, 
    ProbingScenario, 
    CognitiveHypothesis,
    CognitiveDomain,
    ResponseType
)
from llm_cognitive_crawler.models import OllamaProvider

# Create a simple scenario
scenario = ProbingScenario(
    title="Simple Ethics Test",
    prompt="Is it okay to lie to protect someone's feelings?",
    domain=CognitiveDomain.ETHICAL_REASONING,
    response_type=ResponseType.BINARY_CHOICE
)

# Create a hypothesis
hypothesis = CognitiveHypothesis(
    name="Utilitarian Reasoner",
    description="Maximizes overall happiness",
    predicted_response_patterns={
        "ethical_reasoning_binary_choice": {"yes": 0.7, "protect": 0.8}
    },
    cognitive_attributes={"empathy": 0.8, "outcome_focused": 0.9},
    prior_probability=0.4
)

# Test with mock provider (no Ollama needed)
from tests.test_crawler import MockLLMProvider
provider = MockLLMProvider()
provider.set_response(scenario.scenario_id, "Yes, protecting feelings is important")

# Create crawler and run analysis
crawler = LLMCognitiveCrawler(provider)
crawler.add_scenario(scenario)
crawler.add_hypothesis(hypothesis)

# Run single scenario
import asyncio
response = asyncio.run(crawler.run_scenario(scenario.scenario_id))
print(f"Response: {response.raw_response}")

# Generate cognitive profile
profile = crawler.generate_cognitive_profile()
print(f"Dominant pattern: {profile.dominant_pattern}")
print(f"Confidence: {profile.confidence}")
```

### 3. Ollama Integration Test (Optional)
If you have Ollama running locally:

```python
import asyncio
from llm_cognitive_crawler import LLMCognitiveCrawler, ProbingScenario
from llm_cognitive_crawler.models import OllamaProvider

async def test_ollama():
    # Check if Ollama is available
    provider = OllamaProvider("llama2")  # or any model you have
    
    is_healthy = await provider.health_check()
    if not is_healthy:
        print("Ollama not available - skipping test")
        return
    
    # Get available models
    models = await provider.get_available_models()
    print(f"Available models: {models}")
    
    if not models:
        print("No models available")
        return
    
    # Use first available model
    provider.model_name = models[0]
    
    # Create simple test
    scenario = ProbingScenario(
        title="Math Test",
        prompt="What is 7 + 15?",
    )
    
    crawler = LLMCognitiveCrawler(provider)
    crawler.add_scenario(scenario)
    
    response = await crawler.run_scenario(scenario.scenario_id)
    print(f"Model: {response.model_name}")
    print(f"Response: {response.raw_response}")
    print(f"Time: {response.response_time_ms}ms")
    
    await provider.close()

# Run the test
asyncio.run(test_ollama())
```

### 4. Data Model Validation Tests
Test data model validation:

```python
from llm_cognitive_crawler.core.data_models import *

# Test scenario validation
try:
    scenario = ProbingScenario(title="Test", prompt="")  # Should fail
except ValueError as e:
    print(f"Expected error: {e}")

# Test hypothesis validation  
try:
    hypothesis = CognitiveHypothesis(
        name="Test",
        cognitive_attributes={"invalid": 1.5}  # Should fail
    )
except ValueError as e:
    print(f"Expected error: {e}")

# Test response validation
try:
    response = LLMResponse(scenario_id="", model_name="test")  # Should fail
except ValueError as e:
    print(f"Expected error: {e}")
```

### 5. Bayesian Engine Tests
Test the inference engine:

```python
from llm_cognitive_crawler.core.bayesian_engine import BayesianEngine
from llm_cognitive_crawler.core.data_models import *

engine = BayesianEngine()

# Add competing hypotheses
h1 = CognitiveHypothesis(
    name="Utilitarian",
    predicted_response_patterns={
        "ethical_reasoning_binary_choice": {"save more": 0.9}
    },
    prior_probability=0.3
)

h2 = CognitiveHypothesis(
    name="Deontological", 
    predicted_response_patterns={
        "ethical_reasoning_binary_choice": {"save more": 0.1}
    },
    prior_probability=0.7
)

engine.add_hypothesis(h1)
engine.add_hypothesis(h2)

# Create test scenario and response
scenario = ProbingScenario(
    prompt="Trolley problem",
    domain=CognitiveDomain.ETHICAL_REASONING,
    response_type=ResponseType.BINARY_CHOICE
)

response = LLMResponse(
    scenario_id=scenario.scenario_id,
    model_name="test",
    raw_response="I would save more lives"
)

# Update beliefs
posteriors = engine.update_beliefs(scenario, response)
print("Posterior probabilities:")
for hyp_id, prob in posteriors.items():
    hyp = engine.hypotheses[hyp_id]
    print(f"  {hyp.name}: {prob:.3f}")

# Check convergence
metrics = engine.get_convergence_metrics()
print(f"Entropy: {metrics['entropy']:.3f}")
print(f"Max posterior: {metrics['max_posterior']:.3f}")
```

## Success Criteria

### Phase 1 Core Architecture ✅
- [x] All unit tests pass (>80% coverage)
- [x] Core data models work correctly with validation
- [x] Bayesian inference engine updates beliefs properly
- [x] LLM provider interface works (tested with Ollama)
- [x] Main crawler orchestrates workflow correctly
- [x] Cognitive profile generation works
- [x] Export/import functionality available

### Integration Criteria
- [ ] Successfully connects to Ollama (when available)
- [ ] Handles API errors gracefully
- [ ] Proper async/await usage throughout
- [ ] Memory usage remains reasonable for test scenarios
- [ ] Response times acceptable for single queries

### Documentation Criteria
- [x] Core API documented
- [x] Test examples provided
- [x] Installation instructions clear
- [x] Usage patterns demonstrated

## Next Steps
After Phase 1 testing passes:
1. Implement Phase 1.2: Scenario Generation Framework
2. Implement Phase 1.3: Cognitive Hypothesis Framework  
3. Add more LLM providers (OpenAI, Anthropic)
4. Scale testing to larger scenario sets