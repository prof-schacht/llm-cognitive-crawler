# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Rules to Follow:
1. ALWAYS write secure best practice Python code.
2. Always try to write as lean as possible code. Don't blow up the repo. 
4 Iterate function based on pytest results
5. MOVE Test scripts to the tests folder if they are not already there and ensure that they could be reused for later Tests for code coverage or reruns.
6. ALWAYS commit after each new function is added to our codebase
7. Ensure that you are using uv for isolating environments and packagemanagement
8. Use tree command for project structure. If tree comand not exist install it with command: brew install tree
9. For new and open functionalities which should be implemented create first a new branch and work in this branch - Check in the branch as PR
10. Ensure that always if a issue is completed pull requests are created.
11. Create a tmp folder for development. And create a scratchpad.md file in this folder to chronologically document the development process in a way that humans and llms can easily pickup the development.
12. Give the user after each finished step a short advise how to test your implementation, by creating a docs/testplan.md file for the user.
13. Always update or create the docs/howto.md file with the newly changed functionality to know how to use the actual implementation.
14. Absolut important keep the repo lean and clean, don't add unnecessary files, don't overengineer.
15. Om major implementation steps create a documentation update based on the instruction you find in docs/01-update-docs.md
16. IF things are unclear perform web search
17. Look heavily in the documentation and code of inspect ai and deepteam
18. if we need access to language models use ollama as a starting point: 
BAseurl: http:/localhost:11434 
IDentify Hosted Models: curl http://localhost:11434/api/tags
19. Ensure that the test coverage is above 80% and always test if your implementations are really working. Don't commit or finish any activity without ensuring that this implemented stuff is working. Always run the whole test suite after you implemented a new aspect. 


1.  Span different sup agent to work on task parallel if possible. 

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LLM Cognitive Crawler is a research project that uses Bayesian inverse planning to reverse-engineer cognitive patterns and mental models of Large Language Models. The project systematically probes LLMs across different cognitive domains (ethical reasoning, logical reasoning, risk assessment, social cognition, causal reasoning) to create "cognitive fingerprints" and detect biases.

## Development Commands

### Environment Setup

For Package Handling and Environment use UV/UVX with alle relevenat dependencies.


### API Configuration
```bash
# Copy and configure API keys
cp config/api_keys.example.env config/api_keys.env
# Edit config/api_keys.env with actual API keys (never commit this file)
```

### Testing
```bash
# Run full test suite
pytest

# Run with coverage
pytest --cov=llm_cognitive_crawler

# Run specific test files
pytest tests/test_scenarios.py
```

### Code Quality
```bash
# Format code with Black (when configured)
black .

# Type checking with mypy (when configured)
mypy llm_cognitive_crawler

# Lint with flake8 (when configured)
flake8 llm_cognitive_crawler
```

## Core Architecture

### Primary Components
Based on the README.md architecture description:

- **LLMCognitiveCrawler**: Main orchestrator class
- **scenario_generator**: Creates systematic cognitive probing tests
- **hypothesis_framework**: Defines cognitive pattern hypotheses (utilitarian, cautious, rule-based, etc.)
- **llm_interface**: Manages API connections to different LLM providers (OpenAI, Anthropic, Google, Mistral, etc.)
- **response_classifier**: NLP-based categorization of LLM outputs
- **bayesian_engine**: Updates beliefs using inverse planning methodology
- **profile_analyzer**: Generates cognitive insights and fingerprints

### Key Research Domains
- **Ethical Reasoning**: Trolley problems, fairness dilemmas (Utilitarian vs. Deontological vs. Virtue ethics)
- **Logical Reasoning**: Syllogisms, probability puzzles (Formal logic vs. Heuristic reasoning)
- **Risk Assessment**: Financial choices, uncertainty (Risk-averse vs. Risk-seeking vs. Optimizing)
- **Social Cognition**: Theory of mind, cultural scenarios (Empathetic vs. Analytical social reasoning)
- **Causal Reasoning**: Scientific thinking, counterfactuals (Mechanistic vs. Correlational reasoning)

### API Integration
The project supports multiple LLM providers:
- OpenAI (GPT-4, etc.)
- Anthropic (Claude-3, etc.)
- Google AI (Gemma, PaLM models)
- Cohere
- Hugging Face
- Mistral AI
- ollama (local)

### Configuration Management
- API keys stored in `config/api_keys.env` (never committed)
- Rate limiting and cost management built-in
- Model-specific parameter configuration
- Caching and performance monitoring capabilities

## Research Methodology

The project implements Bayesian inverse planning where:
```
P(Mental Model | Response) ∝ P(Response | Mental Model) × P(Mental Model)
```

### Usage Pattern
```python
from llm_cognitive_crawler import LLMCognitiveCrawler
from scenario_generators import EthicalScenarios, ReasoningScenarios
from hypothesis_generators import ReasoningStyleHypotheses

# Initialize crawler with target model
crawler = LLMCognitiveCrawler("gpt-4")

# Add cognitive probing scenarios
crawler.add_scenarios(EthicalScenarios.generate_all())
crawler.add_scenarios(ReasoningScenarios.generate_all())

# Add cognitive hypotheses
crawler.add_hypotheses(ReasoningStyleHypotheses.generate_all())

# Run comprehensive analysis
results = crawler.run_comprehensive_analysis()

# Generate cognitive profile
profile = crawler.generate_cognitive_profile()
```

## Security and Privacy

- Never commit API keys or sensitive configuration
- All API keys go in `config/api_keys.env` (gitignored)
- Anonymization and data retention policies implemented
- Encryption and audit logging capabilities
- Cost monitoring and budget controls

## Current Project Status

This is an early-stage research project. The repository currently contains:
- Comprehensive documentation and research framework
- API configuration templates
- Contributing guidelines
- No actual Python implementation yet (based on file exploration)

The project is in the planning/design phase with a 12-month research timeline across 4 phases: Foundation, Expansion, Validation, and Applications.