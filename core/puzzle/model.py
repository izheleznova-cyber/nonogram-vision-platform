from dataclasses import dataclass


@dataclass
class Puzzle:
    """
    Internal puzzle model.
    """

    width: int
    height: int

    colors: int

    matrix: list[list[int]]

    row_hints: list | None = None
    column_hints: list | None = None
