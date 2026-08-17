from pathlib import Path

from algorithms.astar import astar
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from data.network_loader import load_network
from utils.display import print_search_result
from models.graph import Graph
from services.pathfinder import compare_algorithms

PROJECT_ROOT = Path(__file__).resolve().parent.parent

NETWORK_FILE = (PROJECT_ROOT / "data" / "sample_network.json")

def run_cli() -> None:
    """Run the interactive command-line application"""
    graph = load_network(NETWORK_FILE)

    print("Sri Lanka Pathfinder")

    while True:

        towns = sorted(graph.get_towns())    #Alphabetical order

        _print_towns(towns)

        start = _choose_town(towns, "\nChoose start town number: ",)

        goal = _choose_town(towns, "Choose destination town number: ",)

        _print_algorithm_menu()

        algorithm = _choose_algorithm()

        if algorithm == "ALL":
            _compare_all(graph, start, goal,)
        else:
            _run_algorithm(algorithm, graph, start, goal,)

        if not _ask_to_continue():
            break

    print("\nGoodbye.")

def _print_towns(towns: list[str]) -> None:
    """Print available towns with numbered options"""
    print("\n Available towns: ")

    for index, town in enumerate(towns, start=1, ):
        print(f"{index}. {town}")

def _choose_town(towns: list[str], prompt: str,) -> str:
    """Ask the user to select a town by number."""
    while True:
        choice = input(prompt).strip()

        if not choice.isdigit():
            print(
                "Please enter a valid town number."
            )
            continue

        index = int(choice) - 1

        if not 0 <= index < len(towns):
            print(
                "Town number is out of range."
            )
            continue

        return towns[index]

def _print_algorithm_menu() -> None:
    """Print available pathfinding options."""
    print("\nChoose algorithm:")
    print("1. BFS")
    print("2. Dijkstra")
    print("3. A*")
    print("4. Compare all")

def _choose_algorithm() -> str:
    """Ask the user to choose a pathfinding algorithm."""
    valid_choices = {
        "1": "BFS",
        "2": "Dijkstra",
        "3": "A*",
        "4": "ALL",
    }

    while True:
        choice = input(
            "Selection: "
        ).strip()

        if choice in valid_choices:
            return valid_choices[choice]

        print(
            "Please choose 1, 2, 3, or 4."
        )

def _run_algorithm(algorithm: str, graph: Graph, start: str, goal: str,) -> None:

    algorithms = {
        "BFS": bfs,
        "Dijkstra": dijkstra,
        "A*": astar,
    }

    search_function = algorithms.get(
        algorithm
    )

    if search_function is None:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    result = search_function(graph, start, goal,)

    print_search_result(algorithm, graph, result, )

def _compare_all(graph: Graph, start: str, goal: str,) -> None:
    """Run and print all pathfinding algorithms."""
    results = compare_algorithms(graph, start, goal,)

    for algorithm_name, result in results.items():
        print_search_result(
            algorithm_name,
            graph,
            result,
        )

def _ask_to_continue() -> bool:
    """Ask whether the user wants to run another search."""
    while True:
        choice = input("\nSearch again? (y/n): ").strip().lower()

        if choice in {"y", "yes"}:
            return True

        if choice in {"n", "no"}:
            return False

        print("Please enter y or n.")