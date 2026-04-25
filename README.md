# AgentVerse by Haptis

AgentVerse is an open-source agentic simulation platform built by Haptis for training robots, AI models, and agents in a haptics-first virtual environment.

Unlike traditional simulators that focus mainly on vision and physics, AgentVerse treats touch and force as foundational sensory primitives. The project is designed as the simulation backbone for haptic intelligence: agents observe, act, receive haptic feedback, and improve inside environments where force, pressure, contact, and tactile state are first-class signals.

## Why AgentVerse

AgentVerse is built around a self-improving loop:

1. Agents act in simulated robot and haptic environments.
2. The environment returns task state plus haptic feedback.
3. Training utilities convert those interactions into rewards, curriculum progress, and labeled haptic data.
4. Teacher and learner agents improve over time.
5. The generated data feeds back into Motoko, Haptis's open-source haptic foundation model family developed by Monodox.

This creates a closed-loop system where simulation, agents, and models can co-evolve together, reducing the need for constant human-authored simulation design.

## Ecosystem

AgentVerse sits inside the Haptis ecosystem alongside:

- **HAPT**: the developer console and integration surface.
- **Motoko**: the open-source haptic foundation model family.
- **AgentVerse**: the simulation and training backbone for touch-aware agents.

Together, these pieces form an open-source stack for haptic intelligence and next-generation robotics.

## Current Status

This repository currently contains the Python package scaffold for AgentVerse:

- Simulation environment interfaces
- Robot and haptic environment hooks
- Agent definitions, including haptic and teacher-agent placeholders
- Haptic simulation primitives for force, touch, and sensor feedback
- Motoko model integration placeholders
- Training utilities for curricula, rewards, and training loops
- MuJoCo and USD backend integration hooks
- Examples, tests, documentation, and YAML configs

The implementation is intentionally early-stage. The public interfaces are being shaped around the haptics-first training loop before backend integrations become production-complete.

## Install

```bash
pip install -e .
```

For development tools:

```bash
pip install -e ".[dev]"
```

## Quick Start

Run the basic agent example:

```bash
python examples/basic_agent.py
```

Run the test suite:

```bash
pytest
```

## Core Stack

- Python package distributed through PyPI-compatible tooling
- MuJoCo hooks for physics simulation
- PyTorch-facing model integration points
- Ray RLlib-oriented multi-agent training structure
- YAML configuration for environments, agents, and training

## Open Source

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.
- Read [AGENTS.md](AGENTS.md) for coding-agent and automation guidance.
- Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.
- Report vulnerabilities using [SECURITY.md](SECURITY.md).
- Track planned work in [ROADMAP.md](ROADMAP.md).
- See release notes in [CHANGELOG.md](CHANGELOG.md).
- Use [.env.example](.env.example) as the local environment template.

## License

AgentVerse is released under the Apache License 2.0.
