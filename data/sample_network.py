from models.graph import Graph

def build_sample_graph() -> Graph:
    """Create and return the initial sample Sri lankan road graph"""
    graph = Graph()

    towns = [
        "Colombo",
        "Kaduwela",
        "Malabe",
        "Kottawa",
        "Homagama",
        "Avissawella",
        "Ratnapura",
        "Kegalle",
        "Kandy",
        "Gampaha",
    ]

    for town in towns:
        graph.add_town(town)

    roads = [
        ("Colombo", "Kaduwela", 16),
        ("Colombo", "Kottawa", 21),
        ("Colombo", "Gampaha", 28),
        ("Kaduwela", "Malabe", 8),
        ("Kaduwela", "Avissawella", 35),
        ("Malabe", "Kottawa", 12),
        ("Kottawa", "Homagama", 7),
        ("Homagama", "Avissawella", 32),
        ("Avissawella", "Ratnapura", 44),
        ("Avissawella", "Kegalle", 40),
        ("Gampaha", "Kegalle", 55),
        ("Kegalle", "Kandy", 42),
        ("Ratnapura", "Kandy", 90),
    ]

    for town_a, town_b, distance in roads:
        graph.add_road(town_a, town_b, distance)

    coordinates = {
        "Colombo": (6.93, 79.85),
        "Kaduwela": (6.93, 79.98),
        "Malabe": (6.90, 79.96),
        "Kottawa": (6.84, 79.96),
        "Homagama": (6.84, 80.00),
        "Avissawella": (6.95, 80.21),
        "Ratnapura": (6.68, 80.40),
        "Kegalle": (7.25, 80.35),
        "Kandy": (7.29, 80.64),
        "Gampaha": (7.09, 80.00),
    }

    for town, (latitude, longitude,) in coordinates.items(): graph.set_coordinates(town, latitude, longitude,)

    return graph