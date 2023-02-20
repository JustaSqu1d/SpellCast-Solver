from typing import List

from solver.enums import LetterValues

__all__ = [
    'DOUBLE_LETTER_CHARACTER',
    'DOUBLE_WORD_CHARACTER',
    'is_word_valid',
    'initialize_dictionary',
    'is_prefix_valid',
    'get_word_value',
    'get_letter_value',
]

DOUBLE_LETTER_CHARACTER = "*"
DOUBLE_WORD_CHARACTER = "^"


def is_word_valid(words: List[str], word: str) -> bool:
    """Checks if the word is valid"""
    return word in words and len(word) > 1


def initialize_dictionary() -> List[str]:
    """Returns a list of all the words in the dictionary"""
    with open('/Users/kmang/PycharmProjects/pythonProject1/solver/words.txt') as file:
        return [word.strip() for word in file.readlines()]


def is_prefix_valid(words: List[str], word: str) -> bool:
    """Checks if any word starts with this prefix using binary search"""
    word = word.upper()
    if not words:
        return False
    if len(words) == 1:
        return words[0].startswith(word)
    mid = len(words) // 2
    if words[mid].startswith(word):
        return True
    elif words[mid] < word:
        return is_prefix_valid(words[mid:], word)
    else:
        return is_prefix_valid(words[:mid], word)


def get_word_value(word) -> int:
    """Returns the value of the word."""
    value = 0
    is_double_word = False
    is_long = len(word) > 5
    for CHAR in word:
        if CHAR == DOUBLE_LETTER_CHARACTER:
            value += get_letter_value(word[word.index(CHAR) + 1]) * 2
        elif CHAR == DOUBLE_WORD_CHARACTER:
            is_double_word = True
        else:
            value += get_letter_value(CHAR)
    return value * 2 if is_double_word else value + 10 if is_long else 0


def get_letter_value(letter: str) -> int:
    """Returns the value of the letter."""
    return LetterValues[letter].value
