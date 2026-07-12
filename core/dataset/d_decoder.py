"""
d_decoder.py

Reconstruct puzzle matrix from array d.

Implementation follows the algorithm found
in nonogram.min.062.js.
"""

from __future__ import annotations

from .d_header import DHeader, read_header

from core.puzzle.hints import generate_hints
from core.puzzle.model import Puzzle


def fill_matrix(
    matrix: list[list[int]],
    data: list[list[int]],
    header: DHeader,
) -> None:
    """
    Restore matrix E from encoded blocks.

    This function is a direct Python translation
    of the corresponding JavaScript code.
    """

    offset = header.block_offset

    start = header.first_block_record
    finish = start + header.blocks

    for record in data[start:finish]:

        # Starting column
        col_start = record[0] - offset[0] - 1

        # Block width
        width = record[1] - offset[1]

        # Cell color
        color = record[2] - offset[2]

        # Row number
        row = record[3] - offset[3] - 1

        if not (0 <= row < header.rows):
            raise ValueError(f"Invalid row index: {row}")

        if not (0 <= col_start < header.columns):
            raise ValueError(f"Invalid start column: {col_start}")

        if col_start + width > header.columns:
            raise ValueError(f"Block exceeds row width: start={col_start}, width={width}"
            )
        
        if color < 0 or color > header.colors:
            raise ValueError(f"Invalid color index: {color}"
            )


        # Paint horizontal run
        for col in range(col_start, col_start + width):

            matrix[row][col] = color


def decode(
    data: list[list[int]],
) -> Puzzle:
    """
    Decode puzzle from array d.
    """

    header = read_header(data)

    matrix = [
        [0] * header.columns
        for _ in range(header.rows)
    ]

    fill_matrix(
        matrix,
        data,
        header,
    )

    # Генерация подсказок
    row_hints, column_hints = generate_hints(matrix)

    return Puzzle(
        width=header.columns,
        height=header.rows,
        colors=header.colors,
        matrix=matrix,
        row_hints=row_hints,
        column_hints=column_hints,
    )
