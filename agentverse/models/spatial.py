class SpatialModel:
    """Simple spatial model placeholder."""

    def distance(self, a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
        return sum((left - right) ** 2 for left, right in zip(a, b)) ** 0.5

