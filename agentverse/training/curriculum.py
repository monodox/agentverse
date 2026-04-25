class Curriculum:
    """Tracks curriculum difficulty."""

    def __init__(self, difficulty: int = 1) -> None:
        self.difficulty = difficulty

    def advance(self) -> int:
        self.difficulty += 1
        return self.difficulty

