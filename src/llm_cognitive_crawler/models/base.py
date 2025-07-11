"""Base LLM provider interface."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from ..core.data_models import LLMResponse, ProbingScenario


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name
        self.config = kwargs
    
    @abstractmethod
    async def query(self, scenario: ProbingScenario, **kwargs) -> LLMResponse:
        """Query the LLM with a probing scenario."""
        pass
    
    @abstractmethod
    async def get_available_models(self) -> List[str]:
        """Get list of available models."""
        pass
    
    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the provider is healthy and available."""
        pass
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model."""
        return {
            "model_name": self.model_name,
            "provider": self.__class__.__name__,
            "config": self.config
        }