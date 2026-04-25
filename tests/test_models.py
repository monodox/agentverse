from agentverse.models import EmbeddingModel, MotokoModel, SpatialModel


def test_embedding_model() -> None:
    assert EmbeddingModel().encode("abc") == [3.0]


def test_motoko_and_spatial_models() -> None:
    assert MotokoModel().predict({"x": 1})["prediction"] is None
    assert SpatialModel().distance((0, 0, 0), (3, 4, 0)) == 5.0

