"""
layout.py

Layout calculations for rendering a nonogram.

The module computes image geometry only.
It performs no drawing.
"""

from __future__ import annotations

from dataclasses import dataclass

from .model import Puzzle


CELL_SIZE = 20
MARGIN = 10


@dataclass(slots=True)
class Layout:
    """
    Geometry of rendered puzzle.
    """

    cell_size: int

    left_hint_cells: int
    top_hint_cells: int

    puzzle_width: int
    puzzle_height: int

    image_width: int
    image_height: int

    puzzle_x: int
    puzzle_y: int


def calculate_layout(
    puzzle: Puzzle,
    cell_size: int = CELL_SIZE,
    margin: int = MARGIN,
) -> Layout:
    """
    Calculate layout for rendering.
    """

    if puzzle.row_hints is None:
        raise ValueError("row_hints are missing")

    if puzzle.column_hints is None:
        raise ValueError("column_hints are missing")

    left_hint_cells = max(
        len(hints)
        for hints in puzzle.row_hints
    )

    top_hint_cells = max(
        len(hints)
        for hints in puzzle.column_hints
    )

    puzzle_width = puzzle.width * cell_size

    puzzle_height = puzzle.height * cell_size

    puzzle_x = margin + left_hint_cells * cell_size

    puzzle_y = margin + top_hint_cells * cell_size

    image_width = (
        puzzle_x
        + puzzle_width
        + margin
    )

    image_height = (
        puzzle_y
        + puzzle_height
        + margin
    )

    return Layout(
        cell_size=cell_size,

        left_hint_cells=left_hint_cells,
        top_hint_cells=top_hint_cells,

        puzzle_width=puzzle_width,
        puzzle_height=puzzle_height,

        image_width=image_width,
        image_height=image_height,

        puzzle_x=puzzle_x,
        puzzle_y=puzzle_y,
    )
