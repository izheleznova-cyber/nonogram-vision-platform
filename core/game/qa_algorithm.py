"""
qa_algorithm.py

Analogue of nonograms.ru Qa().

This module determines which hints
can be crossed out automatically.
"""

from __future__ import annotations

from core.puzzle.model import Puzzle
from core.puzzle.player import PlayerBoard

from .player_runs import (
    player_row_runs,
    player_column_runs,
)


def analyse_row(
    puzzle: Puzzle,
    board: PlayerBoard,
    row: int,
) -> list[bool]:
    """
    Analyse one puzzle row.

    Returns completion state
    for every row hint.
    """

    return _analyse_line(
        solution_runs=puzzle.row_runs[row],
        player_runs=player_row_runs(board, row),
        solution_line=puzzle.matrix[row],
    )


def analyse_column(
    puzzle: Puzzle,
    board: PlayerBoard,
    col: int,
) -> list[bool]:
    """
    Analyse one puzzle column.
    """

    solution = [
        puzzle.matrix[row][col]
        for row in range(puzzle.height)
    ]

    return _analyse_line(
        solution_runs=puzzle.column_runs[col],
        player_runs=player_column_runs(board, col),
        solution_line=solution,
    )


def _analyse_line(
    solution_runs: list[tuple[int, int]],
    player_runs: list[tuple[int, int]],
    solution_line: list[int],
) -> list[bool]:
    """
    Simplified analogue of Qa().

    Current stage:

        1. Compare runs.
        2. Verify solution.
    """

    result: list[bool] = []

    for run in solution_runs:

        result.append(
            _match_run(
                run,
                player_runs,
                solution_line,
            )
        )

    return result


def _match_run(
    run: tuple[int, int],
    player_runs: list[tuple[int, int]],
    solution_line: list[int],
) -> bool:
    """
    Check one hint.
    """

    if run not in player_runs:
        return False

    start, length = run

    #
    # Stage 1:
    # verify that every cell
    # belongs to the solution.
    #

    for i in range(start, start + length):

        if solution_line[i] == 0:
            return False

    return True


def analyse_row_debug(
    puzzle: Puzzle,
    board: PlayerBoard,
    row: int,
) -> None:
    """
    Print detailed diagnostics for one puzzle row.
    """

    solution_runs = puzzle.row_runs[row]
    player_runs = player_row_runs(board, row)
    solution_line = puzzle.matrix[row]

    print()
    print("=" * 70)
    print(f"ROW {row}")
    print("=" * 70)

    print()

    print("Solution line:")

    print(
        "".join(
            "#" if cell else "."
            for cell in solution_line
        )
    )

    print()

    print("Solution runs:")

    print(solution_runs)

    print()

    print("Player runs:")

    print(player_runs)

    print()

    print("-" * 70)

    for index, run in enumerate(solution_runs):

        print()

        print(f"Hint {index}")

        print(f"Expected : {run}")

        found = run in player_runs

        print(f"Found    : {found}")

        if found:

            start, length = run

            ok = True

            for col in range(start, start + length):

                if solution_line[col] == 0:
                    ok = False
                    break

            print(f"Solution : {ok}")

            print(f"Result   : {'COMPLETED' if ok else 'FAILED'}")

        else:

            print("Solution : skipped")

            print("Result   : NOT COMPLETED")

    print()

    print("Completed list:")

    print(
        analyse_row(
            puzzle,
            board,
            row,
        )
    )

    print()