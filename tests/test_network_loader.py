import pytest
import json

from data.network_loader import load_network
from data.sample_network import build_sample_graph

def test_load_sample_network() -> None:
    graph = load_network(
        "data/sample_network.json"
    )

    assert graph.town_count() == 10
    assert graph.road_count() == 13

def test_loaded_network_contains_coordinates() -> None:
    graph = load_network(
        "data/sample_network.json"
    )

    for town in graph.get_towns():
        assert graph.has_coordinates(town)

def test_loaded_network_contains_known_road() -> None:
    graph = load_network(
        "data/sample_network.json"
    )

    assert graph.has_road(
        "Colombo",
        "Kaduwela",
    )

def test_loader_rejects_missing_towns(tmp_path,) -> None:
    file_path = (
    tmp_path / "network.json")

    file_path.write_text(
        """
        {
        "roads": []
        }
        """,
        encoding="utf-8",
    )

    with pytest.raises(ValueError,match="missing 'towns'",):
        load_network(file_path)

def test_loader_rejects_invalid_json(
    tmp_path,
) -> None:
    file_path = (
        tmp_path / "network.json"
    )

    file_path.write_text(
        "{ invalid json }",
        encoding="utf-8",
    )

    with pytest.raises(
        json.JSONDecodeError
    ):
        load_network(file_path)

def test_loader_rejects_missing_file(
    tmp_path,
) -> None:
    file_path = (
        tmp_path / "missing.json"
    )

    with pytest.raises(
        FileNotFoundError
    ):
        load_network(file_path)

def test_loader_rejects_town_missing_name(
    tmp_path,
) -> None:
    file_path = (
        tmp_path / "network.json"
    )

    file_path.write_text(
        """
        {
          "towns": [
            {
              "latitude": 6.93,
              "longitude": 79.85
            }
          ],
          "roads": []
        }
        """,
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_network(file_path)

def test_loader_rejects_negative_road_distance(
    tmp_path,
) -> None:
    network_data = {
        "towns": [
            {
                "name": "A",
                "latitude": 0,
                "longitude": 0,
            },
            {
                "name": "B",
                "latitude": 0,
                "longitude": 1,
            },
        ],
        "roads": [
            {
                "from": "A",
                "to": "B",
                "distance": -5,
            },
        ],
    }

    file_path = (
        tmp_path / "network.json"
    )

    file_path.write_text(
        json.dumps(network_data),
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_network(file_path)

def test_json_network_matches_old_sample_builder() -> None:
    old_graph = build_sample_graph()

    new_graph = load_network(
        "data/sample_network.json"
    )

    assert (
        old_graph.town_count()
        == new_graph.town_count()
    )

    assert (
        old_graph.road_count()
        == new_graph.road_count()
    )

    assert (
        old_graph.get_towns()
        == new_graph.get_towns()
    )