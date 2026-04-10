def count_vowels(s):
    """Количество гласных (a, e, i, o, u) в строке. Регистр не важен."""
    total = 0
    for i in s.lower():
        if i in ("aeiou"):
            total += 1
    return total


def reverse_words(s):
    """Слова в обратном порядке.
    reverse_words("hello world foo") -> "foo world hello"
    """
    return " ".join(s.split()[::-1])


def is_palindrome(s):
    """Проверяет, является ли строка палиндромом. Регистр не важен."""
    return s.lower().replace(" ","") == s.lower().replace(" ","")[::-1]


def capitalize_words(s):
    """Первая буква каждого слова заглавная.
    Без использования .title() или .capitalize().
    capitalize_words("hello world") -> "Hello World"
    """
    words = s.split()
    result = []

    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
    return " ".join(result)
    

def longest_word(s):
    """Самое длинное слово в строке. Если несколько — первое."""
    words = s.split()
    return max(words, key=len) if words else ""
    


def word_frequency(s):
    """Словарь {слово: сколько раз встречается}.
    Регистр не важен, знаки препинания игнорировать.
    """
    result = {}

    for word in s.lower().split():
        word = word.strip(".,!?;:()\"'")
        if word:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    return result
    


def caesar_cipher(s, n):
    """Шифр Цезаря: сдвигает каждую букву на n позиций.
    Только латинские буквы, регистр сохраняется.
    Остальные символы не меняются.
    caesar_cipher("Hello, World!", 3) -> "Khoor, Zruog!"
    """
    #c = "z"

    #pos = ord(c) - ord('a')   # 25
    #pos = (pos + n) % 26      # 1
    #new = chr(pos + ord('a')) # "b"
    
def caesar_cipher(s, n):
    result = []

    for char in s:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            pos = ord(char) - base
            new_pos = (pos + n) % 26
            result.append(chr(base + new_pos))
        else:
            result.append(char)

    return "".join(result)

def run_length_decode(s): 
    """Декодирует строку вида "3a2b1c" -> "aaabbc".   
    Число перед буквой — сколько раз её повторить. """
    result = []
    num = ""

    for char in s:
        if char.isdigit():
            num += char
        else:
            result.append(char * int(num))
            num = ""

    return "".join(result)