from data.sample_network import build_sample_graph


def main() -> None:
    graph = build_sample_graph()

    print("Sri Lanka Pathfinder")
    print(graph)

    print("\nTowns:")
    for town in graph.get_towns():
        print(f"- {town}")

    print("\nColombo neighbours:")
    for neighbour, distance in graph.get_neighbours("Colombo").items():
        print(f"- {neighbour}: {distance} km")

    
if __name__ == "__main__":
    main()