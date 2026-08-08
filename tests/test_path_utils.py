from algorithms.path_utils import path_distance
from data.sample_network import build_sample_graph

def test_path_distance_calculates_total_distance() -> None:
    graph = build_sample_graph()

    path = [
        "Colombo",
        "Gampaha",
        "Kegalle",
        "Kandy",
    ]

    distance = path_distance(graph, path)

    assert distance == 125.0

def test_single_town_path_has_zero_distance() -> None:
    graph = build_sample_graph()

    distance = path_distance(graph, ["Colombo"])

    assert distance == 0.0

def test_direct_path_distance() -> None:
    graph = build_sample_graph()

    distance = path_distance(
        graph,
        ["Colombo", "Kaduwela"],
    )

    assert distance == 16.0