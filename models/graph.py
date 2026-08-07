class Graph:
    """Represent an undirected, weighted graph of towns and roads."""

    def __init__(self) -> None:
        """Create an empty graph."""
        self._adjacency: dict[str, dict[str, float]] = {}

    def add_town(self, town: str) -> None:
        """Add a town to the graph."""
        if not isinstance(town, str):
            raise TypeError("Town name must be a string.")

        town = town.strip()  # Remove whitespace surrounding town name

        if not town:
            raise ValueError("Town name must not be empty.")

        if town in self._adjacency:
            raise ValueError(f"Town already exists: {town}")

        self._adjacency[town] = {}

    def has_town(self, town: str) -> bool:
        """Return whether a town exists in the graph."""
        return town in self._adjacency

    def town_count(self) -> int:
        """Return number of towns in the graph"""
        return len(self._adjacency)

    def get_towns(self) -> list[str]:
        """Return all town names in insertion order."""
        return list(self._adjacency.keys())

    def _require_town(self, town: str) -> None:
        """Raise an error if town does not exist."""
        if town not in self._adjacency:
            raise ValueError(f"Unknown town: {town}")

    def add_road(self, town_a: str, town_b: str, distance: float) -> None:
        """Add an undirected weighted road between two existing towns"""
        self._require_town(town_a)
        self._require_town(town_b)

        if town_a == town_b:
            raise ValueError("A town cannot have a road to itself")

        if isinstance(distance, bool) or not isinstance(distance, (int, float)):
            raise TypeError("Road distance must be a number")

        if distance <= 0:
            raise ValueError("Road distance must be greater than 0")

        if town_b in self._adjacency[town_a]:
            raise ValueError(f"Road already exists between {town_a} and {town_b}")

        numeric_distance = float(distance)

        self._adjacency[town_a][town_b] = numeric_distance
        self._adjacency[town_b][town_a] = numeric_distance

    def get_neighbours(self, town: str) -> dict[str, float]:
        """Return a copy of a town's neighbours and road distances"""
        self._require_town(town)
        return self._adjacency[town].copy()

    def has_road(self, town_a: str, town_b: str) -> bool:
        """Return whether a direct road exists between two towns"""
        self._require_town(town_a)
        self._require_town(town_b)

        return town_b in self._adjacency[town_a]

    def get_distance(self, town_a: str, town_b: str) -> float:
        """Return the distance of the direct road between the two towns"""
        self._require_town(town_a)
        self._require_town(town_b)

        if town_b not in self._adjacency[town_a]:
            raise ValueError(f"No direct road exists between {town_a} and {town_b}")

        return self._adjacency[town_a][town_b]

    def road_count(self) -> int:
        """Return the number of undirected roads in the graph"""
        neighbour_entries = sum(len(neighbours) for neighbours in self._adjacency.values())

        return neighbour_entries // 2

    def __str__(self) -> str:
        """Return a readble summary of the graph"""
        return(f"Graph(towns={self.town_count()}, roads={self.road_count()})")

