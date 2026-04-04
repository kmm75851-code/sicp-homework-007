import inspect
import sequences as seq_module
import pytest
from sequences import (
    squares, only_positive, product, sum_of_evens,
    words_longer_than, upper_words, max_by_length, pipeline
)


def test_squares():
    assert list(squares((1, 2, 3, 4))) == [1, 4, 9, 16]
    assert list(squares((0, 5))) == [0, 25]
    assert list(squares(())) == []


def test_only_positive():
    assert list(only_positive((-1, 2, -3, 4, 0))) == [2, 4]
    assert list(only_positive((1, 2, 3))) == [1, 2, 3]
    assert list(only_positive((-1, -2))) == []


def test_product():
    assert product((1, 2, 3, 4, 5)) == 120
    assert product((1,)) == 1
    assert product((2, 3)) == 6


def test_sum_of_evens():
    assert sum_of_evens((1, 2, 3, 4, 5, 6)) == 12
    assert sum_of_evens((1, 3, 5)) == 0
    assert sum_of_evens((2, 4)) == 6
    assert sum_of_evens(()) == 0


def test_words_longer_than():
    assert list(words_longer_than(["hi", "hello", "world", "ok"], 3)) == ["hello", "world"]
    assert list(words_longer_than(["a", "bb", "ccc"], 5)) == []


def test_upper_words():
    assert list(upper_words(["hello", "world"])) == ["HELLO", "WORLD"]
    assert list(upper_words(["python"])) == ["PYTHON"]


def test_max_by_length():
    assert max_by_length(["hi", "python", "ok", "hello"]) == "python"
    assert max_by_length(["a", "bb", "ccc"]) == "ccc"
    assert max_by_length(["one"]) == "one"


def test_pipeline():
    assert pipeline((1, 2, 3, 4, 5)) == 35
    assert pipeline((2, 4, 6)) == 0
    assert pipeline((1, 3)) == 10
    assert pipeline(()) == 0


def test_no_loops():
    fns = ['squares', 'only_positive', 'product', 'sum_of_evens',
           'words_longer_than', 'upper_words', 'max_by_length', 'pipeline']
    for name in fns:
        src = inspect.getsource(getattr(seq_module, name))
        for keyword in ['for ', 'while ']:
            assert keyword not in src, (
                f"{name}: запрещено использовать '{keyword.strip()}' — только map/filter/reduce"
            )
