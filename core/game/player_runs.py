"""
player_runs.py

Extract runs from current player board.
"""

from __future__ import annotations

from core.puzzle.player import (
    PlayerBoard,
    FILLED,
)


def player_row_runs(
    board: PlayerBoard,
    row: int,
) -> list[tuple[int, int]]:
    """
    Return player runs for one row.

    Each run is represented as:

        (start_column, length)
    """

    runs: list[tuple[int, int]] = []

    start: int | None = None
    length = 0

    for col in range(board.width):

        if board.state(row, col) == FILLED:

            if start is None:
                start = col

            length += 1

        else:

            if start is not None:
                runs.append((start, length))
                start = None
                length = 0

    if start is not None:
        runs.append((start, length))

    return runs

def player_column_runs(
    board: PlayerBoard,
    col: int,
) -> list[tuple[int, int]]:
    """
    Return player runs for one column.

    Each run is represented as:

        (start_row, length)
    """

    runs: list[tuple[int, int]] = []

    start: int | None = None
    length = 0

    for row in range(board.height):

        if board.state(row, col) == FILLED:

            if start is None:
                start = row

            length += 1

        else:

            if start is not None:
                runs.append((start, length))
                start = None
                length = 0

    if start is not None:
        runs.append((start, length))

    return runs    