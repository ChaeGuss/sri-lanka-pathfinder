import json
from pathlib import Path

from models.graph import Graph
from utils.geography import geographic_distance


def load_osm_style_network(file_path: str | Path,) -> Graph:
    """Convert an OSM-style JSON file into a Graph."""

    path = Path(file_path)

    file_contents = path.read_text(encoding="utf-8")

    data = json.loads(file_contents)

    if not isinstance(data, dict):
        raise ValueError("OSM-style data must be a JSON object.")

    if "nodes" not in data:
        raise ValueError("OSM-style data is missing 'nodes'.")

    if "ways" not in data:
        raise ValueError("OSM-style data is missing 'ways'.")

    if not isinstance(data["nodes"], list):
        raise ValueError("'nodes' must be a list.")

    if not isinstance(data["ways"], list):
        raise ValueError("'ways' must be a list.")

    graph = Graph()

    node_lookup = {}

    for node_data in data["nodes"]:
        node_id = node_data["id"]
        latitude = node_data["latitude"]
        longitude = node_data["longitude"]

        node_lookup[node_id] = (latitude,longitude,)

        graph_node_id = str(node_id)

        graph.add_town(graph_node_id)

        graph.set_coordinates(graph_node_id, latitude, longitude, )

    for way_data in data["ways"]:
        tags = way_data.get("tags", {} )

        if "highway" not in tags:
            continue

        way_nodes = way_data["nodes"]

        if len(way_nodes) < 2:
            continue

        for index in range(
            len(way_nodes) - 1
        ):
            node_a_id = way_nodes[index]
            node_b_id = way_nodes[index + 1]

            if node_a_id not in node_lookup:
                raise ValueError(f"Way references unknown node: {node_a_id}")

            if node_b_id not in node_lookup:
                raise ValueError(f"Way references unknown node: {node_b_id}")

            coordinate_a = node_lookup[node_a_id]

            coordinate_b = node_lookup[node_b_id]

            distance = geographic_distance(coordinate_a,coordinate_b,)

            town_a = str(node_a_id)
            town_b = str(node_b_id)

            if graph.has_road(town_a,town_b,):
                continue

            graph.add_road(town_a, town_b, distance, )

    graph.validate()

    return graph