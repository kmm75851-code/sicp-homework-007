from functools import reduce
from operator import add, mul


def squares(seq):
    """Квадраты всех элементов. Возвращает итератор.

    >>> list(squares((1, 2, 3, 4)))
    [1, 4, 9, 16]
    >>> list(squares(()))
    []

    Подсказка: map(lambda x: ..., seq)
    """
    pass


def only_positive(seq):
    """Только положительные числа (> 0). Возвращает итератор.

    >>> list(only_positive((-1, 2, -3, 4, 0)))
    [2, 4]
    >>> list(only_positive((-1, -2)))
    []

    Подсказка: filter(lambda x: ..., seq)
    """
    pass


def product(seq):
    """Произведение всех элементов через reduce.

    >>> product((1, 2, 3, 4, 5))
    120
    >>> product((2, 3))
    6

    Подсказка: reduce(mul, seq)
    """
    pass


def sum_of_evens(seq):
    """Сумма чётных элементов через filter + reduce.
    Если чётных нет — возвращает 0.

    >>> sum_of_evens((1, 2, 3, 4, 5, 6))
    12
    >>> sum_of_evens((1, 3, 5))
    0

    Подсказка: reduce(add, filter(..., seq), 0)
    Третий аргумент reduce — начальное значение (initial).
    Без него reduce упадёт на пустой последовательности.
    """
    pass


def words_longer_than(words, n):
    """Слова строго длиннее n символов. Возвращает итератор.

    >>> list(words_longer_than(['hi', 'hello', 'world', 'ok'], 3))
    ['hello', 'world']
    >>> list(words_longer_than(['a', 'bb'], 5))
    []

    Подсказка: filter(lambda w: len(w) > n, words)
    """
    pass


def upper_words(words):
    """Все слова в верхнем регистре. Возвращает итератор.

    >>> list(upper_words(['hello', 'world']))
    ['HELLO', 'WORLD']

    Подсказка: map(lambda w: w.upper(), words)
    """
    pass


def max_by_length(words):
    """Самое длинное слово через reduce. Возвращает строку.

    >>> max_by_length(['hi', 'python', 'ok', 'hello'])
    'python'
    >>> max_by_length(['one'])
    'one'

    Подсказка: reduce(lambda a, b: a if len(a) >= len(b) else b, words)
    """
    pass


def pipeline(seq):
    """Сумма квадратов нечётных чисел.
    Только через map + filter + reduce. Без list comprehension и циклов.

    >>> pipeline((1, 2, 3, 4, 5))
    35
    >>> pipeline((2, 4, 6))
    0
    >>> pipeline((1, 3))
    10

    Подсказка: reduce(add, map(..., filter(..., seq)), 0)
    Порядок: сначала filter (отбираем нечётные), потом map (квадраты), потом reduce (сумма).
    """
    pass
