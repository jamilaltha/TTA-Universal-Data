from d10z.models.tta_model import TTAModel  # asumiendo


def test_rotation_curve_monotonic_at_outer_radius() -> None:
    model = TTAModel()
    radii, velocities = model.example_rotation_curve()
    assert len(radii) == len(velocities)
    # Skeleton simple: la velocidad no debe crecer sin control en las últimas N
    assert velocities[-1] <= velocities[-2] * 1.2
