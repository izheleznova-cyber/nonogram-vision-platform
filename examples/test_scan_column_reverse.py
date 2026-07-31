"""
Diagnostic test for qa_algorithm.

Prints every stage of column analysis.
"""

from __future__ import annotations

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.game.player_runs import (
    player_column_runs,
)

from core.game.qa_algorithm import (
    _scan_column_bottom_to_top,
)

from core.puzzle.player import (
    PlayerBoard,
    EMPTY,
    FILLED,
    CROSSED,
)

PAGE_ID = 1039


def fill_run(board, col, start, length):

    for row in range(start, start + length):
        board.fill(row, col)


def print_column(puzzle, board, col):

    print()
    print("=" * 70)
    print(f"COLUMN {col}")
    print("=" * 70)
    print()

    print("Solution matrix:")

    print(
        "".join(
            "#"
            if puzzle.matrix[row][col]
            else "."
            for row in range(puzzle.height)
        )
    )

    print()
    print("Solution runs:")
    print(puzzle.column_runs[col])

    print()
    print("Player runs:")
    print(player_column_runs(board, col))

    completed = _scan_column_bottom_to_top(
        puzzle,
        board,
        col,
    )

    symbols = {
        EMPTY: ".",
        FILLED: "#",
        CROSSED: "x",
    }

    print()
    print("Board after scan:")

    print(
        "".join(
            symbols[board.state(row, col)]
            for row in range(board.height)
        )
    )

    print()
    print("Completed:")
    print(completed)


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    board = PlayerBoard.create(
        puzzle.width,
        puzzle.height,
    )

    #
    # Choose test column.
    #
    col = 13

    #
    # Initial state.
    #
    print_column(
        puzzle,
        board,
        col,
    )

    #
    # Fill first solution run.
    #
    start, length = puzzle.column_runs[col][0]

    fill_run(
        board,
        col,
        start,
        length,
    )

    print_column(
        puzzle,
        board,
        col,
    )

    #
    # Fill second solution run.
    #
    if len(puzzle.column_runs[col]) > 1:

        start, length = puzzle.column_runs[col][1]

        fill_run(
            board,
            col,
            start,
            length,
        )

        print_column(
            puzzle,
            board,
            col,
        )

    #
    # Fill third solution run.
    #
    if len(puzzle.column_runs[col]) > 2:

        start, length = puzzle.column_runs[col][2]

        fill_run(
            board,
            col,
            start,
            length,
        )

        print_column(
            puzzle,
            board,
            col,
        )

    #
    # Temporary experiment.
    #
    for row in range(0, 30):
        board.fill(row, col)

    print_column(
        puzzle,
        board,
        col,
    )

    #
    # Two neighbouring groups without a gap.
    #
    for row in range(13, 19):
        board.fill(row, col)

    print_column(
        puzzle,
        board,
        col,
    )

    #
    # Reset board.
    #
    board = PlayerBoard.create(
        puzzle.width,
        puzzle.height,
    )

    for row in range(13, 19):
        board.fill(row, col)

    print_column(
        puzzle,
        board,
        col,
    )

    #
    # Fill every solution run.
    #

    board = PlayerBoard.create(
        puzzle.width,
        puzzle.height,
    )

    for start, length in puzzle.column_runs[col]:
        fill_run(
            board,
            col,
            start,
            length,
        )

    print_column(
        puzzle,
        board,
        col,
    )

if __name__ == "__main__":
    main()
