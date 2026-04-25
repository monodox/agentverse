# Contributing

Thanks for your interest in contributing to AgentVerse.

AgentVerse is an open-source haptics-first simulation platform by Haptis. The project is early-stage, so contributions that improve clarity, correctness, tests, examples, and architecture are especially valuable.

## Development Setup

Clone the repository and install it in editable mode:

```bash
pip install -e ".[dev]"
```

You can also install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

## Code Style

Use the configured Python tooling:

```bash
ruff check .
black .
```

## Contribution Guidelines

- Keep changes focused and easy to review.
- Add or update tests for behavior changes.
- Update documentation when public APIs, configs, or workflows change.
- Avoid committing secrets, local credentials, large generated files, or model artifacts.
- Prefer clear interfaces over premature abstractions.

## Pull Requests

Before opening a pull request:

- Confirm tests pass.
- Confirm formatting and linting pass.
- Describe what changed and why.
- Link related issues when available.

## Project Areas

Useful contribution areas include:

- Haptic simulation primitives.
- MuJoCo environment integration.
- Multi-agent training flows.
- Motoko model integration points.
- Example tasks and benchmark scenarios.
- Documentation and onboarding improvements.
