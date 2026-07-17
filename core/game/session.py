"""
session.py

Game session.

Coordinates player actions, predictions and puzzle checking.
"""

from __future__ import annotations

import time

from dataclasses import dataclass, field

from core.puzzle.model import Puzzle
from core.puzzle.player import (
    PlayerBoard,
    EMPTY,
    FILLED,
    CROSSED,
)

from .settings import LessonSettings
from .action import Action
from .prediction import Prediction
from .check_result import CheckResult


@dataclass(slots=True)
class GameSession:
    """
    One puzzle solving session.
    """

    puzzle: Puzzle

    settings: LessonSettings

    board: PlayerBoard = field(init=False)

    actions: list[Action] = field(default_factory=list)

    predictions: list[Prediction] = field(default_factory=list)

    started_at: float = field(default_factory=time.time)

    #
    # Check statistics
    #

    check_count: int = 0

    last_check_time: float = 0.0

    def __post_init__(self) -> None:

        self.board = PlayerBoard.create(
            self.puzzle.width,
            self.puzzle.height,
        )

    check_count: int = 0

    last_check_time: float = 0.0

    def __post_init__(self) -> None:

        self.board = PlayerBoard.create(
            self.puzzle.width,
            self.puzzle.height,
        )

    # ---------------------------------------------------------
    # Player actions
    # ---------------------------------------------------------

    def fill(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Fill one cell.
        """

        self.board.fill(row, col)

        self.actions.append(
            Action(
                timestamp=time.time(),
                action="fill",
                row=row,
                column=col,
            )
        )

    def cross(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Put a cross into one cell.
        """

        self.board.cross(row, col)

        self.actions.append(
            Action(
                timestamp=time.time(),
                action="cross",
                row=row,
                column=col,
            )
        )

    def clear(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Clear one cell.
        """

        self.board.clear(row, col)

        self.actions.append(
            Action(
                timestamp=time.time(),
                action="clear",
                row=row,
                column=col,
            )
        )


    # ---------------------------------------------------------
    # Mouse actions
    # ---------------------------------------------------------
    def left_click(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Handle left mouse click.
        """

        state = self.board.state(
            row,
            col,
        )

        if state == EMPTY:

            self.fill(
                row,
                col,
            )

        elif state == FILLED:

            self.clear(
                row,
                col,
            )

    def right_click(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Handle right mouse click.
        """

        state = self.board.state(
            row,
            col,
        )

        if state == EMPTY:

            self.cross(
                row,
                col,
            )

        elif state == CROSSED:

            self.clear(
                row,
                col,
            )

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def filled_cells(self) -> int:
        """
        Number of filled cells.
        """

        total = 0

        for row in self.board.cells:

            for cell in row:

                if cell == 1:
                    total += 1

        return total

    def solution_cells(self) -> int:
        """
        Number of filled cells in the solution.
        """

        total = 0

        for row in self.puzzle.matrix:

            for cell in row:

                if cell != 0:
                    total += 1

        return total

    def progress(self) -> float:
        """
        Solving progress (0..1).
        """

        solution = self.solution_cells()

        if solution == 0:
            return 0.0

        return self.filled_cells() / solution

    # ---------------------------------------------------------
    # Predictions
    # ---------------------------------------------------------

    def add_prediction(
        self,
        text: str,
    ) -> None:
        """
        Save current prediction.
        """

        self.predictions.append(
            Prediction(
                timestamp=time.time(),
                progress=self.progress(),
                text=text,
            )
        )

    # ---------------------------------------------------------
    # Session info
    # ---------------------------------------------------------

    def elapsed_time(self) -> float:
        """
        Seconds from session start.
        """

        return time.time() - self.started_at


    def check(
        self,
    ) -> CheckResult:
        """
        Compare current player board
        with the correct puzzle solution.
        """

        errors = []

        #
        # Check limit
        #

        if self.check_count >= self.settings.max_checks:

            return CheckResult(
                solved=False,
                error_count=0,
                incorrect_cells=[],
            )

        for row in range(self.puzzle.height):

            for col in range(self.puzzle.width):

                #
                # Expected puzzle state
                #

                expected_color = self.puzzle.matrix[row][col]

                expected_filled = (
                    expected_color != 0
                )

                #
                # Player state
                #

                player_filled = (
                    self.board.state(row, col)
                    == FILLED
                )

                #
                # Training Check
                # Only extra filled cells are errors.
                #

                if (
                    player_filled
                    and
                    not expected_filled
                ):

                    errors.append(
                        (row, col)
                    )

        self.last_check_time = time.time()
        self.check_count += 1

        self.auto_complete()

        return CheckResult(
            solved=(len(errors) == 0),
            error_count=len(errors),
            incorrect_cells=errors,
        )

    def complete_solved_lines(self) -> bool:
        """
        Automatically cross empty cells
        in solved rows.
        """
        changed = False 

        for row in range(self.puzzle.height):

            expected_count = 0
            player_count = 0

            solved = True

            for col in range(self.puzzle.width):

                expected = (
                    self.puzzle.matrix[row][col] != 0
                )

                player = (
                    self.board.state(row, col)
                    == FILLED
                )

                if expected:
                    expected_count += 1

                if player:
                    player_count += 1

                #
                # Игрок закрасил лишнюю клетку
                #

                if player and not expected:
                    solved = False
                    break

            #
            # Все нужные клетки уже закрашены
            #

            if not solved:
                continue

            if player_count != expected_count:
                continue

            #
            # Остальные клетки становятся крестиками
            #

            for col in range(self.puzzle.width):

                if self.board.state(row, col) == EMPTY:

                    self.board.cross(
                        row,
                        col,
                    )

                    changed = True

        return changed

    def complete_solved_columns(
        self,
    ) -> bool:
        """
        Automatically cross empty cells
        in solved columns.
        """
        changed = False  
        
        for col in range(self.puzzle.width):

            expected_count = 0
            player_count = 0

            solved = True

            for row in range(self.puzzle.height):

                expected = (
                    self.puzzle.matrix[row][col] != 0
                )

                player = (
                    self.board.state(row, col)
                    == FILLED
                )

                #
                # Count filled cells
                #

                if expected:
                    expected_count += 1

                if player:
                    player_count += 1

                #
                # Extra filled cell
                #

                if player and not expected:
                    solved = False
                    break

            #
            # Column is not solved yet
            #

            if not solved:
                continue

            if player_count != expected_count:
                continue

            #
            # Cross remaining empty cells
            #

            for row in range(self.puzzle.height):

                if (
                    self.board.state(row, col)
                    == EMPTY
                ):

                    self.board.cross(
                        row,
                        col,
                    )
                    changed = True

        return changed

    def auto_complete(
        self,
    ) -> None:
        """
        Repeat automatic completion
        until nothing changes.
        """

        while True:

            changed = False

            changed |= self.complete_solved_lines()

            changed |= self.complete_solved_columns()

            if not changed:
                break