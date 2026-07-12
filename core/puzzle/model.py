"""
Internal puzzle model.

Every decoder should produce this object.

The rest of the project works only with Puzzle
and never depends on the original source format.
"""

from dataclasses import dataclass


@dataclass
class Puzzle:
    """
    Internal representation of a nonogram.
    """

    width: int
    height: int

    colors: int

    matrix: list[list[int]]
