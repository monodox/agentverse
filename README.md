# AgentVerse by Haptis

AgentVerse is an open-source agentic simulation platform built by Haptis for training robots, AI models, and agents in a haptics-first virtual environment.

Unlike traditional simulators that focus mainly on vision and physics, AgentVerse treats touch and force as foundational sensory primitives. The project is designed as the simulation backbone for haptic intelligence: agents observe, act, receive haptic feedback, and improve inside environments where force, pressure, contact, and tactile state are first-class signals.

## Links

- Haptis: https://haptis.monodox.com
- Repository: https://github.com/monodox/agentverse
- Support: support@monodox.com
- Legal: legal@monodox.com

## Monorepo Structure

This repository is organized as a monorepo with two packages:

```
packages/
  python/   — Python package (PyPI: agentverse)
  npm/      — TypeScript SDK (npm: @monodox/agentverse)
```

### Python Package

The core simulation platform. Includes environments, agents, haptic primitives, model integration points, training utilities, and MuJoCo/USD backend hooks.

```bash
cd packages/python
pip install -e ".[dev]"
pytest
```

See [packages/python/docs/getting_started.md](packages/python/docs/getting_started.md) for full setup.

### TypeScript SDK

A TypeScript client that mirrors the Python package's public API for use in Node.js tooling, web dashboards, and JavaScript-based agent orchestration.

```bash
npm install
npm run build
npm test
```

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

## Current Status

This repository is in early pre-alpha. The public interfaces are being shaped around the haptics-first training loop before backend integrations become production-complete.

## Open Source

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.
- Read [AGENTS.md](AGENTS.md) for coding-agent and automation guidance.
- Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.
- Report vulnerabilities using [SECURITY.md](SECURITY.md).
- Track planned work in [ROADMAP.md](ROADMAP.md).
- See release notes in [CHANGELOG.md](CHANGELOG.md).

## License

AgentVerse is released under the Apache License 2.0.
