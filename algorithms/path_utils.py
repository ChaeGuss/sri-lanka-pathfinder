from models.graph import Graph

def path_distance(graph: Graph, path: list[str]) -> float:
    """Calculate the total distance of a path"""
    total = 0.0

    for i in range(len(path) - 1):
        town_a = path[i]
        town_b = path[i + 1]

        total += graph.get_distance(town_a, town_b)

    return total