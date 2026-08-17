from cli.app import _choose_town
from cli.app import _choose_algorithm
from cli.app import _ask_to_continue

def test_choose_town_from_number(
    monkeypatch,
) -> None:
    towns = [
        "Colombo",
        "Kandy",
    ]

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2",
    )

    selected = _choose_town(
        towns,
        "Choose: ",
    )

    assert selected == "Kandy"

def test_choose_dijkstra(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2",
    )

    algorithm = _choose_algorithm()

    assert algorithm == "Dijkstra"

def test_choose_town_retries_invalid_input(
    monkeypatch,
) -> None:
    towns = [
        "Colombo",
        "Kandy",
    ]

    answers = iter(
        [
            "hello",
            "99",
            "1",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers),
    )

    selected = _choose_town(
        towns,
        "Choose: ",
    )

    assert selected == "Colombo"

def test_continue_accepts_yes(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "yes",
    )

    assert _ask_to_continue()

def test_continue_accepts_no(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "n",
    )

    assert not _ask_to_continue()