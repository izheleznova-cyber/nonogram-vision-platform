"""
inspect_completed_hints.py

Verify completed hints detection.
"""

from __future__ import annotations

from core.puzzle.model import Puzzle
from core.puzzle.hints import generate_hints
from core.puzzle.runs import (
    matrix_runs,
    column_runs,
)

from core.puzzle.player import PlayerBoard

from core.game.player_runs import player_row_runs
from core.game.completed_hints import completed_row_hints


def main():

    #
    # Puzzle
    #
    # ..###..##
    #

    matrix = [
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    ]

    row_hints, column_hints = generate_hints(matrix)

    puzzle = Puzzle(
        width=10,
        height=1,
        colors=1,
        matrix=matrix,
        row_hints=row_hints,
        column_hints=column_hints,
        row_runs=matrix_runs(matrix),
        column_runs=column_runs(matrix),
    )

    board = PlayerBoard.create(
        width=10,
        height=1,
    )

    #
    # Fill first group only
    #
    # ..###.....
    #

    board.fill(0, 2)
    board.fill(0, 3)
    board.fill(0, 4)

    print("=" * 60)
    print("PUZZLE")
    print("=" * 60)

    print("Hints        :", puzzle.row_hints[0])
    print("Solution runs:", puzzle.row_runs[0])

    print()

    print("=" * 60)
    print("PLAYER")
    print("=" * 60)

    print("Player runs  :", player_row_runs(board, 0))

    print()

    result = completed_row_hints(
        puzzle,
        board,
        0,
    )

    print("=" * 60)
    print("RESULT")
    print("=" * 60)

    print(result)

    assert result == [True, False]

    print()
    print("SUCCESS")


if __name__ == "__main__":
    main()