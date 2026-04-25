from __future__ import annotations

from typing import Any


class BaseAgent:
    """Base interface for agents."""

    def __init__(self, name: str = "agent") -> None:
        self.name = name

    def act(self, observation: dict[str, Any]) -> Any:
        return {"agent": self.name, "observation": observation}

