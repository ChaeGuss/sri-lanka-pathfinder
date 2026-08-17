from cli.app import run_cli


def main() -> None:
    """Run the Sri Lanka Pathfinder CLI."""
    try:
        run_cli() 
    except KeyboardInterrupt: print ("\nApplication cancelled.") #Incase user press Ctrl+C


if __name__ == "__main__":
    main()