import pytest

from data.sample_network import build_sample_graph
from services.pathfinder import compare_algorithms


from algorithms.path_utils import path_distance

def test_compare_algorithms_returns_all_algorithms() -> None:
    graph = build_sample_graph()

    results = compare_algorithms(
        graph,
        "Colombo",
        "Kandy",
    )

    assert set(results.keys()) == {
        "BFS",
        "Dijkstra",
        "A*",
    }

def test_all_algorithms_find_sample_route() -> None:
    graph = build_sample_graph()

    results = compare_algorithms(
        graph,
        "Colombo",
        "Kandy",
    )

    for result in results.values():
        assert result.path is not None
        assert result.path[0] == "Colombo"
        assert result.path[-1] == "Kandy"

def test_dijkstra_and_astar_have_same_sample_cost() -> None:
    graph = build_sample_graph()

    results = compare_algorithms(
        graph,
        "Colombo",
        "Kandy",
    )

    dijkstra_path = results["Dijkstra"].path
    astar_path = results["A*"].path

    assert dijkstra_path is not None
    assert astar_path is not None

    assert path_distance(
        graph,
        dijkstra_path,
    ) == pytest.approx(
        path_distance(
            graph,
            astar_path,
        )
    )