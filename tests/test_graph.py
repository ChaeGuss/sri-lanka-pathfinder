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

def test_set_and_get_coordinates() -> None:
    graph = Graph()

    graph.add_town("Colombo")

    graph.set_coordinates(
        "Colombo",
        6.93,
        79.85,
    )

    assert graph.get_coordinates(
        "Colombo"
    ) == (6.93, 79.85)

def test_town_initially_has_no_coordinates() -> None:
    graph = Graph()

    graph.add_town("Colombo")

    assert not graph.has_coordinates("Colombo")

def test_town_has_coordinates_after_setting_them() -> None:
    graph = Graph()

    graph.add_town("Colombo")

    graph.set_coordinates(
        "Colombo",
        6.93,
        79.85,
    )

    assert graph.has_coordinates("Colombo")

def test_invalid_latitude_is_rejected() -> None:
    graph = Graph()
    graph.add_town("Test")

    with pytest.raises(ValueError):
        graph.set_coordinates(
            "Test",
            100,
            80,
        )

def test_invalid_longitude_is_rejected() -> None:
    graph = Graph()
    graph.add_town("Test")

    with pytest.raises(ValueError):
        graph.set_coordinates(
            "Test",
            7,
            200,
        )

def test_coordinates_require_existing_town() -> None:
    graph = Graph()

    with pytest.raises(ValueError):
        graph.set_coordinates(
            "Unknown",
            7,
            80,
        )

def test_get_coordinates_rejects_missing_coordinates() -> None:
    graph = Graph()

    graph.add_town("Colombo")

    with pytest.raises(ValueError):
        graph.get_coordinates("Colombo")

def test_sample_graph_towns_have_coordinates() -> None:
    graph = build_sample_graph()

    for town in graph.get_towns():
        assert graph.has_coordinates(town)

def test_graph_is_undirected_by_default() -> None:
    graph = Graph()

    assert not graph.is_directed()

def test_graph_can_be_directed() -> None:
    graph = Graph(
        directed=True
    )

    assert graph.is_directed()

def test_directed_road_only_adds_forward_edge() -> None:
    graph = Graph(
        directed=True
    )

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        5,
    )

    assert graph.has_road(
        "A",
        "B",
    )

    assert not graph.has_road(
        "B",
        "A",
    )

def test_undirected_road_adds_both_directions() -> None:
    graph = Graph()

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        5,
    )

    assert graph.has_road(
        "A",
        "B",
    )

    assert graph.has_road(
        "B",
        "A",
    )

def test_directed_road_count() -> None:
    graph = Graph(
        directed=True
    )

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        5,
    )

    assert graph.road_count() == 1

def test_two_directed_edges_count_separately() -> None:
    graph = Graph(
        directed=True
    )

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        5,
    )

    graph.add_road(
        "B",
        "A",
        5,
    )

    assert graph.road_count() == 2

def test_directed_graph_validates_without_reverse_edge() -> None:
    graph = Graph(
        directed=True
    )

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        5,
    )

    graph.validate()

    