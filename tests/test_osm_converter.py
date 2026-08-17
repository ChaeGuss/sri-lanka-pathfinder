import pytest
from data.osm_converter import load_osm_style_network

def test_osm_converter_loads_nodes() -> None:
    graph = load_osm_style_network(
        "data/raw_osm_sample.json"
    )

    assert graph.town_count() == 3

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

