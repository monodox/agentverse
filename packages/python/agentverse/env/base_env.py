from __future__ import annotations

from typing import Any


class BaseEnv:
    """Base interface for simulation environments."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        self.config = config or {}
        self.state: dict[str, Any] = {}

    def reset(self) -> dict[str, Any]:
        self.state = {}
        return self.state

    def step(self, action: Any) -> tuple[dict[str, Any], float, bool, dict[str, Any]]:
        return self.state, 0.0, False, {"action": action}

