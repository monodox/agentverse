from __future__ import annotations

from agentverse.agents.base_agent import BaseAgent


class HapticAgent(BaseAgent):
    """Agent that can consume haptic feedback."""

    def process_touch(self, feedback: dict[str, float]) -> dict[str, float]:
        return feedback
