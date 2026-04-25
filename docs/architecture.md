# Architecture

AgentVerse is organized around a haptics-first agent training loop. The platform is designed to let agents observe world state, act in simulated environments, receive touch and force feedback, and generate data that can improve both policies and haptic foundation models.

## System Loop

The intended high-level loop is:

1. An environment exposes robot, scene, and haptic state.
2. An agent chooses an action from that observation.
3. The simulation backend advances the world.
4. Haptic simulators return force, pressure, contact, and sensor readings.
5. Training utilities compute reward and curriculum progress.
6. Motoko integration points receive labeled haptic data for model improvement.
7. Improved models and agents are fed back into future simulation runs.

This recursive loop is the core distinction of AgentVerse: simulation is not just a playback or design tool, but part of a self-improving training system.

## Package Areas

- `agentverse.env`: simulation environment interfaces, including haptic and robot environments.
- `agentverse.agents`: base, haptic, and teacher-agent implementations.
- `agentverse.haptics`: force, touch, and sensor simulation primitives.
- `agentverse.models`: Motoko, embedding, and spatial model integration points.
- `agentverse.training`: training loops, curricula, and reward utilities.
- `agentverse.sim`: simulation backend hooks for MuJoCo and USD assets.
- `agentverse.utils`: shared configuration, data, and logging helpers.

## Design Principles

- **Haptics first**: touch, force, pressure, and contact are treated as primary signals.
- **Agentic training**: agents are expected to learn from interaction, not only scripted demonstrations.
- **Recursive improvement**: agents can produce data that improves models, which then improves future agents.
- **Accessible infrastructure**: the project is shaped to run on modest research and startup infrastructure, including single-GPU setups.
- **Open ecosystem**: AgentVerse is intended to sit beside HAPT and Motoko as part of the Haptis open-source stack.
