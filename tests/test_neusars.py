import math

from d10z.tta.neusars import (
    Neusar,
    NeusarCluster,
    create_neusar_cluster,
    neusar_consciousness,
)


def test_cluster_coherence_empty_returns_zero():
    cluster = NeusarCluster()
    assert cluster.cluster_coherence == 0.0


def test_collective_process_matches_neusar_count():
    cluster = NeusarCluster([Neusar(), Neusar()])
    inputs = [1 + 0j]  # shorter than the cluster
    output = cluster.collective_process(inputs)
    assert len(output) == 2


def test_create_neusar_cluster_is_reproducible():
    cluster_one = create_neusar_cluster(n_neusars=3, seed=7)
    cluster_two = create_neusar_cluster(n_neusars=3, seed=7)

    states_one = cluster_one.collective_state
    states_two = cluster_two.collective_state

    for left, right in zip(states_one, states_two):
        assert math.isclose(left.real, right.real)
        assert math.isclose(left.imag, right.imag)


def test_neusar_consciousness_handles_no_entanglement():
    cluster = NeusarCluster([Neusar()])
    metrics = neusar_consciousness(cluster)

    assert metrics["integration"] == 0.0
    assert metrics["n_neusars"] == 1
