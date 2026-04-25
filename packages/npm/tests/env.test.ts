import { describe, expect, it } from "vitest";
import { BaseEnv, HapticEnv, RobotEnv } from "../src/env.js";

describe("BaseEnv", () => {
  it("steps with default values", () => {
    const env = new BaseEnv();
    const result = env.step({ move: "noop" });
    expect(result.state).toEqual({});
    expect(result.reward).toBe(0.0);
    expect(result.done).toBe(false);
    expect(result.info).toEqual({ action: { move: "noop" } });
  });
});

describe("HapticEnv", () => {
  it("returns haptic feedback", () => {
    expect(new HapticEnv().getFeedback().force).toBe(0.0);
  });
});

describe("RobotEnv", () => {
  it("returns robot state", () => {
    expect(new RobotEnv().getRobotState().z).toBe(0.0);
  });
});
