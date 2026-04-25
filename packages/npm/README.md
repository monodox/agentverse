# @monodox/agentverse

TypeScript SDK for AgentVerse — haptics-first agentic simulation by Haptis.

This package mirrors the public API of the [AgentVerse Python package](../python) for use in Node.js tooling, web dashboards, and JavaScript-based agent orchestration.

## Install

```bash
npm install @monodox/agentverse
```

## Quick Start

```typescript
import { BaseAgent, BaseEnv, Trainer } from "@monodox/agentverse";

const env = new BaseEnv();
const agent = new BaseAgent("learner");
const trainer = new Trainer(env, agent);

console.log(trainer.trainStep());
```

## API

### Agents

- `BaseAgent` — base interface for agents
- `HapticAgent` — agent with haptic feedback handling
- `TeacherAgent` — agent that provides demonstration actions

### Environments

- `BaseEnv` — base simulation environment
- `HapticEnv` — environment with haptic feedback hooks
- `RobotEnv` — environment for robot control tasks

### Haptics

- `ForceSimulator` — force computation
- `SensorSimulator` — haptic sensor readings
- `TouchSimulator` — contact detection

### Models

- `EmbeddingModel` — embedding placeholder
- `MotokoModel` — Motoko integration point
- `SpatialModel` — spatial distance computation

### Training

- `Trainer` — environment-agent training loop
- `Curriculum` — curriculum difficulty tracking
- `RewardFunction` — reward computation

## Development

```bash
npm run build    # compile TypeScript
npm test         # run tests
npm run lint     # lint source
```

## License

Apache License 2.0
