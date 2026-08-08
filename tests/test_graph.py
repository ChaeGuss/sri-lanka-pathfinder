import pytest

from models.graph import Graph
from data.sample_network import build_sample_graph

def test_new_graph_is_empty() -> None:
    graph = Graph()

    assert graph.town_count() == 0
    assert graph.road_count() == 0

def test_add_town() -> None:
    graph = Graph()

    graph.add_town("Colombo")

    assert graph.has_town("Colombo")
    assert graph.town_count() == 1

def test_get_towns_returns_added_towns() -> None:
    graph = Graph()

    graph.add_town("Colombo")
    graph.add_town("Kandy")
    graph.add_town("Gampaha")

    assert graph.get_towns() == [
        "Colombo",
        "Kandy",
        "Gampaha",
    ]

def test_duplicate_town_is_rejected() -> None:
    graph = Graph()

    graph.add_town("Colombo")

    with pytest.raises(ValueError):
        graph.add_town("Colombo")

def test_town_name_whitespace_is_stripped() -> None:
    graph = Graph()

    graph.add_town("  Colombo  ")

    assert graph.has_town("Colombo")
    assert graph.get_towns() == ["Colombo"]

def test_add_road_connects_both_towns() -> None:
    graph = Graph()

    graph.add_town("Colombo")
    graph.add_town("Kaduwela")

    graph.add_road("Colombo", "Kaduwela", 16)

    assert graph.has_road("Colombo", "Kaduwela")
    assert graph.has_road("Kaduwela", "Colombo")

def test_road_distance_is_stored_in_both_directions() -> None:
    graph = Graph()

    graph.add_town("Colombo")
    graph.add_town("Kaduwela")

    graph.add_road("Colombo", "Kaduwela", 16)

    assert graph.get_distance("Colombo", "Kaduwela") == 16.0
    assert graph.get_distance("Kaduwela", "Colombo") == 16.0

def test_undirected_road_is_counted_once() -> None:
    graph = Graph()

    graph.add_town("Colombo")
    graph.add_town("Kaduwela")

    graph.add_road("Colombo", "Kaduwela", 16)

    assert graph.road_count() == 1

def test_duplicate_road_is_rejected() -> None:
    graph = Graph()

    graph.add_town("Colombo")
    graph.add_town("Kaduwela")

    graph.add_road("Colombo", "Kaduwela", 16)

    with pytest.raises(ValueError):
        graph.add_road("Colombo", "Kaduwela", 16)

def test_sample_graph_has_expected_size() -> None:
    graph = build_sample_graph()

    assert graph.town_count() == 10
    assert graph.road_count() == 13