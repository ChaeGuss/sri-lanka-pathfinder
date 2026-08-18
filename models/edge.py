from dataclasses import dataclass

@dataclass(frozen=True)
class Edge:
    """Represent one directed road segment"""

    distance: float
    way_id: str | None = None
    name: str | None = None
    highway_type: str | None = None
