import { describe, expect, it } from "vitest";
import { BaseAgent, HapticAgent, TeacherAgent } from "../src/agents.js";

describe("BaseAgent", () => {
  it("returns action with agent name", () => {
    const action = new BaseAgent("test").act({ value: 1 });
    expect(action.agent).toBe("test");
  });
});

describe("HapticAgent", () => {
  it("passes through touch feedback", () => {
    const result = new HapticAgent().processTouch({ pressure: 1.0 });
    expect(result.pressure).toBe(1.0);
  });
});

describe("TeacherAgent", () => {
  it("demonstrates using act", () => {
    const result = new TeacherAgent().demonstrate({});
    expect(result.agent).toBe("agent");
  });
});
