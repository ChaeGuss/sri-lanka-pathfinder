from dataclasses import dataclass

@dataclass
class SearchResults:
    """Store the result and statistics of a pathfinding search"""

    path: list[str] | None
    explored_nodes: int