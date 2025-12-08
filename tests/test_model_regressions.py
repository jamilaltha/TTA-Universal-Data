from d10z.models.tta_model import TTAModel


def test_regression_sparc_r2_threshold() -> None:
    model = TTAModel()
    r2 = model.evaluate_on_sparc_sample(n_galaxies=20)
    assert r2 > 0.8  # placeholder: ajusta a tu claim real
