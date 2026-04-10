class Countdown:
    """
    Считает от n до 0 включительно.

    >>> list(Countdown(3))
    [3, 2, 1, 0]
    """
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        """Возвращает сам себя — объект является итератором."""
        return self 

    def __next__(self):
        """Возвращает следующее значение или бросает StopIteration."""
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

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
            self.start = start
            self.stop = stop
            self.step = step

    def __iter__(self):
            current = self.start
            while current < self.stop:
                yield current
                current += self.step

    def __len__(self):
        return max(0, (self.stop - self.start + self.step - 1) // self.step)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Negative index not supported")

        value = self.start + index * self.step

        if value >= self.stop:
            raise IndexError("Index out of range")
        
        return value

    def __contains__(self, value):
        if value < self.start or value >= self.stop:
            return False

        return (value - self.start) % self.step == 0

    def __repr__(self):
        return f"NumberRange({self.start}, {self.stop}, {self.step})"

class Cycle:
    """
    Бесконечно циклится по последовательности.

    >>> from generators import take
    >>> take(7, Cycle([1, 2, 3]))
    [1, 2, 3, 1, 2, 3, 1]
    """
    def __init__(self, seq):
        self.seq = seq
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.seq:
            raise StopIteration  

        value = self.seq[self.index]
        self.index = (self.index + 1) % len(self.seq)
        return value


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
        self.f = f
        self.iterator = iter(iterable) 

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterator)  
        return self.f(value)        
    
class InfiniteCounter:
    """
    Бесконечный счётчик с шагом.

    >>> from generators import take
    >>> take(5, InfiniteCounter(start=0, step=2))
    [0, 2, 4, 6, 8]
    >>> take(4,InfiniteCounter(start=10, step=-1))
    [10, 9, 8, 7]
    """
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        return value