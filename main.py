from data.sample_network import build_sample_graph
from services.pathfinder import compare_algorithms
from utils.display import print_search_result


def main() -> None:
    """Run the Sri Lanka pathfinding application."""
    graph = build_sample_graph()

    start = "Colombo"
    goal = "Kandy"

    results = compare_algorithms(
        graph,
        start,
        goal,
    )

    print(
        f"Route comparison: {start} -> {goal}"
    )

    for algorithm_name, result in results.items():
        print_search_result(
            algorithm_name,
            graph,
            result,
        )


if __name__ == "__main__":
    main()