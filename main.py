
from data.network_loader import load_network
from pathlib import Path


def main() -> None:
    """Run the Sri Lanka pathfinding application."""
    PROJECT_ROOT = Path(__file__).resolve().parent

    NETWORK_FILE = (PROJECT_ROOT / "data" / "sample_network.json")
    graph = load_network(NETWORK_FILE)

    print(graph)
    print(graph.get_towns())
    print(graph.get_neighbours("Colombo"))


if __name__ == "__main__":
    main()