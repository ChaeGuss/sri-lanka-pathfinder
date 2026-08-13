from algorithms.astar import astar
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from models.graph import Graph
from models.search_result import SearchResults

def compare_algorithms(graph: Graph, start: str, goal: str,) -> dict[str, SearchResults]:
    """Run all pathfinding algorithms for the same route"""

    return {"BFS": bfs(graph, start, goal,),
            "Dijkstra": dijkstra(graph, start, goal,),
            "A*": astar(graph, start, goal),}