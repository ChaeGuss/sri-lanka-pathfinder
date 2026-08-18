import pytest
from data.osm_converter import load_osm_style_network
from models.graph import Graph

def test_osm_converter_loads_nodes() -> None:
    graph = load_osm_style_network(
        "data/raw_osm_sample.json"
    )

    assert graph.town_count() == 4

def test_osm_way_becomes_graph_edges() -> None:
    graph = load_osm_style_network(
        "data/raw_osm_sample.json"
    )

    assert graph.has_road(
        "1001",
        "1002",
    )

    assert graph.has_road(
        "1002",
        "1003",
    )

def test_osm_node_coordinates_are_loaded() -> None:
    graph = load_osm_style_network(
        "data/raw_osm_sample.json"
    )

    assert graph.get_coordinates(
        "1001"
    ) == (
        6.9271,
        79.8612,
    )

def test_two_way_osm_road_creates_both_directions() -> None:
    graph = load_osm_style_network(
        "data/raw_osm_sample.json"
    )

    assert graph.has_road(
        "1001",
        "1002",
    )

    assert graph.has_road(
        "1002",
        "1001",
    )

def test_oneway_osm_road_only_creates_forward_edge() -> None:
    graph = load_osm_style_network(
        "data/raw_osm_sample.json"
    )

    assert graph.has_road(
        "1003",
        "1004",
    )

    assert not graph.has_road(
        "1004",
        "1003",
    )

def test_get_distance_returns_minimum_parallel_edge() -> None:
    graph = Graph(
        directed=True
    )

    graph.add_town("A")
    graph.add_town("B")

    graph.add_road(
        "A",
        "B",
        9,
    )

    graph.add_road(
        "A",
        "B",
        4,
    )

    assert graph.get_distance(
        "A",
        "B",
    ) == 4.0