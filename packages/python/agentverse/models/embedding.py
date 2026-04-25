class EmbeddingModel:
    """Simple embedding placeholder."""

    def encode(self, text: str) -> list[float]:
        return [float(len(text))]
