# Road Network Design

## Purpose

This document defines the first sample road network used by the Sri Lanka
Pathfinder project.

The locations are real Sri Lankan towns, but the connections and distances
are simplified learning data and must not be treated as real navigation
information.

## Nodes

| ID | Town        |
| -- | ----------- |
|  1 | Colombo     |
|  2 | Kaduwela    |
|  3 | Malabe      |
|  4 | Kottawa     |
|  5 | Homagama    |
|  6 | Avissawella |
|  7 | Ratnapura   |
|  8 | Kegalle     |
|  9 | Kandy       |
| 10 | Gampaha     |

## Edges

| From       To           | Distance |
| ----------------------- | -------: |
| Colombo — Kaduwela      |    16 km |
| Colombo — Kottawa       |    21 km |
| Colombo — Gampaha       |    28 km |
| Kaduwela — Malabe       |     8 km |
| Kaduwela — Avissawella  |    35 km |
| Malabe — Kottawa        |    12 km |
| Kottawa — Homagama      |     7 km |
| Homagama — Avissawella  |    32 km |
| Avissawella — Ratnapura |    44 km |
| Avissawella — Kegalle   |    40 km |
| Gampaha — Kegalle       |    55 km |
| Kegalle — Kandy         |    42 km |
| Ratnapura — Kandy       |    90 km |



                           Gampaha
                          /       \
                        28         55
                        /           \
                   Colombo          Kegalle ---- 42 ---- Kandy
                  /       \          /                     /
                16         21       40                    90
                /           \      /                     /
          Kaduwela -- 8 -- Malabe                      Ratnapura
              \             /                            /
               35          12                           44
                \         /                            /
                Avissawella ---------------------------
                    \
                     32
                      \
                    Homagama
                       |
                       7
                       |
                    Kottawa

The edge table is the authoritative definition of the graph. The diagram is
only a visual aid.                   

## Design questions

1. What does a node represent? = A node represents one town.
2. What does an edge represent? = An edge represents a direct road connection between two towns.
3. What does a weight represent? = A weight represents the simplified distance of a road in kilometres.
4. Why is the graph weighted? = Because different roads have different distances.
5. What would BFS minimise? = The number of edges used.
6. What would Dijkstra minimise? = The sum of the edge weights.
