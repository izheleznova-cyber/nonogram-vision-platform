"""
renderer.py

Rendering of a nonogram.
"""

from pathlib import Path

from PIL import Image
from PIL import ImageDraw

from .layout import Layout
from .layout import calculate_layout
from .model import Puzzle


BACKGROUND = (255, 255, 255)

GRID_COLOR = (180, 180, 180)
MAJOR_GRID_COLOR = (0, 0, 0)

THIN_WIDTH = 1
THICK_WIDTH = 2


def render_puzzle(
    puzzle: Puzzle,
    output: Path,
) -> None:
    """
    Render puzzle to PNG file.
    """

    layout = calculate_layout(puzzle)

    image = Image.new(
        "RGB",
        (layout.image_width, layout.image_height),
        BACKGROUND,
    )

    draw = ImageDraw.Draw(image)

    _draw_grid(
        draw,
        layout,
    )

    image.save(output)


def _draw_grid(
    draw: ImageDraw.ImageDraw,
    layout: Layout,
) -> None:
    """
    Draw puzzle grid.
    """

    left = layout.puzzle_x
    top = layout.puzzle_y

    right = left + layout.puzzle_width
    bottom = top + layout.puzzle_height

    cell = layout.cell_size

    columns = layout.puzzle_width // cell
    rows = layout.puzzle_height // cell

    #
    # Vertical lines
    #

    for x in range(columns + 1):

        xx = left + x * cell

        major = (x % 5) == 0

        draw.line(
            [(xx, top), (xx, bottom)],
            fill=MAJOR_GRID_COLOR if major else GRID_COLOR,
            width=THICK_WIDTH if major else THIN_WIDTH,
        )

    #
    # Horizontal lines
    #

    for y in range(rows + 1):

        yy = top + y * cell

        major = (y % 5) == 0

        draw.line(
            [(left, yy), (right, yy)],
            fill=MAJOR_GRID_COLOR if major else GRID_COLOR,
            width=THICK_WIDTH if major else THIN_WIDTH,
        )
