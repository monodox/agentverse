# Getting Started

AgentVerse is a Python package for haptics-first agent simulation. The repository is currently an early scaffold, so the examples exercise placeholder interfaces while the MuJoCo, RLlib, and Motoko integrations mature.

## Installation

Install the package in editable mode from the repository root:

```bash
pip install -e .
```

Install development dependencies when running tests:

```bash
pip install -e ".[dev]"
```

## Run an Example

```bash
python examples/basic_agent.py
```

The basic example creates a `BaseEnv`, creates a `BaseAgent`, resets the environment, asks the agent for an action, and prints the action payload.

## Run Tests

```bash
pytest
```

## Configuration

The `configs/` directory contains starter YAML files:

- `default_env.yaml`: environment and haptic feedback settings.
- `agent_config.yaml`: agent identity and policy settings.
- `training_config.yaml`: training loop, curriculum, and optimization settings.

These files are intentionally small so downstream projects can extend them for robot-specific tasks, haptic sensors, and Motoko data generation.
