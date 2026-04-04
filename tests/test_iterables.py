import pytest
from generators import take
from iterables import Countdown, NumberRange, Cycle, LazyMap, InfiniteCounter


class TestCountdown:
    def test_basic(self):
        assert list(Countdown(3)) == [3, 2, 1, 0]

    def test_zero(self):
        assert list(Countdown(0)) == [0]

    def test_is_iterator(self):
        c = Countdown(2)
        assert iter(c) is c

    def test_stop_iteration(self):
        c = Countdown(0)
        next(c)
        with pytest.raises(StopIteration):
            next(c)

    def test_for_loop(self):
        result = []
        for x in Countdown(3):
            result.append(x)
        assert result == [3, 2, 1, 0]


class TestNumberRange:
    def test_list(self):
        assert list(NumberRange(1, 10, 2)) == [1, 3, 5, 7, 9]

    def test_default_step(self):
        assert list(NumberRange(0, 5)) == [0, 1, 2, 3, 4]

    def test_len(self):
        assert len(NumberRange(1, 10, 2)) == 5
        assert len(NumberRange(0, 0)) == 0

    def test_getitem(self):
        r = NumberRange(1, 10, 2)
        assert r[0] == 1
        assert r[2] == 5
        assert r[4] == 9

    def test_contains_true(self):
        r = NumberRange(1, 10, 2)
        assert 1 in r
        assert 3 in r
        assert 9 in r

    def test_contains_false(self):
        r = NumberRange(1, 10, 2)
        assert 2 not in r
        assert 4 not in r
        assert 10 not in r

    def test_repr(self):
        assert repr(NumberRange(1, 10, 2)) == 'NumberRange(1, 10, 2)'


class TestCycle:
    def test_basic(self):
        assert take(7, Cycle([1, 2, 3])) == [1, 2, 3, 1, 2, 3, 1]

    def test_single(self):
        assert take(4, Cycle([42])) == [42, 42, 42, 42]

    def test_is_iterator(self):
        c = Cycle([1, 2])
        assert iter(c) is c


class TestLazyMap:
    def test_squares(self):
        lm = LazyMap(lambda x: x * x, [1, 2, 3, 4])
        assert next(lm) == 1
        assert next(lm) == 4
        assert next(lm) == 9

    def test_list(self):
        assert list(LazyMap(str, [1, 2, 3])) == ['1', '2', '3']

    def test_stop_iteration(self):
        lm = LazyMap(lambda x: x, [1])
        next(lm)
        with pytest.raises(StopIteration):
            next(lm)

    def test_is_iterator(self):
        lm = LazyMap(lambda x: x, [1, 2])
        assert iter(lm) is lm

    def test_no_builtin_map(self):
        import inspect
        import iterables
        src = inspect.getsource(iterables.LazyMap)
        assert 'map(' not in src, 'LazyMap не должен использовать встроенный map()'


class TestInfiniteCounter:
    def test_even(self):
        assert take(5, InfiniteCounter(start=0, step=2)) == [0, 2, 4, 6, 8]

    def test_countdown(self):
        assert take(4, InfiniteCounter(start=10, step=-1)) == [10, 9, 8, 7]

    def test_default(self):
        assert take(3, InfiniteCounter()) == [0, 1, 2]

    def test_is_iterator(self):
        c = InfiniteCounter()
        assert iter(c) is c
