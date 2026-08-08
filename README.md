# Sri Lanka Pathfinder

A pathfinding project that implements and compares BFS,
Dijkstra's algorithm, and A* using a Sri Lankan road network.

## Current stage

Automated testing of the graph and BFS implementation.

## Documentation

- `docs/road-network-design.md`: defines the initial graph model and sample
  road network.

## Project structure

- `models/graph.py`: core undirected weighted graph structure
- `data/sample_network.py`: creates the initial sample road network
- `docs/road-network-design.md`: documents the graph design
- `main.py`: current application entry point
- `tests/`: will contain automated tests
- `algorithms/`: will contain pathfinding algorithms

## Planned features

- Custom graph of Sri Lankan locations
- BFS pathfinding
- Dijkstra shortest-path search
- A* search using geographic coordinates
- Algorithm performance comparison
- Command-line interface
- Map visualisation
- Real road-network integration

## Implemented algorithms

### Breadth-First Search (BFS)

BFS searches the graph level by level and finds paths with the fewest number
of edges. It does not use road distances when choosing a path.

## Running the project

```bash
python main.py

## Testing

The project uses pytest for automated testing.

Run the full test suite with:

```bash
python -m pytest