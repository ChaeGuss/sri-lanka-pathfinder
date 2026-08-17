import pytest

from algorithms.bfs import bfs, bfs_traversal
from data.sample_network import build_sample_graph
from models.graph import Graph

def test_bfs_traversal_starts_with_source() -> None:
    graph = build_sample_graph()

    traversal = bfs_traversal(graph, "Colombo")

    assert traversal[0] == "Colombo"

def test_bfs_traversal_visits_every_sample_town() -> None:
    graph = build_sample_graph()

    traversal = bfs_traversal(graph, "Colombo")

    assert len(traversal) == 10
    assert set(traversal) == set(graph.get_towns())

def test_bfs_finds_colombo_to_kandy_path() -> None:
    graph = build_sample_graph()

    result = bfs(graph, "Colombo", "Kandy")

    assert result.path is not None
    assert result.path[0] == "Colombo"
    assert result.path[-1] == "Kandy"
    assert len(result.path) - 1 == 3
    assert result.explored_nodes > 0

def test_bfs_returns_none_when_goal_is_unreachable() -> None:
    graph = Graph()

    graph.add_town("A")
    graph.add_town("B")
    graph.add_town("C")

    graph.add_road("A", "B", 5)

    result = bfs(graph, "A", "C")

    assert result.path is None
    assert result.explored_nodes == 2

# Proof BFS finds the path with the fewest edges
def test_bfs_prefers_fewer_edges_not_lower_distance() -> None:
    graph = Graph()

    for town in ["A", "B", "C", "D"]:
        graph.add_town(town)

    graph.add_road("A", "B", 100)
    graph.add_road("B", "D", 100)

    graph.add_road("A", "C", 1)
    graph.add_road("C", "B", 1)

    result = bfs(graph, "A", "D")

    assert result.path == ["A", "B", "D"]

    assert result.explored_nodes > 0

def test_bfs_can_travel_in_reverse_direction() -> None:
    graph = build_sample_graph()

    result = bfs(graph, "Kandy", "Colombo")

    assert result.path is not None
    assert result.path[0] == "Kandy"
    assert result.path[-1] == "Colombo"
    assert result.explored_nodes > 0

def test_bfs_start_equals_goal() -> None:
    graph = build_sample_graph()

    result = bfs(
        graph,
        "Colombo",
        "Colombo",
    )

    assert result.path == ["Colombo"]
    assert result.explored_nodes == 1

def test_bfs_respects_directed_roads() -> None:
    graph = Graph(
        directed=True
    )

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        1,
    )

    forward = bfs(
        graph,
        "A",
        "B",
    )

    reverse = bfs(
        graph,
        "B",
        "A",
    )

    assert forward.path == [
        "A",
        "B",
    ]

    assert reverse.path is None