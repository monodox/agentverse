# API Reference

This reference describes the current public scaffold. APIs are expected to grow as the haptics-first simulation, Motoko, MuJoCo, and multi-agent training integrations mature.

## Agents

### `BaseAgent`

`agentverse.agents.BaseAgent` is the base interface for agent implementations.

- `BaseAgent(name: str = "agent")`
- `act(observation: dict[str, Any]) -> Any`

### `HapticAgent`

`agentverse.agents.HapticAgent` extends `BaseAgent` with haptic feedback handling.

- `process_touch(feedback: dict[str, float]) -> dict[str, float]`

### `TeacherAgent`

`agentverse.agents.TeacherAgent` provides a placeholder interface for demonstration actions.

- `demonstrate(observation: dict[str, Any]) -> Any`

## Environments

### `BaseEnv`

`agentverse.env.BaseEnv` is the base simulation environment interface.

- `BaseEnv(config: dict[str, Any] | None = None)`
- `reset() -> dict[str, Any]`
- `step(action: Any) -> tuple[dict[str, Any], float, bool, dict[str, Any]]`

### `HapticEnv`

`agentverse.env.HapticEnv` extends `BaseEnv` with haptic feedback hooks.

- `get_feedback() -> dict[str, float]`

### `RobotEnv`

`agentverse.env.RobotEnv` exposes starter robot state.

- `get_robot_state() -> dict[str, float]`

## Haptics

### `ForceSimulator`

`agentverse.haptics.ForceSimulator` provides starter force computation.

- `compute_force(mass: float, acceleration: float) -> float`

### `SensorSimulator`

`agentverse.haptics.SensorSimulator` exposes starter haptic sensor readings.

- `read() -> dict[str, float]`

### `TouchSimulator`

`agentverse.haptics.TouchSimulator` exposes starter contact detection.

- `detect_contact(pressure: float, threshold: float = 0.1) -> bool`

## Models

### `MotokoModel`

`agentverse.models.MotokoModel` is the placeholder integration point for Haptis's Motoko haptic foundation model family.

- `predict(inputs: dict[str, Any]) -> dict[str, Any]`

## Training

### `Trainer`

`agentverse.training.Trainer` coordinates a minimal environment-agent training step.

- `Trainer(env: Any, agent: Any)`
- `train_step() -> dict[str, Any]`
