from data.sample_network import build_sample_graph
from algorithms.bfs import bfs
from algorithms.path_utils import path_distance
from algorithms.dijkstra import dijkstra

def main() -> None:
    graph = build_sample_graph()

    start = "Colombo"
    goal = "Kandy"

    bfs_path = bfs(graph, start, goal)
    dijkstra_path = dijkstra(graph, start, goal)

    if bfs_path is not None:
        print("\nBFS")
        print("Route:", " -> ".join(bfs_path))
        print("Edges:", len(bfs_path) - 1)
        print(
            "Distance:",
            path_distance(graph, bfs_path),
            "km",
        )

    if dijkstra_path is not None:
        print("\nDijkstra")
        print(
            "Route:",
            " -> ".join(dijkstra_path),
        )
        print(
            "Edges:",
            len(dijkstra_path) - 1,
        )
        print(
            "Distance:",
            path_distance(
                graph,
                dijkstra_path,
            ),
            "km",
        )


if __name__ == "__main__":
    main()