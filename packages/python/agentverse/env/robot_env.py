from __future__ import annotations

from agentverse.env.base_env import BaseEnv


class RobotEnv(BaseEnv):
    """Environment for robot control tasks."""

    def get_robot_state(self) -> dict[str, float]:
        return {"x": 0.0, "y": 0.0, "z": 0.0}

