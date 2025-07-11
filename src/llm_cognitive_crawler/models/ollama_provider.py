"""Ollama provider for local LLM access."""

import time
from typing import Dict, Any, Optional, List
import httpx
import json
from ..core.data_models import LLMResponse, ProbingScenario
from .base import LLMProvider


class OllamaProvider(LLMProvider):
    """Ollama provider for local LLM inference."""
    
    def __init__(self, model_name: str, base_url: str = "http://localhost:11434", **kwargs):
        super().__init__(model_name, **kwargs)
        self.base_url = base_url.rstrip('/')
        self.client = httpx.AsyncClient(timeout=120.0)
    
    async def query(self, scenario: ProbingScenario, **kwargs) -> LLMResponse:
        """Query Ollama with a probing scenario."""
        start_time = time.perf_counter()
        
        try:
            request_data = {
                "model": self.model_name,
                "prompt": scenario.prompt,
                "stream": False,
                **kwargs
            }
            
            response = await self.client.post(
                f"{self.base_url}/api/generate",
                json=request_data
            )
            response.raise_for_status()
            
            result = response.json()
            end_time = time.perf_counter()
            
            return LLMResponse(
                scenario_id=scenario.scenario_id,
                model_name=self.model_name,
                model_version=result.get("model", self.model_name),
                raw_response=result.get("response", ""),
                response_time_ms=(end_time - start_time) * 1000,
                metadata={
                    "total_duration": result.get("total_duration"),
                    "load_duration": result.get("load_duration"),
                    "prompt_eval_count": result.get("prompt_eval_count"),
                    "eval_count": result.get("eval_count"),
                    "eval_duration": result.get("eval_duration"),
                }
            )
            
        except Exception as e:
            end_time = time.perf_counter()
            return LLMResponse(
                scenario_id=scenario.scenario_id,
                model_name=self.model_name,
                model_version="error",
                raw_response=f"Error: {str(e)}",
                response_time_ms=(end_time - start_time) * 1000,
                metadata={"error": str(e)}
            )
    
    async def get_available_models(self) -> List[str]:
        """Get list of available Ollama models."""
        try:
            response = await self.client.get(f"{self.base_url}/api/tags")
            response.raise_for_status()
            data = response.json()
            return [model["name"] for model in data.get("models", [])]
        except Exception:
            return []
    
    async def health_check(self) -> bool:
        """Check if Ollama is running and accessible."""
        try:
            response = await self.client.get(f"{self.base_url}/api/tags")
            return response.status_code == 200
        except Exception:
            return False
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()