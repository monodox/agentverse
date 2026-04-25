# AGENTS.md

Guidance for coding agents working in the AgentVerse repository.

## Project Overview

AgentVerse by Haptis is an open-source, haptics-first agentic simulation platform for training robots, AI models, and autonomous agents. It is designed around touch, force, pressure, contact, and tactile feedback as first-class simulation signals.

The project is currently in early pre-alpha. Most modules are scaffolds or placeholders that define the intended package shape:

- `agentverse.env`: environment interfaces for base, haptic, and robot simulations.
- `agentverse.agents`: base, haptic, and teacher-agent definitions.
- `agentverse.haptics`: force, touch, and sensor simulation primitives.
- `agentverse.models`: Motoko, embedding, and spatial model integration points.
- `agentverse.training`: trainer, curriculum, and reward utilities.
- `agentverse.sim`: MuJoCo and USD backend hooks.
- `configs`: starter YAML configs.
- `docs`: architecture, getting started, and API reference docs.
- `examples`: runnable example scripts.
- `tests`: basic test suite.

## Setup

Recommended editable install:

```bash
pip install -e ".[dev]"
```

Alternative requirements install:

```bash
pip install -r requirements.txt
```

Use `.env.example` as the template for local environment variables. `.env.local` is for local values and must not contain committed secrets.

## Build and Test Commands

Run tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_agents.py
```

Run the basic example after installing the package:

```bash
python examples/basic_agent.py
```

Validate imports without installing by setting `PYTHONPATH` to the repo root:

```bash
PYTHONPATH=. python examples/basic_agent.py
```

On PowerShell:

```powershell
$env:PYTHONPATH='.'; python examples\basic_agent.py
```

Compile-check the package:

```bash
python -m compileall agentverse
```

## Code Style

- Use Python 3.10+ syntax.
- Keep public interfaces typed where practical.
- Prefer small, focused classes and functions.
- Keep scaffolding simple until the backend behavior is real.
- Avoid adding abstractions that do not serve current package boundaries.
- Use `ruff` and `black` for linting and formatting:

```bash
ruff check .
black .
```

## Testing Instructions

- Add tests for behavior changes.
- Keep tests close to the module being changed.
- Prefer deterministic tests with no network calls.
- Do not require MuJoCo, Ray, GPU, cloud credentials, or large model downloads for basic unit tests unless the test is explicitly marked as an integration test.
- If a dependency is optional or heavy, mock the boundary in unit tests.

## Documentation Guidelines

Update docs when changing public behavior:

- `README.md` for project-level positioning, install, and quick start.
- `docs/getting_started.md` for onboarding workflows.
- `docs/architecture.md` for package design and system flow.
- `docs/api_reference.md` for public classes and methods.
- `CHANGELOG.md` for notable user-facing changes.
- `ROADMAP.md` for planned work.

Keep documentation honest about the current state. If a feature is a placeholder, say so.

## Security Considerations

- Never commit real secrets, access tokens, cloud keys, or local credentials.
- Keep `.env.local` local-only. Use `.env.example` for templates.
- Avoid unsafe file loading, pickle deserialization, or arbitrary code execution paths.
- Treat model loading, dataset loading, USD assets, and simulation plugins as potentially untrusted inputs.
- Avoid network calls in import-time code.
- Do not add dependencies casually; prefer maintained packages with clear purpose.
- Follow `SECURITY.md` for vulnerability reporting expectations.

## Dependency Notes

This project includes heavy simulation and ML dependencies such as MuJoCo, PyTorch, Transformers, Ray RLlib, and Hugging Face tooling. Do not assume all contributors have GPU access, cloud credentials, or these packages installed unless the task explicitly concerns those integrations.

When adding code that touches heavy dependencies:

- Keep imports local where possible.
- Provide clear error messages for missing optional dependencies.
- Keep lightweight unit tests available without the full ML/simulation stack.

## Pull Request Guidelines

Before opening or finalizing a PR:

- Run relevant tests.
- Run formatting and linting when available.
- Update documentation for public changes.
- Add changelog notes for notable behavior or dependency changes.
- Explain the motivation and scope clearly.

## Commit Message Guidelines

Use concise, descriptive commit messages. Prefer conventional prefixes when helpful:

- `docs: update getting started guide`
- `feat: add haptic feedback interface`
- `fix: handle empty sensor readings`
- `test: cover trainer step output`
- `chore: update dependency metadata`

## Repository Hygiene

- Do not commit generated caches such as `__pycache__`, `.pytest_cache`, `.ruff_cache`, build outputs, or virtual environments.
- Do not commit large datasets, model checkpoints, experiment logs, or W&B output directories.
- Keep examples runnable and small.
- Keep config defaults safe for local development.

## Current Project State

AgentVerse is a scaffold, not a production-complete simulator yet. The best contributions are those that improve the public shape of the project without pretending incomplete systems are fully implemented.
