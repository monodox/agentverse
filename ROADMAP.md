# Roadmap

AgentVerse is currently in early pre-alpha development. This roadmap is intentionally high-level and will evolve with the project.

## Phase 1: Foundation

- Stabilize package layout and public interfaces.
- Expand documentation and examples.
- Add clear environment, agent, haptic, model, and training abstractions.
- Keep tests aligned with the scaffold.

## Phase 2: Haptic Simulation Core

- Implement richer force, pressure, contact, and tactile sensor primitives.
- Add configurable haptic feedback pipelines.
- Connect haptic feedback to environment step outputs.
- Add benchmark tasks for touch-aware agents.

## Phase 3: Simulation Backends

- Improve MuJoCo integration.
- Add robot task templates.
- Support USD asset loading workflows.
- Document backend setup and limitations.

## Phase 4: Training and Self-Improvement

- Add multi-agent training examples.
- Integrate Ray RLlib workflows.
- Improve reward and curriculum utilities.
- Generate labeled haptic data from agent interactions.

## Phase 5: Motoko Integration

- Define stable Motoko model interfaces.
- Add data export/import paths for haptic training data.
- Support feedback loops between simulation, agents, and models.

## Phase 6: Developer Experience

- Add richer CLI or developer console workflows.
- Improve configuration validation.
- Add more complete examples, tutorials, and tests.
- Prepare packaging and release workflows.
