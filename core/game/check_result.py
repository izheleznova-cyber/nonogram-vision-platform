"""
check_result.py

Puzzle checking result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CheckResult:
    """
    Result of puzzle validation.
    """

    solved: bool

    error_count: int

    incorrect_cells: list[tuple[int, int]]
