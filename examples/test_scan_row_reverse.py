"""
Diagnostic test for qa_algorithm.

Prints every stage of line analysis.
"""

from __future__ import annotations

from pathlib import Path

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR
from core.game.qa_algorithm import _scan_row_right_to_left

from core.puzzle.player import (
    PlayerBoard,
    EMPTY,
    FILLED,
    CROSSED,
)

from core.game.player_runs import (
    player_row_runs,
)

from core.game.qa_algorithm import (
    analyse,
    analyse_row,
    _scan_row_left_to_right,
)

PAGE_ID = 1039

def fill_run(board, row, start, length):

    for col in range(start, start + length):
        board.fill(row, col)
        

def print_row(puzzle, board, row):

    print()
    print("=" * 70)
    print(f"ROW {row}")
    print("=" * 70)

    print()

    print("Solution matrix:")

    print(
        "".join(
            "#" if x else "."
            for x in puzzle.matrix[row]
        )
    )

    print()

    print("Solution runs:")

    print(
        puzzle.row_runs[row]
    )

    print()

    print("Player runs:")

    print(
        player_row_runs(board, row)
    )

    print()

    completed = _scan_row_right_to_left(
        puzzle,
        board,
        row,
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
            for col in range(board.width)
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

    row = 8

    #
    # Initial state
    #

    print_row(
        puzzle,
        board,
        row,
    )

    #
    # Fill first solution run
    #

    start, length = puzzle.row_runs[row][0]

    board.fill(row, start)
    board.fill(row, start + 1)
    board.fill(row, start + 2)

    print_row(
        puzzle,
        board,
        row,
    )

    #
    # Fill second solution run
    #

    if len(puzzle.row_runs[row]) > 1:

        start, length = puzzle.row_runs[row][1]

        fill_run(
            board,
            row,
            start,
            length,
        )

        print_row(
            puzzle,
            board,
            row,
        )

     #
    # Fill third solution run
    #

    if len(puzzle.row_runs[row]) > 2:

        start, length = puzzle.row_runs[row][2]

        fill_run(
            board,
            row,
            start,
            length,
        )

        print_row(
            puzzle,
            board,
            row,
        )   
    #
    # Temporary experiment
    #

    for col in range(0, 30):
        board.fill(row, col)

    print_row(
        puzzle,
        board,
        row,
    )

    #
    # Two neighbouring groups without a gap.
    #
    for col in range(13, 19):
        board.fill(row, col)

    print_row(
        puzzle,
        board,
        row,
    )
        
    #
    # Two neighbouring groups without a gap.
    #

    board = PlayerBoard.create(
        puzzle.width,
        puzzle.height,
    )

    for col in range(13, 19):
        board.fill(row, col)

    print_row(
        puzzle,
        board,
        row,
    )


if __name__ == "__main__":
    main()
