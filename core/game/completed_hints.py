"""
completed_hints.py
Automatic completion detection for row/column hints.
"""
from __future__ import annotations
from core.puzzle.model import Puzzle
from core.puzzle.player import (
    PlayerBoard,
    FILLED,
    CROSSED,
    EMPTY,
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
        board=board,
        line_type="row",
        line_index=row,
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
        board=board,
        line_type="column",
        line_index=col,
    )


def _run_is_bounded(
    board: PlayerBoard,
    line_type: str,
    line_index: int,
    start: int,
    length: int,
) -> bool:
    """
    Check if a run is bounded by crosses or field edges.
    
    For rows: check left (start-1) and right (start+length)
    For columns: check top (start-1) and bottom (start+length)
    """
    # Check left/top boundary
    if start > 0:
        if line_type == "row":
            left_state = board.state(line_index, start - 1)
        else:  # column
            left_state = board.state(start - 1, line_index)
        if left_state != CROSSED:
            return False
    
    # Check right/bottom boundary
    end = start + length
    if line_type == "row":
        if end < board.width:
            right_state = board.state(line_index, end)
            if right_state != CROSSED:
                return False
    else:  # column
        if end < board.height:
            right_state = board.state(end, line_index)
            if right_state != CROSSED:
                return False
    
    return True


def _match_runs(
    solution_runs,
    player_runs,
    matrix,
    board: PlayerBoard,
    line_type: str,
    line_index: int,
):
    """
    Compare player runs with solution runs.
    Now checks that runs are properly bounded.
    """
    result = []
    for solution in solution_runs:
        ok = False
        for player in player_runs:
            if player != solution:
                continue
            if _run_has_errors(matrix, player):
                continue
            # NEW: Check boundaries
            start, length = player
            if not _run_is_bounded(board, line_type, line_index, start, length):
                continue
            ok = True
            break
        result.append(ok)
    return result


def _run_has_errors(matrix, run):
    """
    Check whether the player run contains
    cells that are not part of solution.
    """
    start, length = run
    for i in range(start, start + length):
        if matrix[i] == 0:
            return True
    return False