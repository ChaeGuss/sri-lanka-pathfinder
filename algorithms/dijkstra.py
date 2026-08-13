import heapq

from models.graph import Graph
from algorithms.path_utils import reconstruct_path

def dijkstra(graph: Graph, start: str, goal: str, ) -> list[str] | None:
    """Find the minimum distance path from start to goal using Dijkstra's algorithm."""

    distances = {town: float("inf") for town in graph.get_towns()}

    distances[start] = 0.0

    parents: dict[str, str | None] = {start: None}

    priority_queue: list[tuple[float, str]] = []

    heapq.heappush(priority_queue, (0.0, start), )   # push the starting town with distance 0 into the priority queue

    explored_nodes = 0

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)   # pop the town with the smallest distance from the priority queue
        
        if current_distance > distances[current]:
            continue

        explored_nodes += 1

        if current == goal:
            return reconstruct_path(parents, goal)

        for neighbour, road_distance in graph.get_neighbours(current).items():
            candidate_distance = (current_distance + road_distance)   # calculate the distance to the neighbour through the current town

            if candidate_distance < distances[neighbour]:
                distances[neighbour] = candidate_distance
                parents[neighbour] = current

                heapq.heappush(priority_queue, (candidate_distance, neighbour))

    return None

