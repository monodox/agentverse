/**
 * Training utilities.
 */

import type { BaseAgent } from "./agents.js";
import type { BaseEnv, StepResult } from "./env.js";

/** Tracks curriculum difficulty. */
export class Curriculum {
  difficulty: number;

  constructor(difficulty = 1) {
    this.difficulty = difficulty;
  }

  advance(): number {
    this.difficulty += 1;
    return this.difficulty;
  }
}

/** Basic reward function placeholder. */
export class RewardFunction {
  compute(success: boolean): number {
    return success ? 1.0 : 0.0;
  }
}

/** Basic training loop placeholder. */
export class Trainer {
  readonly env: BaseEnv;
  readonly agent: BaseAgent;

  constructor(env: BaseEnv, agent: BaseAgent) {
    this.env = env;
    this.agent = agent;
  }

  trainStep(): StepResult {
    const observation = this.env.reset();
    const action = this.agent.act(observation);
    return this.env.step(action);
  }
}
