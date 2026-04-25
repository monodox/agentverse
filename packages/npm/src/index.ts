/**
 * AgentVerse TypeScript SDK — haptics-first agentic simulation by Haptis.
 */

export { BaseAgent, HapticAgent, TeacherAgent } from "./agents.js";
export type { ActionResult, Observation } from "./agents.js";

export { BaseEnv, HapticEnv, RobotEnv } from "./env.js";
export type { EnvConfig, StepResult } from "./env.js";

export { ForceSimulator, SensorSimulator, TouchSimulator } from "./haptics.js";

export { EmbeddingModel, MotokoModel, SpatialModel } from "./models.js";

export { Curriculum, RewardFunction, Trainer } from "./training.js";
