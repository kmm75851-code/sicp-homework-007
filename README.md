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

## Ограничения

- `sequences.py` — только `map`, `filter`, `reduce`. Никаких `for`/`while`.
- `iterables.py` — `LazyMap` не может использовать встроенный `map()`. Проверяется автоматически.

## Ключевая идея

`for x in obj` под капотом:
1. Python вызывает `obj.__iter__()` → получает итератор
2. Вызывает `iterator.__next__()` снова и снова
3. Когда `StopIteration` — цикл завершается

Генераторы с `yield` реализуют этот протокол автоматически.
Классы с `__iter__`/`__next__` делают то же самое вручную.
