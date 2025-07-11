"""LLM Cognitive Crawler - Bayesian Inverse Planning for LLM Mental Models."""

from .core import (
    LLMCognitiveCrawler,
    ProbingScenario,
    CognitiveHypothesis,
    LLMResponse,
    BayesianEngine,
)
from .models import LLMProvider, OllamaProvider

__version__ = "0.1.0"
__all__ = [
    "LLMCognitiveCrawler",
    "ProbingScenario", 
    "CognitiveHypothesis",
    "LLMResponse",
    "BayesianEngine",
    "LLMProvider",
    "OllamaProvider",
]

def main() -> None:
    print(f"LLM Cognitive Crawler v{__version__}")
    print("Bayesian Inverse Planning for Reverse Engineering LLM Mental Models")
