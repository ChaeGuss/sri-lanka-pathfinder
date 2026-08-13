from models.search_result import SearchResults


def test_search_result_stores_path_and_explored_count() -> None:
    result = SearchResults(
        path=["A", "B"],
        explored_nodes=4,
    )

    assert result.path == ["A", "B"]
    assert result.explored_nodes == 4