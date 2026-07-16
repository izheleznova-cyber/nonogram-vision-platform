"""
player.py

Player board state.
"""

from __future__ import annotations

from dataclasses import dataclass


EMPTY = 0
FILLED = 1
CROSSED = 2


@dataclass(slots=True)
class PlayerBoard:
    """
    Current player board.
    """

    width: int
    height: int

    cells: list[list[int]]

    @classmethod
    def create(
        cls,
        width: int,
        height: int,
    ) -> "PlayerBoard":
        """
        Create an empty player board.
        """

        return cls(
            width=width,
            height=height,
            cells=[
                [EMPTY] * width
                for _ in range(height)
            ],
        )
    
    def fill(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Mark cell as filled.
        """

        self.cells[row][col] = FILLED


    def cross(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Mark cell with a cross.
        """

        self.cells[row][col] = CROSSED


    def clear(
        self,
        row: int,
        col: int,
    ) -> None:
        """
        Clear a cell.
        """

        self.cells[row][col] = EMPTY

    def state(
        self,
        row: int,
        col: int,
    ) -> int:
        """
        Return current cell state.
        """

        return self.cells[row][col]
