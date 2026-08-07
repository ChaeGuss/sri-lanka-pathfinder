# Sri Lanka Pathfinder

A pathfinding project that implements and compares BFS,
Dijkstra's algorithm, and A* using a Sri Lankan road network.

## Current stage

Implementing the core undirected weighted graph data structure.

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

## Running the project

```bash
python main.py