import math
import pytest

from d10z.bigstart.flower_of_life import (
    FlowerOfLife,
    create_flower_geometry,
    flower_coherence,
)


def test_geometry_positions_and_center_adjustment():
    center = [1.0, -1.0, 0.5]
    flower = create_flower_geometry(scale=2.0, center=center, z_offset=0.3)

    assert isinstance(flower, FlowerOfLife)
    assert len(flower.positions) == 19
    assert all(len(node) == 3 for node in flower.positions)
    assert flower.center == pytest.approx([1.0, -1.0, 0.8])

    # All first ring nodes should be exactly scale distance from center
    distances = [math.dist(node, flower.center) for node in flower.first_ring]
    assert all(math.isclose(distance, 2.0) for distance in distances)

    # Second ring should contain two distinct radii: 2 * scale and sqrt(3) * scale
    radii = {round(math.dist(node, flower.center), 6) for node in flower.second_ring}
    assert radii == {
        round(4.0, 6),
        round(math.sqrt(12), 6),
    }


def test_connectivity_structure_and_symmetry():
    flower = create_flower_geometry()
    connectivity = flower.get_connectivity()

    # Matrix should be symmetric
    for i in range(flower.n_nodes):
        for j in range(flower.n_nodes):
            assert connectivity[i][j] == connectivity[j][i]

    # Center connects to all first ring nodes with weight 1.0
    assert connectivity[0][1:7] == [1.0] * 6

    # First ring neighbors are connected
    for i in range(1, 7):
        next_i = 1 + (i % 6)
        assert connectivity[i][next_i] == pytest.approx(1.0)

    # Second ring connectivity uses reduced weight
    second_ring_weights = connectivity[7:19]
    nonzero = [value for row in second_ring_weights for value in row[7:19] if value > 0]
    assert all(math.isclose(value, 0.6) for value in nonzero)


def test_flower_coherence_weighting_and_validation():
    phases = [0.0] * 19
    assert flower_coherence(phases) == pytest.approx(1.0)

    with pytest.raises(ValueError):
        flower_coherence([0.0] * 5)

    # Introduce phase differences and ensure coherence decreases
    phases[1:7] = [math.pi] * 6
    assert flower_coherence(phases) < 1.0
