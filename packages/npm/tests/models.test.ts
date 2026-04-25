import { describe, expect, it } from "vitest";
import { EmbeddingModel, MotokoModel, SpatialModel } from "../src/models.js";

describe("EmbeddingModel", () => {
  it("encodes text length", () => {
    expect(new EmbeddingModel().encode("abc")).toEqual([3]);
  });
});

describe("MotokoModel", () => {
  it("returns null prediction", () => {
    expect(new MotokoModel().predict({ x: 1 }).prediction).toBeNull();
  });
});

describe("SpatialModel", () => {
  it("computes euclidean distance", () => {
    expect(new SpatialModel().distance([0, 0, 0], [3, 4, 0])).toBe(5.0);
  });
});
