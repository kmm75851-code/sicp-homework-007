class Countdown:
    """
    Считает от n до 0 включительно.

    >>> list(Countdown(3))
    [3, 2, 1, 0]
    """
    def __init__(self, n):
        pass

    def __iter__(self):
        """Возвращает сам себя — объект является итератором."""
        pass

    def __next__(self):
        """Возвращает следующее значение или бросает StopIteration."""
        pass


class NumberRange:
    """
    Своя реализация range с полным интерфейсом последовательности.

    >>> r = NumberRange(1, 10, 2)
    >>> list(r)
    [1, 3, 5, 7, 9]
    >>> len(r)
    5
    >>> r[2]
    5
    >>> 3 in r
    True
    >>> 4 in r
    False
    >>> repr(r)
    'NumberRange(1, 10, 2)'
    """
    def __init__(self, start, stop, step=1):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass

    def __contains__(self, value):
        pass

    def __repr__(self):
        pass


class Cycle:
    """
    Бесконечно циклится по последовательности.

    >>> from generators import take
    >>> take(7, Cycle([1, 2, 3]))
    [1, 2, 3, 1, 2, 3, 1]
    """
    def __init__(self, seq):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


class LazyMap:
    """
    Ленивый map без использования встроенного map().

    >>> lm = LazyMap(lambda x: x * x, [1, 2, 3, 4])
    >>> next(lm)
    1
    >>> next(lm)
    4
    >>> list(LazyMap(str, [1, 2, 3]))
    ['1', '2', '3']
    """
    def __init__(self, f, iterable):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


class InfiniteCounter:
    """
    Бесконечный счётчик с шагом.

    >>> from generators import take
    >>> take(5, InfiniteCounter(start=0, step=2))
    [0, 2, 4, 6, 8]
    >>> take(4, InfiniteCounter(start=10, step=-1))
    [10, 9, 8, 7]
    """
    def __init__(self, start=0, step=1):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
