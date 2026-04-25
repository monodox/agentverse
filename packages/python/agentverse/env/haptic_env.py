from __future__ import annotations

from agentverse.env.base_env import BaseEnv


class HapticEnv(BaseEnv):
    """Environment with haptic feedback hooks."""

    def get_feedback(self) -> dict[str, float]:
        return {"force": 0.0, "pressure": 0.0}

