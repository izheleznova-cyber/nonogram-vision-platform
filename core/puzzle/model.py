from dataclasses import dataclass


@dataclass
class Puzzle:

    width: int
    height: int

    colors: int

    matrix: list[list[int]]

    row_hints: list | None = None
    column_hints: list | None = None

    row_runs: list | None = None
    column_runs: list | None = None
