import pytest

from algorithms.astar import astar
from algorithms.dijkstra import dijkstra
from algorithms.path_utils import path_distance
from data.sample_network import build_sample_graph
from models.graph import Graph

def test_astar_finds_route() -> None:
    graph = build_sample_graph()

    result = astar(
        graph,
        "Colombo",
        "Kandy",
    )

    assert result.path is not None
    assert result.path[0] == "Colombo"
    assert result.path[-1] == "Kandy"
    assert result.explored_nodes > 0

def test_astar_matches_dijkstra_distance() -> None:
    graph = build_sample_graph()

    astar_result = astar(
        graph,
        "Colombo",
        "Kandy",
    )

    dijkstra_result = dijkstra(
        graph,
        "Colombo",
        "Kandy",
    )

    assert astar_result.path is not None
    assert dijkstra_result.path is not None

    assert path_distance(
        graph,
        astar_result.path,
    ) == pytest.approx(
        path_distance(
            graph,
            dijkstra_result.path,
        )
    )

def test_astar_start_equals_goal() -> None:
    graph = build_sample_graph()

    result = astar(
        graph,
        "Colombo",
        "Colombo",
    )

    assert result.path == ["Colombo"]

def test_astar_rejects_unknown_start() -> None:
    graph = build_sample_graph()

    with pytest.raises(ValueError):
        astar(
            graph,
            "Unknown",
            "Kandy",
        )

def test_astar_rejects_unknown_goal() -> None:
    graph = build_sample_graph()

    with pytest.raises(ValueError):
        astar(
            graph,
            "Colombo",
            "Unknown",
        )

def test_astar_requires_coordinates() -> None:
    graph = Graph()

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        5,
    )

    with pytest.raises(ValueError):
        astar(
            graph,
            "A",
            "B",
        )

def test_astar_returns_none_when_unreachable() -> None:
    graph = Graph()

    for town in ["A", "B", "C"]:
        graph.add_town(town)

    graph.set_coordinates(
        "A",
        0,
        0,
    )

    graph.set_coordinates(
        "B",
        0,
        0.01,
    )

    graph.set_coordinates(
        "C",
        0,
        0.02,
    )

    graph.add_road(
        "A",
        "B",
        5,
    )

    result = astar(
        graph,
        "A",
        "C",
    )

    assert result.path is None

    assert result.explored_nodes > 0