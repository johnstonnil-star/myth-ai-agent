# myth_agent/base_agent.py
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Base interface for all agents."""

    @abstractmethod
    async def run(self, prompt: str) -> str:
        ...
