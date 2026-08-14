import pytest

from data.network_loader import load_network
from models.graph import Graph


@pytest.fixture
def sample_graph() -> Graph:
    """Return the sample road graph for tests."""
    return load_network(
        "data/sample_network.json"
    )