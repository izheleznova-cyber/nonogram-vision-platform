"""
Generate nonogram hints from a puzzle matrix.

The implementation follows the algorithm used by
nonograms.ru but is written in clear Python.
"""

from __future__ import annotations

from typing import List


Hint = List[List[int]]
"""
One row (or column) of hints.

Example (black/white):

[[5,1],[2,1]]

Example (color):

[[4,2],[3,5],[1,2]]
"""


def generate_row_hints(
    matrix: list[list[int]],
) -> list[Hint]:
    """
    Generate hints for all rows.
    """

    hints: list[Hint] = []

    for row in matrix:

        row_hint: Hint = []

        current_color = 0
        run_length = 0

        for cell in row:

            if cell == current_color:

                if cell != 0:
                    run_length += 1

            else:

                if current_color != 0:
                    row_hint.append(
                        [run_length, current_color]
                    )

                current_color = cell

                if cell == 0:
                    run_length = 0
                else:
                    run_length = 1

        if current_color != 0:
            row_hint.append(
                [run_length, current_color]
            )

        hints.append(row_hint)

    return hints


def generate_column_hints(
    matrix: list[list[int]],
) -> list[Hint]:
    """
    Generate hints for all columns.
    """

    height = len(matrix)
    width = len(matrix[0])

    hints: list[Hint] = []

    for col in range(width):

        column_hint: Hint = []

        current_color = 0
        run_length = 0

        for row in range(height):

            cell = matrix[row][col]

            if cell == current_color:

                if cell != 0:
                    run_length += 1

            else:

                if current_color != 0:
                    column_hint.append(
                        [run_length, current_color]
                    )

                current_color = cell

                if cell == 0:
                    run_length = 0
                else:
                    run_length = 1

        if current_color != 0:
            column_hint.append(
                [run_length, current_color]
            )

        hints.append(column_hint)
    return hints

def generate_hints(
    matrix: list[list[int]],
) -> tuple[list[Hint], list[Hint]]:
    """
    Generate both row and column hints.
    """

    rows = generate_row_hints(matrix)

    columns = generate_column_hints(matrix)

    return rows, columns    



    
