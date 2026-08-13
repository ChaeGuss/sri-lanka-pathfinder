from data.sample_network import build_sample_graph
from algorithms.bfs import bfs
from algorithms.path_utils import path_distance
from algorithms.dijkstra import dijkstra
from utils.geography import geographic_distance
from algorithms.astar import astar

def main() -> None:
    graph = build_sample_graph()

    path = astar(graph, "Colombo", "Kandy", )

    print(path)

    if path is not None:
        print(path_distance(graph, path))
    
if __name__ == "__main__":
    main()