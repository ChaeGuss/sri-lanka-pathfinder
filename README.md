# Sri Lanka Pathfinder

A pathfinding project that implements and compares BFS,
Dijkstra's algorithm, and A* using a Sri Lankan road network.

## Current stage

Implementing A* search and comparing BFS, Dijkstra, and A* behaviour.

## Documentation

- `docs/road-network-design.md`: defines the initial graph model and sample
  road network.

The Graph model now supports both undirected and directed graphs.

The human-friendly sample town network remains undirected.

OSM-style converted road networks are directed so that one-way roads can
be represented.

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

## Geographic coordinates

Sample towns can now store latitude and longitude coordinates.

Coordinates are currently approximate learning data rather than precise
road-junction locations.

Geographic distance is calculated using a spherical Haversine calculation.

The geographic distance will later be used as the heuristic estimate for
A* search.

## Implemented algorithms

### Breadth-First Search (BFS)

BFS searches the graph level by level and finds paths with the fewest number
of edges. It does not use road distances when choosing a path.

### Dijkstra's Algorithm

Dijkstra's algorithm finds a path with the minimum total edge weight.

In this project, edge weights currently represent simplified road distances
in kilometres.

Unlike BFS, Dijkstra considers road weights when selecting routes.

The implementation uses Python's `heapq` module as a priority queue.

### A* Search

A* uses both the known road cost from the start and a heuristic estimate of
the remaining distance to the destination.

The implementation uses:

- `g(n)` for the known road distance from the start
- `h(n)` for approximate geographic distance to the goal
- `f(n) = g(n) + h(n)` for priority

The heuristic is calculated using latitude and longitude coordinates.

Each pathfinding algorithm returns a SearchResult containing:

- the discovered path, or None if unreachable
- the number of explored nodes

models/
    data structures

algorithms/
    pathfinding logic

services/
    coordinates algorithm execution

utils/
    shared presentation/geographic helpers

data/
    sample network JSON - contains towns
                                      name
                                      latitude
                                      longitude

                                  roads
                                      from
                                      to
                                      distance
    network loader - deserializes JSON file and constructs the Graph

    raw_osm_sample.json - To teach how external road data is transformed into the application's graph model

tests/
    automated correctness checks


OpenStreetMap-style data
           │
           ▼
      OSM converter
           │
           ▼
          Graph
           │
    ┌──────┼──────┐
    ▼      ▼      ▼
   BFS  Dijkstra   A*



## Running the project

```bash
python main.py

1. Select a start town.
2. Select a destination.
3. Choose BFS, Dijkstra, A*, or comparison mode.
4. Review route, distance, edge count, and explored nodes.
5. Choose whether to run another search.

## Testing

The project uses pytest for automated testing.

Run the full test suite with:

```bash
python -m pytest