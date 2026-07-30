"""
completed_hints.py

Determine which hints are already completed.
"""

from __future__ import annotations

from core.puzzle.model import Puzzle
from core.puzzle.player import PlayerBoard

from .player_runs import (
    player_row_runs,
    player_column_runs,
)


def has_run(
    run: tuple[int, int],
    player_runs: list[tuple[int, int]],
) -> bool:
    """
    Return True if the exact run exists in player runs.
    """

    return run in player_runs



def completed_row_hints(
    puzzle: Puzzle,
    board: PlayerBoard,
    row: int,
) -> list[bool]:
    """
    Return completion state for every row hint.

    Example:

        solution:
            [(7,15),(30,2),(39,7)]

        player:
            [(7,15),(39,7)]

        result:
            [True, False, True]
    """

    solution = puzzle.row_runs[row]
    player = player_row_runs(board, row)

    return [
        has_run(run, player)
        for run in solution
    ]


def completed_column_hints(
    puzzle: Puzzle,
    board: PlayerBoard,
    col: int,
) -> list[bool]:
    """
    Return completion state for every column hint.
    """

    solution = puzzle.column_runs[col]
    player = player_column_runs(board, col)

    return [
        run_completed(run, player)
        for run in solution
    ]
