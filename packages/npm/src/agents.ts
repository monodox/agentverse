/**
 * Agent definitions.
 */

export interface Observation {
  [key: string]: unknown;
}

export interface ActionResult {
  agent: string;
  observation: Observation;
}

/** Base interface for agents. */
export class BaseAgent {
  readonly name: string;

  constructor(name = "agent") {
    this.name = name;
  }

  act(observation: Observation): ActionResult {
    return { agent: this.name, observation };
  }
}

/** Agent that can consume haptic feedback. */
export class HapticAgent extends BaseAgent {
  processTouch(feedback: Record<string, number>): Record<string, number> {
    return { ...feedback };
  }
}

/** Agent that provides demonstration actions. */
export class TeacherAgent extends BaseAgent {
  demonstrate(observation: Observation): ActionResult {
    return this.act(observation);
  }
}
