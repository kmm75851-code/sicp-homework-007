def naturals():
    """Бесконечный генератор натуральных чисел: 1, 2, 3, ..."""
    n = 1 
    while True:
        yield n
        n += 1 



def take(n, gen):
    """Берёт первые n элементов из генератора. Возвращает список."""
    lst = []
    for i in range(n):
        lst.append(next(gen))
    return lst 


def fibonacci():
    """Бесконечный генератор чисел Фибоначчи: 0, 1, 1, 2, 3, 5, 8, ..."""
    a, f = 0, 1
    while True:
        yield a
        a, f = f, a + f


def running_sum(seq):
    """Генератор накопленных сумм.
    running_sum([1, 2, 3, 4]) -> yields 1, 3, 6, 10
    """
    total = 0
    for i in seq:
        total += i
        yield total 

def sieve(n):
    """Решето Эратосфена — все простые числа до n включительно."""
    if n < 2:
        return iter(())

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return (i for i in range(2, n + 1) if sieve[i])

def drop_while(pred, gen):
    """Пропускает элементы пока pred истинен, потом отдаёт остальные."""

    it = iter(gen)

    for x in it:
        if not pred(x):
            yield x
            break

    for x in it:
        yield x


def take_while(pred, gen):
    """Берёт элементы пока pred истинен, потом останавливается."""
    for i in gen:
        if pred(i):
            yield i
        else:
            break

def zip_with(f, a, b):
    """Применяет f к парам элементов двух последовательностей лениво."""
    for i,y in zip(a, b):
        yield f(i, y)

def window(seq, n):
    """Скользящее окно размером n — генератор кортежей.
    window([1,2,3,4,5], 3) -> (1,2,3), (2,3,4), (3,4,5)
    """
    for i in range(len(seq) - n + 1):
            yield tuple(seq[i: i + n])



def interleave_gen(a, b):
    """Чередует элементы двух итераторов лениво.
    Останавливается когда один из итераторов исчерпан.
    interleave_gen([1,2,3], ['a','b','c']) -> 1, 'a', 2, 'b', 3, 'c'
    """
    for i, y in zip(a, b):
        yield i 
        yield y

def flatten_gen(nested):
    """Рекурсивно разворачивает вложенные
    итерируемые в плоский поток. Строки не разворачивать.
    flatten_gen([1, [2, [3, 4]], 5]) -> 1, 2, 3, 4, 5 """
    for item in nested:
        if isinstance(item,(list,tuple)):
            for sub in flatten_gen(item):
                yield sub
        else:
            yield item