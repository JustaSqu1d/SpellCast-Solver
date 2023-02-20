from typing import List

from solver import Board, Tile
from solver.board import Word
from solver.utils import initialize_dictionary, is_prefix_valid, is_word_valid, DOUBLE_WORD_CHARACTER, \
    DOUBLE_LETTER_CHARACTER
import threading

def solver(grid: Board) -> None:
    dictionary = initialize_dictionary()

    def solver_helper(x: int, y: int, word: Word, results: List[Word]) -> None:

        # print(word.word, x, y)

        current_tile = grid.get_tile(x, y)

        if current_tile is None:
            return

        if current_tile.used:
            return

        new_tiles = word.tiles.copy()
        new_tiles.append(current_tile)

        new_word = Word(new_tiles)

        if not is_prefix_valid(dictionary, new_word.word):
            return

        current_tile.used = True

        if is_word_valid(dictionary, new_word.word):
            results.append(new_word)

        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                if not (x_offset == 0 and y_offset == 0):
                    solver_helper(x + x_offset, y + y_offset, new_word, results)

        current_tile.used = False

    words = []
    for x in range(5):
        for y in range(5):
            solver_helper(x, y, Word([]), words)

    words = sorted(words, key=lambda word: word.get_value(), reverse=True)

    limit = 0

    for word in words:
        if limit == 5:
            break
        print(word)
        limit += 1


if __name__ == '__main__':

    line1 = "A* V I U E".split()
    line2 = "Q E U E N".split()
    line3 = "P I N A T".split()
    line4 = "I A I B Z".split()
    line5 = "C O V H M^".split()

    row_1 = []
    for x, char in enumerate(line1):
        row_1.append(Tile(char, x, 0, DOUBLE_LETTER_CHARACTER in char, DOUBLE_WORD_CHARACTER in char))

    row_2 = []
    for x, char in enumerate(line2):
        row_2.append(Tile(char, x, 1, DOUBLE_LETTER_CHARACTER in char, DOUBLE_WORD_CHARACTER in char))

    row_3 = []
    for x, char in enumerate(line3):
        row_3.append(Tile(char, x, 2, DOUBLE_LETTER_CHARACTER in char, DOUBLE_WORD_CHARACTER in char))

    row_4 = []
    for x, char in enumerate(line4):
        row_4.append(Tile(char, x, 3, DOUBLE_LETTER_CHARACTER in char, DOUBLE_WORD_CHARACTER in char))

    row_5 = []
    for x, char in enumerate(line5):
        row_5.append(Tile(char, x, 4, DOUBLE_LETTER_CHARACTER in char, DOUBLE_WORD_CHARACTER in char))

    print(row_1, row_2, row_3, row_4, row_5, sep="\n")

    board = Board([row_1, row_2, row_3, row_4, row_5])

    solver(board)
