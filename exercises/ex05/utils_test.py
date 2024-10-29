from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens() -> None:
    test: list[int] = [2, 3, 4]
    assert only_evens(test) == [2, 4]


def test_only_evens_edge() -> None:
    test: list[int] = [-2, -1, 0, 2, 3, 4]
    assert only_evens(test) == [-2, 0, 2, 4]


def test_only_evens_odd() -> None:
    test: list[int] = [1, 3, 5]
    assert only_evens(test) == []


def test_sub() -> None:
    test: list[int] = [2, 3, 4]
    assert sub(test, 0, 1) == [2]


def test_sub_wide_range() -> None:
    test: list[int] = [2, 3, 4]
    assert sub(test, -3, 10) == [2, 3, 4]


def test_sub_out_range() -> None:
    test: list[int] = [2, 3, 4]
    assert sub(test, 4, 10) == []


def test_add_at_index() -> None:
    test: list[int] = [1, 3, 4]
    add_at_index(test, 2, 1)
    assert test == [1, 2, 3, 4]


def test_add_at_index_empty() -> None:
    test: list[int] = []
    add_at_index(test, 5, 0)
    assert test == [5]


def test_add_at_index_raises_indexerror() -> None:
    test: list[int] = [2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(test, 6, 8)
