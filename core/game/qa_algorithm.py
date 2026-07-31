"""
qa_algorithm.py

Analogue of nonograms.ru Qa().

This module determines which hints
can be crossed out automatically.
"""

from __future__ import annotations

from core.puzzle.model import Puzzle
from core.puzzle.player import (
    PlayerBoard,
    EMPTY,
    FILLED,
    CROSSED,
)

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

def _apply_completed_hint(
    puzzle: Puzzle,
    board: PlayerBoard,
    completed: list[bool],
    row: int,
    hint: int,
) -> None:
    """
    Logical equivalent of JavaScript Qa().J().

    For now:
        - marks the clue as completed.

    Later:
        - crosses cells around completed clues;
        - auto-crosses empty cells when all clues are completed.
    """

    completed[hint] = True

def _auto_cross_completed_line(
    board: PlayerBoard,
    completed: list[bool],
    row: int,
) -> None:
    """
    If every clue in the row has been completed,
    automatically cross all remaining empty cells.
    """

    if not all(completed):
        return

    for col in range(board.width):

        if board.state(row, col) == EMPTY:
            board.cross(
                row,
                col,
            )


def _auto_cross_completed_line(
    board: PlayerBoard,
    completed: list[bool],
    row: int,
) -> None:
    """
    Equivalent of the final part of JavaScript J().

    If every clue in the row has been completed,
    automatically cross all remaining empty cells.
    """

    if not all(completed):
        return

    for col in range(board.width):

        if board.state(row, col) == EMPTY:
            board.cross(
                row,
                col,
            )

def _auto_cross_completed_column(
    board: PlayerBoard,
    completed: list[bool],
    col: int,
) -> None:
    """
    Cross every remaining EMPTY cell in a completed column.
    """

    if not all(completed):
        return

    for row in range(board.height):
        if board.state(row, col) == EMPTY:
            board.cross(row, col)


def _scan_row_left_to_right(
    puzzle: Puzzle,
    board: PlayerBoard,
    row: int,
) -> list[bool]:
    """
    PASS 1.
    Scan one row from left to right.
    """

    hints = puzzle.row_runs[row]
    completed = [False] * len(hints)

    hint = 0
    col = 0

    while col < puzzle.width:

        #
        # Начало текущей группы.
        #
        start = col
        value = board.state(row, col)
        error = False

        #
        # Пройти всю группу одинаковых клеток.
        #
        while (
            col < puzzle.width
            and board.state(row, col) == value
        ):

            player = board.state(row, col)
            solution = puzzle.matrix[row][col]

            #
            # Player filled a cell that should be empty.
            #
            if (
                player == FILLED
                and solution == 0
            ):
                error = True

            col += 1

        #
        # Если группа содержит ошибку,
        # прекращаем анализ строки.
        #
        if error:
            break

        length = col - start

        #
        # Пропускаем пустые группы.
        #
        if value != FILLED:
            continue

        #
        # Закончились подсказки.
        #
        if hint >= len(hints):
            break

        #
        # Длина текущей подсказки.
        #
        _, hint_length = hints[hint]

        #
        # Совпала длина группы.
        #
        if length == hint_length:

            #
            # Two neighbouring hints
            # have the same length.
            #
            if (
                hint < len(hints) - 1
                and hints[hint + 1][1] == hint_length
                and col < puzzle.width
                and board.state(row, col) != EMPTY
            ):
                break

            _apply_completed_hint(
                puzzle,
                board,
                completed,
                row,
                hint,
            )

            #
            # TODO:
            # Qa(): J(hint, row, True, True)
            # Automatic crossing will be implemented later.
            #
            hint += 1

        else:
            break

    _auto_cross_completed_line(
        board,
        completed,
        row,
    )

    return completed

def _scan_column_top_to_bottom(
    puzzle: Puzzle,
    board: PlayerBoard,
    col: int,
) -> list[bool]:
    """
    PASS 2.
    Scan one column from top to bottom.
    """

    hints = puzzle.column_runs[col]
    completed = [False] * len(hints)

    hint = 0
    row = 0

    while row < puzzle.height:

        #
        # Beginning of current group.
        #
        start = row
        value = board.state(row, col)
        error = False

        #
        # Walk through the whole group.
        #
        while (
            row < puzzle.height
            and board.state(row, col) == value
        ):

            player = board.state(row, col)
            solution = puzzle.matrix[row][col]

            #
            # Player filled a cell that should be empty.
            #
            if (
                player == FILLED
                and solution == 0
            ):
                error = True

            row += 1

        #
        # Stop analysing this column
        # if the group contains an error.
        #
        if error:
            break

        length = row - start

        #
        # Skip empty groups.
        #
        if value != FILLED:
            continue

        #
        # No more hints.
        #
        if hint >= len(hints):
            break

        #
        # Current hint length.
        #
        _, hint_length = hints[hint]

        #
        # Group length matches hint.
        #
        if length == hint_length:

            #
            # Two neighbouring hints
            # have the same length.
            #
            if (
                hint < len(hints) - 1
                and hints[hint + 1][1] == hint_length
                and row < puzzle.height
                and board.state(row, col) != EMPTY
            ):
                break

            _apply_completed_hint(
                puzzle,
                board,
                completed,
                col,
                hint,
            )

            hint += 1

        else:
            break

    _auto_cross_completed_column(
        board,
        completed,
        col,
    )

    return completed

    
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