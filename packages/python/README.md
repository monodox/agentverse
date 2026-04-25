# AgentVerse — Python Package

The core Python package for AgentVerse, a haptics-first agentic simulation platform by Haptis.

Part of the [AgentVerse monorepo](../../README.md).

## Links

- Haptis: https://haptis.monodox.com
- Repository: https://github.com/monodox/agentverse
- Support: support@monodox.com

## Install

```bash
pip install -e .
```

For development tools:

```bash
pip install -e ".[dev]"
```

## Quick Start

```bash
python examples/basic_agent.py
```

## Run Tests

```bash
pytest
```

## Package Structure

- `agentverse.env` — environment interfaces for base, haptic, and robot simulations
- `agentverse.agents` — base, haptic, and teacher-agent definitions
- `agentverse.haptics` — force, touch, and sensor simulation primitives
- `agentverse.models` — Motoko, embedding, and spatial model integration points
- `agentverse.training` — trainer, curriculum, and reward utilities
- `agentverse.sim` — MuJoCo and USD backend hooks
- `agentverse.utils` — configuration, data, and logging helpers
- `configs/` — starter YAML configs
- `docs/` — architecture, getting started, and API reference
- `examples/` — runnable example scripts
- `tests/` — test suite

## Configuration

Copy `.env.example` to `.env.local` for local development. Never commit real secrets.

## Code Style

```bash
ruff check .
black .
```

## Documentation

- [Getting Started](docs/getting_started.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)

## License

Apache License 2.0
