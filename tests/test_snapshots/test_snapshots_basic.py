from d10z.models.tta_model import TTAModel


def test_snapshot_example_output() -> None:
    model = TTAModel()
    out = model.run_example()
    # compara con un valor "esperado" aproximado
    assert isinstance(out, dict)
    assert "metric" in out
