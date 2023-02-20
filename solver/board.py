from typing import List, Optional

from solver.utils import get_letter_value, DOUBLE_LETTER_CHARACTER, DOUBLE_WORD_CHARACTER

__all__ = [
    'Tile',
    'Board',
    'Word',
]


class Tile:
    def __init__(self, letter, x: int, y: int, double_letter: Optional[bool] = False,
                 double_word: Optional[bool] = False, used: Optional[bool] = False):
        self.letter = letter.replace("*", "").replace("^", "")
        self.x = x
        self.y = y
        self.double_letter = double_letter
        self.double_word = double_word
        self.used = used

    def get_value(self) -> int:
        """:int: Returns the value of the tile"""
        return get_letter_value(self.letter) * (2 if self.double_letter else 1)

    def __str__(self):
        return self.letter + \
            (DOUBLE_LETTER_CHARACTER if self.double_letter else "") + \
            (DOUBLE_WORD_CHARACTER if self.double_word else "") + \
            f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, tiles: List[List[Tile]]):
        """Creates a new board with the given tiles

        Parameters:
            tiles (List[List[Tile]]): The tiles to use for the board.
                Warning
                    This board must be a square.
        """
        self.tiles = tiles
        self.size = len(tiles)

    def get_tile(self, x, y) -> Tile:
        """:Tile: Returns the tile at the given coordinates"""
        return self.tiles[x][y] if 0 <= x < self.size and 0 <= y < self.size else None

    def update_tile(self, x, y, tile: Tile):
        self.tiles[x][y] = tile


class Word:
    def __init__(self, tiles: List[Tile]):
        self.tiles = tiles
        self.word = "".join([tile.letter for tile in tiles])

    def get_value(self) -> int:
        """:int: Returns the value of the word"""
        points = 0
        doubled = False
        is_long = len(self.tiles) > 5

        for tile in self.tiles:
            points += tile.get_value()
            if tile.double_word:
                doubled = True

        return points * (2 if doubled else 1) + (10 if is_long else 0)

    def __str__(self):
        return self.word + f"({self.get_value()})" + "".join([f"({tile.x}, {tile.y})" for tile in self.tiles])

    def __repr__(self):
        return self.__str__()
