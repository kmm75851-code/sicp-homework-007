import pytest
from strings import (
    count_vowels, reverse_words, is_palindrome, capitalize_words,
    longest_word, word_frequency, caesar_cipher, run_length_decode
)


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0


def test_reverse_words():
    assert reverse_words("hello world foo") == "foo world hello"
    assert reverse_words("one") == "one"
    assert reverse_words("a b c") == "c b a"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("Racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("a") is True
    assert is_palindrome("") is True


def test_capitalize_words():
    assert capitalize_words("hello world python") == "Hello World Python"
    assert capitalize_words("one") == "One"
    assert capitalize_words("a b c") == "A B C"


def test_longest_word():
    assert longest_word("hi hello world ok") == "hello"
    assert longest_word("python is great") == "python"
    assert longest_word("a bb ccc") == "ccc"


def test_word_frequency():
    assert word_frequency("the cat sat on the mat") == {
        "the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1
    }
    assert word_frequency("a a a") == {"a": 3}
    assert word_frequency("The the THE") == {"the": 3}


def test_caesar_cipher():
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"
    assert caesar_cipher("Khoor, Zruog!", -3) == "Hello, World!"
    assert caesar_cipher("xyz", 3) == "abc"
    assert caesar_cipher("XYZ", 3) == "ABC"
    assert caesar_cipher("abc", 0) == "abc"


def test_run_length_decode():
    assert run_length_decode("3a2b1c") == "aaabbc"
    assert run_length_decode("1h2e3l1o") == "heello"
    assert run_length_decode("5x") == "xxxxx"
