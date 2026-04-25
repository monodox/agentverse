# AGENTS.md

Guidance for coding agents working in the AgentVerse repository.

## Project Overview

AgentVerse by Haptis is an open-source, haptics-first agentic simulation platform for training robots, AI models, and autonomous agents. It is designed around touch, force, pressure, contact, and tactile feedback as first-class simulation signals.

Project links:

- Haptis site: https://haptis.monodox.com
- Repository: https://github.com/monodox/agentverse
- Support: support@monodox.com
- Legal: legal@monodox.com

## Monorepo Layout

This repository is a monorepo with two packages:

```
packages/
  python/   — Python package (PyPI: agentverse)
  npm/      — TypeScript SDK (npm: @agentverse/sdk)
```

The root `package.json` uses npm workspaces to manage the TypeScript package. The Python package is managed independently via `pyproject.toml` inside `packages/python/`.

The project is currently in early pre-alpha. Most modules are scaffolds or placeholders that define the intended package shape.

### Python package (`packages/python/`)

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

### TypeScript SDK (`packages/npm/`)

- `src/agents.ts`: agent classes mirroring the Python API.
- `src/env.ts`: environment classes.
- `src/haptics.ts`: haptic simulation primitives.
- `src/models.ts`: model integration points.
- `src/training.ts`: training utilities.
- `tests/`: vitest test suite.

## Setup

### Python

```bash
cd packages/python
pip install -e ".[dev]"
```

Alternative requirements install:

```bash
cd packages/python
pip install -r requirements.txt
```

Use `packages/python/.env.example` as the template for local environment variables. `.env.local` is for local values and must not contain committed secrets.

### TypeScript

From the repository root:

```bash
npm install
npm run build
```

## Build and Test Commands

### Python

Run tests:

```bash
cd packages/python
pytest
```

Run a specific test file:

```bash
pytest packages/python/tests/test_agents.py
```

Run the basic example after installing the package:

```bash
python packages/python/examples/basic_agent.py
```

Validate imports without installing by setting `PYTHONPATH`:

```bash
PYTHONPATH=packages/python python packages/python/examples/basic_agent.py
```

On PowerShell:

```powershell
$env:PYTHONPATH='packages/python'; python packages\python\examples\basic_agent.py
```

Compile-check the package:

```bash
python -m compileall packages/python/agentverse
```

### TypeScript

From the repository root:

```bash
npm run build       # compile TypeScript
npm test            # run vitest
npm run lint        # lint source
```

## Code Style

### Python

- Use Python 3.10+ syntax.
- Keep public interfaces typed where practical.
- Prefer small, focused classes and functions.
- Keep scaffolding simple until the backend behavior is real.
- Avoid adding abstractions that do not serve current package boundaries.
- Use `ruff` and `black` for linting and formatting:

```bash
cd packages/python
ruff check .
black .
```

### TypeScript

- Use strict TypeScript with ES2022 target.
- Keep public interfaces typed.
- Mirror the Python package's public API surface.
- Use ESLint for linting.

## Testing Instructions

- Add tests for behavior changes.
- Keep tests close to the module being changed.
- Prefer deterministic tests with no network calls.
- Do not require MuJoCo, Ray, GPU, cloud credentials, or large model downloads for basic unit tests unless the test is explicitly marked as an integration test.
- If a dependency is optional or heavy, mock the boundary in unit tests.
- TypeScript tests use vitest. Run with `npm test` from the root.

## Documentation Guidelines

Update docs when changing public behavior:

- `README.md` for project-level positioning, install, and quick start.
- `packages/python/docs/getting_started.md` for Python onboarding workflows.
- `packages/python/docs/architecture.md` for package design and system flow.
- `packages/python/docs/api_reference.md` for public classes and methods.
- `packages/npm/README.md` for TypeScript SDK usage.
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

The Python package includes heavy simulation and ML dependencies such as MuJoCo, PyTorch, Transformers, Ray RLlib, and Hugging Face tooling. Do not assume all contributors have GPU access, cloud credentials, or these packages installed unless the task explicitly concerns those integrations.

When adding code that touches heavy dependencies:

- Keep imports local where possible.
- Provide clear error messages for missing optional dependencies.
- Keep lightweight unit tests available without the full ML/simulation stack.

The TypeScript SDK has minimal dependencies (TypeScript, vitest, ESLint). Keep it lightweight.

## Pull Request Guidelines

Before opening or finalizing a PR:

- Run relevant tests for both packages if changes span both.
- Run formatting and linting when available.
- Update documentation for public changes.
- Add changelog notes for notable behavior or dependency changes.
- Explain the motivation and scope clearly.

## Commit Message Guidelines

Use concise, descriptive commit messages. Prefer conventional prefixes when helpful:

- `docs: update getting started guide`
- `feat: add haptic feedback interface`
- `feat(npm): add training utilities to SDK`
- `fix: handle empty sensor readings`
- `test: cover trainer step output`
- `chore: update dependency metadata`

## Repository Hygiene

- Do not commit generated caches such as `__pycache__`, `.pytest_cache`, `.ruff_cache`, `node_modules`, `dist`, build outputs, or virtual environments.
- Do not commit large datasets, model checkpoints, experiment logs, or W&B output directories.
- Keep examples runnable and small.
- Keep config defaults safe for local development.

## Current Project State

AgentVerse is a scaffold, not a production-complete simulator yet. The best contributions are those that improve the public shape of the project without pretending incomplete systems are fully implemented.
