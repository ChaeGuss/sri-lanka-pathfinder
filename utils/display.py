from algorithms.path_utils import path_distance
from models.graph import Graph
from models.search_result import SearchResults


def print_search_result(
    algorithm_name: str,
    graph: Graph,
    result: SearchResults,
) -> None:
    """Print a pathfinding result in a readable format."""

    print(f"\n{algorithm_name}")
    print("-" * len(algorithm_name))

    if result.path is None:
        print("No route found.")
        print(
            "Explored nodes:",
            result.explored_nodes,
        )
        return

    print(
        "Route:",
        " -> ".join(result.path),
    )

    print(
        "Edges:",
        len(result.path) - 1,
    )

    print(
        "Distance:",
        path_distance(
            graph,
            result.path,
        ),
        "km",
    )

    print(
        "Explored nodes:",
        result.explored_nodes,
    )