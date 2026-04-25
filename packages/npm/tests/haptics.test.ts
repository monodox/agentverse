import { describe, expect, it } from "vitest";
import { ForceSimulator, SensorSimulator, TouchSimulator } from "../src/haptics.js";

describe("ForceSimulator", () => {
  it("computes force as mass * acceleration", () => {
    expect(new ForceSimulator().computeForce(2.0, 3.0)).toBe(6.0);
  });
});

describe("TouchSimulator", () => {
  it("detects contact above threshold", () => {
    expect(new TouchSimulator().detectContact(0.2)).toBe(true);
  });
});

describe("SensorSimulator", () => {
  it("returns default sensor readings", () => {
    expect(new SensorSimulator().read().pressure).toBe(0.0);
  });
});
