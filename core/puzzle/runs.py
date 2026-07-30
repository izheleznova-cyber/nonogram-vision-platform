"""
Utilities for extracting filled runs from puzzles.
"""

from __future__ import annotations


def matrix_runs(
    matrix: list[list[int]],
) -> list[list[tuple[int, int]]]:
    """
    Build runs for every row.

    Each run is

        (start, length)
    """

    result = []

    for row in matrix:

        runs = []

        start = None
        length = 0

        for col, cell in enumerate(row):

            if cell != 0:

                if start is None:
                    start = col

                length += 1

            else:

                if start is not None:

                    runs.append(
                        (start, length)
                    )

                    start = None
                    length = 0

        if start is not None:

            runs.append(
                (start, length)
            )

        result.append(runs)

    return result


def column_runs(
    matrix: list[list[int]],
) -> list[list[tuple[int, int]]]:
    """
    Build runs for every column.

    Each run is

        (start, length)
    """

    if not matrix:
        return []

    height = len(matrix)
    width = len(matrix[0])

    result = []

    for col in range(width):

        runs = []

        start = None
        length = 0

        for row in range(height):

            cell = matrix[row][col]

            if cell != 0:

                if start is None:
                    start = row

                length += 1

            else:

                if start is not None:

                    runs.append(
                        (start, length)
                    )

                    start = None
                    length = 0

        if start is not None:

            runs.append(
                (start, length)
            )

        result.append(runs)

    return result