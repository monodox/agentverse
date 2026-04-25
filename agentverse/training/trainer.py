from __future__ import annotations

from typing import Any


class Trainer:
    """Basic training loop placeholder."""

    def __init__(self, env: Any, agent: Any) -> None:
        self.env = env
        self.agent = agent

    def train_step(self) -> dict[str, Any]:
        observation = self.env.reset()
        action = self.agent.act(observation)
        next_state, reward, done, info = self.env.step(action)
        return {"state": next_state, "reward": reward, "done": done, "info": info}
