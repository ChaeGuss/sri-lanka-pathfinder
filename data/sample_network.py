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

    return graph