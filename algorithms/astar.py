import heapq

from algorithms.path_utils import reconstruct_path
from models.graph import Graph
from utils.geography import geographic_distance

def _heuristic(graph: Graph, town: str, goal: str, ) -> float:
    """Estimate remaining distance from a town to the goal"""
    town_coordinates = graph.get_coordinates(town)
    goal_coordinates = graph.get_coordinates(goal)

    return geographic_distance(town_coordinates, goal_coordinates)

def astar(graph: Graph, start: str, goal: str, ) -> list[str] | None:
    """Find a minimum distance path using A* search"""

    if not graph.has_town(start):
        raise ValueError(f"Unknown start town: {start}")

    if not graph.has_town(goal):
        raise ValueError(f"Unknown goal town: {goal}")

    if start == goal:
        return [start]

    if not graph.has_coordinates(start):
        raise ValueError(f"No corrdinates stored for start town: {start}")

    if not graph.has_coordinates(goal):
        raise ValueError(f"No coordinates stored for goal town: {goal}")

    g_scores = {town: float("inf") for town in graph.get_towns()}
    g_scores[start] = 0.0               #best known road cost from start → each town

    parents: dict[str, str | None] = { start: None}

    start_priority = _heuristic(graph, start, goal)

    priority_queue: list[tuple[float, float, str]] = []

    heapq.heappush(priority_queue, (start_priority, 0.0, start),)

    explored_nodes = 0

    while priority_queue:
        current_priority, queued_g, current = heapq.heappop(priority_queue)

        if queued_g > g_scores[current]:
          continue

        explored_nodes += 1

        if current == goal:
            return reconstruct_path(parents, goal,)

        for neighbour, road_distance in graph.get_neighbours(current).items():

            if not graph.has_coordinates(neighbour):
                raise ValueError(f"No coordinates stored for town: {neighbour}")

            candidate_g = (g_scores[current] + road_distance)

            if candidate_g < g_scores[neighbour]:
                g_scores[neighbour] = candidate_g
                parents[neighbour] = current

                h_score = _heuristic(graph, neighbour, goal, )     #estimated remaining geographic distance

                f_score = candidate_g + h_score

                heapq.heappush(priority_queue, (f_score, candidate_g, neighbour,), )

    return None

