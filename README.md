# Homework 007 — Sequences, Generators & Iterables

SICP Course | Урок 008

## Файлы

| Файл | Тема | Функций/Классов |
|------|------|-----------------|
| `sequences.py` | map / filter / reduce (без циклов) | 8 |
| `generators.py` | Ленивые генераторы с `yield` | 11 |
| `iterables.py` | Дандер-методы: `__iter__`, `__next__`, `__len__`, `__getitem__`, `__contains__` | 5 классов |

## Запуск тестов

```bash
pytest tests/ -v
```

## Ограничения — проверяются автоматически

- `sequences.py` — только `map`, `filter`, `reduce`. `for`/`while` запрещены.
- `iterables.py` — `LazyMap` не может использовать встроенный `map()`.

---

## Часть 1: sequences.py

> Никаких `for`/`while` — только `map`, `filter`, `reduce`.

- **`squares(seq)`** → квадраты всех элементов. `map(lambda x: x*x, seq)`
- **`only_positive(seq)`** → только числа > 0. `filter(lambda x: x > 0, seq)`
- **`product(seq)`** → произведение через `reduce(mul, seq)`
- **`sum_of_evens(seq)`** → сумма чётных. Осторожно: `reduce` падает на пустой последовательности — используй третий аргумент `initial=0`
- **`words_longer_than(words, n)`** → слова строго длиннее n символов
- **`upper_words(words)`** → все слова в верхнем регистре
- **`max_by_length(words)`** → самое длинное слово через `reduce`
- **`pipeline(seq)`** → сумма квадратов нечётных: сначала `filter`, потом `map`, потом `reduce`

---

## Часть 2: generators.py

> Все функции — генераторы с `yield`. Бесконечные не хранят всё в памяти.

- **`naturals()`** → бесконечно: 1, 2, 3, ...
- **`take(n, gen)`** → первые n элементов из генератора → список
- **`fibonacci()`** → бесконечно: 0, 1, 1, 2, 3, 5, 8, ...
- **`running_sum(seq)`** → накопленные суммы: [1,2,3] → 1, 3, 6
- **`sieve(n)`** → простые числа до n
- **`drop_while(pred, gen)`** → пропускает пока pred истинен, потом отдаёт всё
- **`take_while(pred, gen)`** → берёт пока pred истинен, потом стоп
- **`zip_with(f, a, b)`** → применяет f к парам лениво
- **`window(seq, n)`** → скользящее окно: `(1,2,3), (2,3,4), ...`
- **`interleave_gen(a, b)`** → чередует два итератора: a0, b0, a1, b1, ...
- **`flatten_gen(nested)`** → рекурсивно разворачивает вложенные списки. Строки не разворачивать!

---

## Часть 3: iterables.py

> Ключевая идея: `for x in obj` вызывает `obj.__iter__()`, потом `__next__()` снова и снова, пока не `StopIteration`.

### Countdown
Считает от n до 0. Реализует `__iter__` (возвращает `self`) и `__next__` (возвращает текущее значение и уменьшает счётчик).
```python
list(Countdown(3))  # → [3, 2, 1, 0]
```
💡 Храни `self.current = n`. Когда `current < 0` — `raise StopIteration`.

### NumberRange
Своя реализация `range` с полным интерфейсом.
```python
r = NumberRange(1, 10, 2)
list(r)    # → [1, 3, 5, 7, 9]
len(r)     # → 5
r[2]       # → 5
3 in r     # → True
4 in r     # → False
```
💡 `__len__`: `max(0, (stop - start + step - 1) // step)`
💡 `__contains__`: без перебора — `start <= value < stop and (value - start) % step == 0`

### Cycle
Бесконечно циклится по последовательности.
```python
take(7, Cycle([1, 2, 3]))  # → [1, 2, 3, 1, 2, 3, 1]
```
💡 Храни индекс, увеличивай на 1, берёт `seq[index % len(seq)]`.

### LazyMap
Ленивый map **без встроенного** `map()`. Запрещено — проверяется тестом.
```python
lm = LazyMap(lambda x: x*x, [1, 2, 3])
next(lm)  # → 1
next(lm)  # → 4
```
💡 В `__init__` вызови `iter(iterable)` и сохрани. В `__next__` — `next(self._iter)` и примени функцию.

### InfiniteCounter
Бесконечный счётчик с шагом (может быть отрицательным).
```python
take(5, InfiniteCounter(0, 2))   # → [0, 2, 4, 6, 8]
take(4, InfiniteCounter(10, -1)) # → [10, 9, 8, 7]
```

---

## Ключевая идея

```
for x in obj:
    ...
```
Это эквивалентно:
```python
it = obj.__iter__()
while True:
    try:
        x = it.__next__()
    except StopIteration:
        break
```
Генераторы с `yield` реализуют этот протокол автоматически.
Классы с `__iter__`/`__next__` — вручную.
