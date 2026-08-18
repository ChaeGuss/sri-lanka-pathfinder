import pytest

from utils.geography import geographic_distance
from data.sample_network import build_sample_graph

def test_same_coordinates_have_zero_distance() -> None:
    coordinate = (6.93, 79.85)

    distance = geographic_distance(
        coordinate,
        coordinate,
    )

    assert distance == pytest.approx(0.0)

def test_geographic_distance_is_symmetric() -> None:
    colombo = (6.93, 79.85)
    kandy = (7.29, 80.64)

    forward = geographic_distance(
        colombo,
        kandy,
    )

    reverse = geographic_distance(
        kandy,
        colombo,
    )

    assert forward == pytest.approx(reverse)

def test_colombo_to_kandy_geographic_distance_is_reasonable() -> None:
    colombo = (6.93, 79.85)
    kandy = (7.29, 80.64)

    distance = geographic_distance(
        colombo,
        kandy,
    )

    assert 90 < distance < 100

def test_geographic_distance_does_not_exceed_direct_road_distance() -> None:
    graph = build_sample_graph()

    for town in graph.get_towns():
        town_coordinates = graph.get_coordinates(
            town
        )

        for neighbour, edges in graph.get_neighbours(town).items():
            neighbour_coordinates = graph.get_coordinates(
                neighbour
            )

            estimate = geographic_distance(
                town_coordinates,
                neighbour_coordinates,
            )

            for edge in edges:
                assert estimate <= edge.distance

def test_sample_coordinates_are_valid() -> None:
    graph = build_sample_graph()

    for town in graph.get_towns():
        latitude, longitude = graph.get_coordinates(
            town
        )

        assert -90 <= latitude <= 90
        assert -180 <= longitude <= 180

        