import pytest
from operator import add
from generators import (
    naturals, take, fibonacci, running_sum,
    sieve, drop_while, take_while, zip_with,
    window, interleave_gen, flatten_gen
)


def test_naturals():
    gen = naturals()
    assert [next(gen) for _ in range(5)] == [1, 2, 3, 4, 5]


def test_take():
    assert take(5, naturals()) == [1, 2, 3, 4, 5]
    assert take(0, naturals()) == []
    assert take(3, iter([10, 20, 30, 40])) == [10, 20, 30]


def test_fibonacci():
    assert take(8, fibonacci()) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert take(1, fibonacci()) == [0]


def test_running_sum():
    assert list(running_sum([1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(running_sum([5])) == [5]
    assert list(running_sum([])) == []


def test_sieve():
    assert sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert sieve(10) == [2, 3, 5, 7]
    assert sieve(1) == []


def test_drop_while():
    assert list(drop_while(lambda x: x < 5, [1, 3, 5, 7, 2])) == [5, 7, 2]
    assert list(drop_while(lambda x: x > 0, [1, 2, 3])) == []
    assert list(drop_while(lambda x: x < 0, [1, 2, 3])) == [1, 2, 3]


def test_take_while():
    assert list(take_while(lambda x: x < 5, [1, 3, 5, 7, 2])) == [1, 3]
    assert list(take_while(lambda x: x > 0, [1, 2, 3])) == [1, 2, 3]
    assert list(take_while(lambda x: x < 0, [1, 2, 3])) == []


def test_zip_with():
    assert list(zip_with(add, [1, 2, 3], [10, 20, 30])) == [11, 22, 33]
    assert list(zip_with(lambda a, b: a * b, [2, 3], [4, 5])) == [8, 15]
    assert list(zip_with(add, [], [])) == []


def test_window():
    assert list(window([1, 2, 3, 4, 5], 3)) == [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    assert list(window([1, 2, 3], 1)) == [(1,), (2,), (3,)]
    assert list(window([1, 2], 3)) == []


def test_interleave_gen():
    assert list(interleave_gen([1, 2, 3], ['a', 'b', 'c'])) == [1, 'a', 2, 'b', 3, 'c']
    assert list(interleave_gen([1, 2], ['a', 'b', 'c'])) == [1, 'a', 2, 'b']
    assert list(interleave_gen([], [1, 2])) == []


def test_flatten_gen():
    assert list(flatten_gen([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]
    assert list(flatten_gen([1, 2, 3])) == [1, 2, 3]
    assert list(flatten_gen([[1, 2], [3, [4, [5]]]])) == [1, 2, 3, 4, 5]
    assert list(flatten_gen(['hello', ['world']])) == ['hello', 'world']
