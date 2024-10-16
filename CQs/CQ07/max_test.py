from CQs.CQ07.find_max import find_and_remove_max  # type: ignore


def test_find_and_remove_max() -> None:
    input: list[int] = [3, 0, 2, 3, 1]
    assert find_and_remove_max(input) == 3
    # normal test


def test_mutate_max() -> None:
    input: list[int] = [3, 0, 2, 3, 1]
    assert find_and_remove_max(input) != [3, 0, 2, 3, 1]
    # test to see if the list has changed from its original


def test_return_empty() -> None:
    input: list[int] = []
    assert find_and_remove_max(input) == -1
    # testing for empty list
