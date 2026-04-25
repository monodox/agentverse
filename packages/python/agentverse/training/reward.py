class RewardFunction:
    """Basic reward function placeholder."""

    def __call__(self, success: bool) -> float:
        return 1.0 if success else 0.0
