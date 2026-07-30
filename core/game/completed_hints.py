"""
completed_hints.py

Automatic completion detection for row/column hints.
"""

from __future__ import annotations

from core.puzzle.model import Puzzle
from core.puzzle.player import (
    PlayerBoard,
    FILLED,
)

from .player_runs import (
    player_row_runs,
    player_column_runs,
)


def completed_row_hints(
    puzzle: Puzzle,
    board: PlayerBoard,
    row: int,
) -> list[bool]:
    """
    Determine which row hints are completed.
    """

    player = player_row_runs(board, row)
    solution = puzzle.row_runs[row]

    return _match_runs(
        solution_runs=solution,
        player_runs=player,
        matrix=puzzle.matrix[row],
    )


def completed_column_hints(
    puzzle: Puzzle,
    board: PlayerBoard,
    col: int,
) -> list[bool]:
    """
    Determine which column hints are completed.
    """

    player = player_column_runs(board, col)
    solution = puzzle.column_runs[col]

    matrix = [
        puzzle.matrix[row][col]
        for row in range(puzzle.height)
    ]

    return _match_runs(
        solution_runs=solution,
        player_runs=player,
        matrix=matrix,
    )


def _match_runs(
    solution_runs,
    player_runs,
    matrix,
):
    """
    Compare player runs with solution runs.

    This function is a simplified analogue
    of nonograms.ru Qa().
    """

    result = []

    for solution in solution_runs:

        ok = False

        for player in player_runs:

            if player != solution:
                continue

            if _run_has_errors(
                matrix,
                player,
            ):
                continue

            ok = True
            break

        result.append(ok)

    return result


def _run_has_errors(
    matrix,
    run,
):
    """
    Check whether the player run contains
    cells that are not part of solution.
    """

    start, length = run

    for i in range(start, start + length):

        if matrix[i] == 0:
            return True

    return False