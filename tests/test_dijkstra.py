import pytest

from algorithms.dijkstra import dijkstra
from algorithms.path_utils import path_distance
from data.sample_network import build_sample_graph
from models.graph import Graph
from algorithms.path_utils import (path_distance, reconstruct_path)

def test_dijkstra_finds_route() -> None:
    graph = build_sample_graph()

    result = dijkstra(
        graph,
        "Colombo",
        "Kandy",
    )

    assert result.path is not None
    assert result.path[0] == "Colombo"
    assert result.path[-1] == "Kandy"

    assert result.explored_nodes > 0

def test_dijkstra_finds_minimum_sample_distance() -> None:
    graph = build_sample_graph()

    result = dijkstra(
        graph,
        "Colombo",
        "Kandy",
    )

    assert result.path is not None

    assert path_distance(graph, result.path) == 125.0

    assert result.explored_nodes > 0

def test_dijkstra_prefers_lower_weight_over_fewer_edges() -> None:
    graph = Graph()

    for town in ["A", "B", "C", "D"]:
        graph.add_town(town)

    graph.add_road("A", "B", 100)
    graph.add_road("B", "D", 100)

    graph.add_road("A", "C", 1)
    graph.add_road("C", "B", 1)

    result = dijkstra(graph, "A", "D")

    assert result.path == [
        "A",
        "C",
        "B",
        "D",
    ]

    assert path_distance(graph, result.path) == 102.0

    assert result.explored_nodes > 0

def test_dijkstra_start_equals_goal() -> None:
    graph = build_sample_graph()

    result = dijkstra(
        graph,
        "Colombo",
        "Colombo",
    )

    assert result.path == ["Colombo"]

    assert result.explored_nodes > 0

def test_dijkstra_rejects_unknown_start() -> None:
    graph = build_sample_graph()

    with pytest.raises(ValueError):
        dijkstra(
            graph,
            "Unknown",
            "Kandy",
        )

def test_dijkstra_rejects_unknown_goal() -> None:
    graph = build_sample_graph()

    with pytest.raises(ValueError):
        dijkstra(
            graph,
            "Colombo",
            "Unknown",
        )

def test_dijkstra_returns_none_when_unreachable() -> None:
    graph = Graph()

    graph.add_town("A")
    graph.add_town("B")
    graph.add_town("C")

    graph.add_road("A", "B", 5)

    result = dijkstra(
        graph,
        "A",
        "C",
    )

    assert result.path is None

    assert result.explored_nodes > 0

def test_dijkstra_handles_direct_road() -> None:
    graph = Graph()

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road("A", "B", 7)

    result = dijkstra(graph, "A", "B")

    assert result.path == ["A", "B"]
    assert path_distance(graph, result.path) == 7.0

    assert result.explored_nodes > 0

def test_dijkstra_can_improve_previous_distance() -> None:
    graph = Graph()

    for town in ["A", "B", "C"]:
        graph.add_town(town)

    graph.add_road("A", "B", 50)
    graph.add_road("A", "C", 10)
    graph.add_road("C", "B", 10)

    result = dijkstra(graph, "A", "B")

    assert result.path == [
        "A",
        "C",
        "B",
    ]

    assert path_distance(graph, result.path) == 20.0

    assert result.explored_nodes > 0

def test_reconstruct_path_from_parents() -> None:
    parents = {
        "Colombo": None,
        "Gampaha": "Colombo",
        "Kegalle": "Gampaha",
        "Kandy": "Kegalle",
    }

    path = reconstruct_path(
        parents,
        "Kandy",
    )

    assert path == [
        "Colombo",
        "Gampaha",
        "Kegalle",
        "Kandy",
    ]

def test_dijkstra_respects_directed_roads() -> None:
    graph = Graph(
        directed=True
    )

    for town in [
        "A",
        "B",
        "C",
    ]:
        graph.add_town(town)

    graph.add_road(
        "A",
        "B",
        5,
    )

    graph.add_road(
        "B",
        "C",
        5,
    )

    forward = dijkstra(
        graph,
        "A",
        "C",
    )

    reverse = dijkstra(
        graph,
        "C",
        "A",
    )

    assert forward.path == [
        "A",
        "B",
        "C",
    ]

    assert reverse.path is None

def test_dijkstra_uses_cheapest_parallel_edge() -> None:
    graph = Graph(
        directed=True
    )

    for town in [
        "A",
        "B",
        "C",
    ]:
        graph.add_town(town)

    graph.add_road(
        "A",
        "B",
        10,
    )

    graph.add_road(
        "A",
        "B",
        3,
    )

    graph.add_road(
        "B",
        "C",
        2,
    )

    result = dijkstra(
        graph,
        "A",
        "C",
    )

    assert result.path == [
        "A",
        "B",
        "C",
    ]

    assert path_distance(
        graph,
        result.path,
    ) == 5.0