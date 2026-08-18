from models.edge import Edge

class Graph:
    """Represent an undirected, weighted graph of towns and roads."""

    def __init__(self, directed: bool = False) -> None:
        """Create an empty graph."""

        if not isinstance(directed, bool):
            raise TypeError("directed must be a boolean")
        
        self._directed = directed
        self._adjacency: dict[str, dict[str, list[Edge]], ] = {}
        self._coordinates: dict[str, tuple[float, float], ] = {}

    def is_directed(self) -> bool:
        """Return whether the graph is directed"""
        return self._directed

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

    def add_road(self, town_a: str, town_b: str, distance: float, *,
                 way_id: str | None = None, name: str | None = None, highway_type: str | None = None,) -> None:
        """Add an undirected weighted road between two existing towns"""
        self._require_town(town_a)
        self._require_town(town_b)

        if town_a == town_b:
            raise ValueError("A town cannot have a road to itself")

        if isinstance(distance, bool) or not isinstance(distance, (int, float)):
            raise TypeError("Road distance must be a number")

        if distance <= 0:
            raise ValueError("Road distance must be greater than 0")

        edge = Edge(distance=float(distance), way_id=way_id, name=name, highway_type=highway_type,)

        self._add_directed_edge(town_a, town_b, edge, )

        if not self._directed:
            reverse_edge = Edge(distance=float(distance), way_id=way_id, name=name, highway_type=highway_type,)

            self._add_directed_edge(town_b, town_a, reverse_edge, )

    def _add_directed_edge(self, town_a: str, town_b: str, edge: Edge, ) -> None:
        if town_b not in self._adjacency[town_a]:
            self._adjacency[town_a][town_b] = []

        self._adjacency[town_a][town_b].append(edge)

    def get_neighbours(self, town: str) -> dict[str, list[Edge]]:
        """Return a copy of a town's neighbours and road distances"""
        self._require_town(town)
        return {neighbour: edges.copy()
                for neighbour, edges in self._adjacency[town].items()}

    def has_road(self, town_a: str, town_b: str) -> bool:
        """Return whether a direct road exists between two towns"""
        self._require_town(town_a)
        self._require_town(town_b)

        return town_b in self._adjacency[town_a]

    def get_distance(self, town_a: str, town_b: str) -> float:
        """Return the distance"""
        self._require_town(town_a)
        self._require_town(town_b)

        edges = self._adjacency[town_a].get(town_b)

        if not edges:
            raise ValueError(f"No direct road exists from " f"{town_a} to {town_b}")

        return min(edge.distance for edge in edges)

    def get_edges(self, town_a: str, town_b: str, ) -> list[Edge]:
        """Return all direct edges from one node to another"""

        self._require_town(town_a)
        self._require_town(town_b)

        edges = self._adjacency[town_a].get(town_b)

        if edges is None:
            return []

        return edges.copy()

    def road_count(self) -> int:
        """Return the number of roads in the graph"""
        edge_entries = sum(len(edges) for neighbours in self._adjacency.values()
                                   for edges in neighbours.values())

        if self._directed:
            return edge_entries

        return edge_entries // 2

    def __str__(self) -> str:
        """Return a readble summary of the graph"""
        return(f"Graph(towns={self.town_count()}, roads={self.road_count()})")

    def set_coordinates(self, town: str, latitude: float, longitude: float, ) -> None:
        """Set geographic coordinates for an existing town"""
        self._require_town(town)

        if isinstance(latitude, bool) or not isinstance(latitude, (int, float), ):
            raise TypeError("Latitude must be a number")

        if isinstance(longitude, bool) or not isinstance(longitude, (int, float), ):
            raise TypeError("Longitude must be a number")

        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees") # Latitude measures north/south angular position, with the Equator at 0° and poles at ±90°

        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees") # Longitude measures east/west angular position, with the Prime Meridian at 0° and the International Date Line at ±180°

        self._coordinates[town] = (float(latitude), float(longitude), )

    def has_coordinates(self, town: str) -> bool:
        """Return whether a town has geographic coordinates set"""
        self._require_town(town)

        return town in self._coordinates

    def get_coordinates(self, town: str, ) -> tuple[float, float]:
        """Return the latitude and logitude of a town"""
        self._require_town(town)

        if town not in self._coordinates:
            raise ValueError(f"Coordinates not stored for town: {town}")

        return self._coordinates[town]

    def validate(self) -> None:
        """Raise an error if the graph is internally inconsistent."""

        for town, neighbours in self._adjacency.items():

            if town in neighbours:
                raise ValueError(
                    f"Self-loop found for town: {town}"
                )

            for neighbour, edges in neighbours.items():

                if neighbour not in self._adjacency:
                    raise ValueError(
                        f"Unknown neighbour "
                        f"{neighbour} stored for {town}."
                    )

                for edge in edges:
                    if edge.distance <= 0:
                        raise ValueError(...)

                if not edges:
                    raise ValueError(f"Empty edge list stored from " f"{town} to {neighbour}")

                if self._directed:
                    continue

                forward_distances = sorted(edge.distance for edge in edges)

                reverse_edges = self._adjacency[neighbour].get(town)

                if reverse_edges is None:
                    raise ValueError(...)

                reverse_distances = sorted(edge.distance for edge in reverse_edges
                )

                if forward_distances != reverse_distances:
                    raise ValueError(
                        f"Road distances disagree between "
                        f"{town} and {neighbour}."
                    )