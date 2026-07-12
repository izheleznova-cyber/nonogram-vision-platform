"""
d_header.py

Reading header information from array d.

The implementation follows the algorithm found
in nonogram.min.062.js.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DHeader:
    """
    Header of array d.
    """

    puzzle_id: int

    rows: int
    columns: int

    colors: int

    blocks: int

    color_offset: list[int]

    block_offset: list[int]

    first_block_record: int


def decode_value(record: list[int]) -> int:
    """
    Decode one encoded integer.

    JavaScript:

        a % m + b % m - c % m
    """

    return (
        record[0] % record[3]
        + record[1] % record[3]
        - record[2] % record[3]
    )


def decode_square(record: list[int]) -> int:
    """
    Decode quadratic value.

    JavaScript:

        x*x + y*2 + z
    """

    x = record[0] % record[3]
    y = record[1] % record[3]
    z = record[2] % record[3]

    return x * x + y * 2 + z


def read_header(data: list[list[int]]) -> DHeader:
    """
    Decode array header.
    """

    puzzle_id = decode_square(data[0])

    columns = decode_value(data[1])

    rows = decode_value(data[2])

    colors = decode_value(data[3])

    color_offset = data[4]

    V = colors + 5

    blocks = decode_square(data[V])

    block_offset = data[V + 1]

    first_block = V + 2

    return DHeader(
        puzzle_id=puzzle_id,
        rows=rows,
        columns=columns,
        colors=colors,
        blocks=blocks,
        color_offset=color_offset,
        block_offset=block_offset,
        first_block_record=first_block,
    )
