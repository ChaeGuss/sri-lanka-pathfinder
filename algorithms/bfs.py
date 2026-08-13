from collections import deque

from models.graph import Graph
from algorithms.path_utils import reconstruct_path

def bfs_traversal(graph: Graph, start: str) -> list[str]:
    """Return towns in breadth-first traversal order."""
    if not graph.has_town(start):
        raise ValueError(f"Unknown starting town: {start}")

    queue = deque([start])
    visited = {start}
    traversal_order = []

    while queue:
        current = queue.popleft()
        print("Current:", current)

        traversal_order.append(current)
        print("Queue:", list(queue))

        for neighbour in graph.get_neighbours(current):   # iterates over keys of the dictionary
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                print("Visited:", visited)

    return traversal_order

# path search function using BFS
def bfs(graph: Graph, start: str, goal: str) -> list[str] | None:
    """Find a path from start to goal using breadth-first search."""

    explored_nodes = 0

    if not graph.has_town(start):
        raise ValueError(f"Unknown start town: {start}")

    if not graph.has_town(goal):
        raise ValueError(f"Unknown goal town: {goal}")

    if start == goal:
        return [start]

    queue = deque([start])
    visited = {start}
    parents: dict[str, str | None] = {start: None}

    while queue:
        current = queue.popleft()
        explored_nodes += 1

        print("BFS explored:", explored_nodes,)

        for neighbour in graph.get_neighbours(current):
            if neighbour in visited:
                continue

            visited.add(neighbour)
            parents[neighbour] = current
            queue.append(neighbour)

            if neighbour == goal:
                return reconstruct_path(parents, goal) # return a real route

            queue.append(neighbour)

    return None  # no path found