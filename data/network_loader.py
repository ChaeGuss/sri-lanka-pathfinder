import json
from pathlib import Path
from models.graph import Graph

def load_network(file_path: str | Path, ) -> Graph:
    """Load a road network from a JSON file"""
    path = Path(file_path)

    file_contents = path.read_text(encoding="utf-8")

    data = json.loads(file_contents)

    if not isinstance(data, dict):
        raise ValueError("Network data must be a JSON object")

    if "towns" not in data:
        raise ValueError("Network data is missing 'towns'.")

    if "roads" not in data:
        raise ValueError("Network data is missing 'roads'.")

    if not isinstance(data["towns"], list):
        raise ValueError("'towns' must be a list")

    if not isinstance(data["roads"], list):
            raise ValueError("'roads' must be a list")

    graph = Graph()

    towns = data["towns"]

    for town_data in towns:
        if not isinstance(town_data, dict):
                raise ValueError("Each town must be a JSON object")

        required_fields = {"name", "latitude", "longitude",}

        missing_fields = (required_fields - town_data.keys())

        if missing_fields:
                raise ValueError(f"Town is missing fields: {missing_fields}")
        
        name = town_data["name"]
        latitude = town_data["latitude"]
        longitude = town_data["longitude"]

        graph.add_town(name)

        graph.set_coordinates(name, latitude, longitude,)

        

    roads = data["roads"]

    for road_data in roads:
        if not isinstance(road_data, dict):
            raise ValueError(
                "Each road must be a JSON object."
            )

        required_fields = {"from","to", "distance",
        }

        missing_fields = (required_fields - road_data.keys())

        if missing_fields:
            raise ValueError(f"Road is missing fields: {missing_fields}")

        town_a = road_data["from"]
        town_b = road_data["to"]
        distance = road_data["distance"]

        graph.add_road(town_a, town_b, distance, )

        


    graph.validate()

    return graph