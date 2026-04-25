/**
 * Simulation environments.
 */

export interface EnvConfig {
  [key: string]: unknown;
}

export interface StepResult {
  state: Record<string, unknown>;
  reward: number;
  done: boolean;
  info: Record<string, unknown>;
}

/** Base interface for simulation environments. */
export class BaseEnv {
  readonly config: EnvConfig;
  state: Record<string, unknown>;

  constructor(config: EnvConfig = {}) {
    this.config = config;
    this.state = {};
  }

  reset(): Record<string, unknown> {
    this.state = {};
    return this.state;
  }

  step(action: unknown): StepResult {
    return { state: this.state, reward: 0.0, done: false, info: { action } };
  }
}

/** Environment with haptic feedback hooks. */
export class HapticEnv extends BaseEnv {
  getFeedback(): Record<string, number> {
    return { force: 0.0, pressure: 0.0 };
  }
}

/** Environment for robot control tasks. */
export class RobotEnv extends BaseEnv {
  getRobotState(): Record<string, number> {
    return { x: 0.0, y: 0.0, z: 0.0 };
  }
}
