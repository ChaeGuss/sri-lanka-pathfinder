from data.sample_network import build_sample_graph
from algorithms.bfs import bfs
from algorithms.path_utils import path_distance

def main() -> None:
    graph = build_sample_graph()

    start = "Colombo"
    goal = "Kandy"

    path = bfs(graph, start, goal)

    if path is None:
        print(f"No route found from {start} to {goal}.")
        return

    print("BFS result:")
    print("Route:", "->".join(path))
    print("Edges:", len(path) -1)
    print("Distance:", path_distance(graph, path), "km")
    
    
if __name__ == "__main__":
    main()