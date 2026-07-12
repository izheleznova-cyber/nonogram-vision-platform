"""
renderer.py

Render Puzzle objects.

Version 1

    - render solution matrix
    - black/white rendering
    - PNG output

Future versions will add:

    - grid
    - row hints
    - column hints
    - colors
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

from .model import Puzzle


CELL_SIZE = 12


def render_matrix(
    matrix: list[list[int]],
    output_path: Path,
    cell_size: int = CELL_SIZE,
) -> None:
    """
    Render puzzle matrix to a PNG image.
    """

    height = len(matrix)
    width = len(matrix[0])

    image = Image.new(
        "RGB",
        (
            width * cell_size,
            height * cell_size,
        ),
        "white",
    )

    pixels = image.load()

    for row in range(height):

        for col in range(width):

            if matrix[row][col] == 0:
                rgb = (255, 255, 255)
            else:
                rgb = (0, 0, 0)

            x0 = col * cell_size
            y0 = row * cell_size

            for dy in range(cell_size):

                for dx in range(cell_size):

                    pixels[
                        x0 + dx,
                        y0 + dy,
                    ] = rgb

    image.save(output_path)


def render_puzzle(
    puzzle: Puzzle,
    output_path: Path,
    cell_size: int = CELL_SIZE,
) -> None:
    """
    Render Puzzle object.

    Public renderer interface.

    Parameters
    ----------
    puzzle
        Puzzle object.

    output_path
        Output PNG filename.

    cell_size
        Pixel size of one puzzle cell.
    """

    render_matrix(
        puzzle.matrix,
        output_path,
        cell_size,
    )
