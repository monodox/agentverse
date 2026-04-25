from __future__ import annotations

from typing import Any

from agentverse.agents.base_agent import BaseAgent


class TeacherAgent(BaseAgent):
    """Agent that provides demonstration actions."""

    def demonstrate(self, observation: dict[str, Any]) -> Any:
        return self.act(observation)

