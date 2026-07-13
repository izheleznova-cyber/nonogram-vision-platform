"""
checker.py

Puzzle checking utilities.
"""

from __future__ import annotations

from .model import Puzzle
from .player import PlayerBoard


def is_cell_correct(
    puzzle: Puzzle,
    board: PlayerBoard,
    row: int,
    col: int,
) -> bool:
    """
    Check a single cell.
    """

    solution = puzzle.matrix[row][col]

    player = board.cells[row][col]

    #
    # Empty cell
    #
    if solution == 0:
        return player != 1

    #
    # Filled cell
    #
    return player == 1


def is_solved(
    puzzle: Puzzle,
    board: PlayerBoard,
) -> bool:
    """
    Check whether the whole puzzle is solved.
    """

    for row in range(puzzle.height):

        for col in range(puzzle.width):

            if not is_cell_correct(
                puzzle,
                board,
                row,
                col,
            ):
                return False

    return True
