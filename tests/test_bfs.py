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

    path = bfs(graph, "Colombo", "Kandy")

    assert path is not None
    assert path[0] == "Colombo"
    assert path[-1] == "Kandy"
    assert len(path) - 1 == 3

def test_bfs_returns_none_when_goal_is_unreachable() -> None:
    graph = Graph()

    graph.add_town("A")
    graph.add_town("B")
    graph.add_town("C")

    graph.add_road("A", "B", 5)

    path = bfs(graph, "A", "C")

    assert path is None

# Proof BFS finds the path with the fewest edges
def test_bfs_prefers_fewer_edges_not_lower_distance() -> None:
    graph = Graph()

    for town in ["A", "B", "C", "D"]:
        graph.add_town(town)

    graph.add_road("A", "B", 100)
    graph.add_road("B", "D", 100)

    graph.add_road("A", "C", 1)
    graph.add_road("C", "B", 1)

    path = bfs(graph, "A", "D")

    assert path == ["A", "B", "D"]

def test_bfs_can_travel_in_reverse_direction() -> None:
    graph = build_sample_graph()

    path = bfs(graph, "Kandy", "Colombo")

    assert path is not None
    assert path[0] == "Kandy"
    assert path[-1] == "Colombo"