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

FONT_SIZE = 10

HINT_TEXT_OFFSET_X = 2
HINT_TEXT_OFFSET_Y = 0

BACKGROUND = (255, 255, 255)

GRID_COLOR = (180, 180, 180)
MAJOR_GRID_COLOR = (0, 0, 0)

THIN_WIDTH = 1
THICK_WIDTH = 2

DEBUG_HINT_GRID = False
DEBUG_HINT_INDEX = False 


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

    if DEBUG_HINT_GRID:
        _draw_hint_grid(
            draw,
            layout,
        )

    if DEBUG_HINT_INDEX:
        _draw_hint_indexes(
            draw,
            layout,
        )
    
    _draw_cells(
    draw,
    puzzle,
    layout,
    )

    
    _draw_row_hints(
    draw,
    puzzle,
    layout,
    )

    _draw_column_hints(
    draw,
    puzzle,
    layout,
    )

    
    _draw_coordinates(
        draw,
        puzzle,
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

from PIL import ImageFont

try:
    FONT = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        10,
    )
except OSError:
    FONT = ImageFont.load_default()


def _draw_row_hints(
    draw: ImageDraw.ImageDraw,
    puzzle: Puzzle,
    layout: Layout,
) -> None:
    """
    Draw left row hints.
    """

    cell = layout.cell_size

    #
    # Левая граница области подсказок
    #
    left = (
        layout.puzzle_x
        - layout.left_hint_cells * cell
    )
    

    for row, hints in enumerate(puzzle.row_hints):

        #
        # Верхняя координата строки
        #
        y = (
            layout.puzzle_y
            + row * cell
        )

        hint_count = len(hints)

        #
        # Первая занятая ячейка
        #
        start_cell = (
            layout.left_hint_cells
            - hint_count
        )

        for index, (length, color) in enumerate(hints):

            #
            # Левая граница текущей ячейки
            #
            cell_left = (
                left
                + (start_cell + index) * cell
            )

            text = str(length)

            #
            # Только высота текста.
            # По X больше НЕ центрируем.
            #
            bbox = draw.textbbox(
                (0, 0),
                text,
                font=FONT,
            )

            text_height = bbox[3] - bbox[1]

            draw.text(
                (
                    cell_left + 2,
                    y + (cell - text_height) // 2,
                ),
                text,
                fill="black",
                font=FONT,
            )

def _draw_column_hints(
    draw: ImageDraw.ImageDraw,
    puzzle: Puzzle,
    layout: Layout,
) -> None:
    """
    Draw top column hints.
    """

    cell = layout.cell_size

    #
    # Верхняя граница области подсказок
    #
    top = (
        layout.puzzle_y
        - layout.top_hint_cells * cell
    )

    for col, hints in enumerate(puzzle.column_hints):

        #
        # Левая координата столбца
        #
        x = (
            layout.puzzle_x
            + col * cell
        )

        hint_count = len(hints)

        #
        # Первая занятая ячейка
        #
        start_cell = (
            layout.top_hint_cells
            - hint_count
        )

        for index, (length, color) in enumerate(hints):

            #
            # Верхняя граница текущей ячейки
            #
            cell_top = (
                top
                + (start_cell + index) * cell
            )

            text = str(length)

            bbox = draw.textbbox(
                (0, 0),
                text,
                font=FONT,
            )

            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            draw.text(
                (
                    x + (cell - text_width) // 2,
                    cell_top + (cell - text_height) // 2,
                ),
                text,
                fill="black",
                font=FONT,
            )


def _draw_hint_grid(
    draw: ImageDraw.ImageDraw,
    layout: Layout,
) -> None:
    """
    Draw hint area grid (debug only).
    """

    cell = layout.cell_size

    left = layout.puzzle_x - layout.left_hint_cells * cell
    right = layout.puzzle_x

    top = layout.puzzle_y
    bottom = layout.puzzle_y + layout.puzzle_height

    #
    # Vertical lines
    #

    for i in range(layout.left_hint_cells + 1):

        x = left + i * cell

        draw.line(
            [(x, top), (x, bottom)],
            fill=(220, 220, 220),
            width=1,
        )

    #
    # Horizontal lines
    #

    rows = layout.puzzle_height // cell

    for i in range(rows + 1):

        y = top + i * cell

        draw.line(
            [(left, y), (right, y)],
            fill=(220, 220, 220),
            width=1,
        )

def _draw_hint_indexes(
    draw: ImageDraw.ImageDraw,
    layout: Layout,
) -> None:
    """
    Draw indexes of hint cells (debug only).
    """

    cell = layout.cell_size

    left = layout.puzzle_x - layout.left_hint_cells * cell

    for row in range(layout.puzzle_height // cell):

        y = (
            layout.puzzle_y
            + row * cell
            + cell // 2
        )

        for col in range(layout.left_hint_cells):

            x = (
                left
                + col * cell
                + cell // 2
            )

            text = str(col)

            bbox = draw.textbbox(
                (0, 0),
                text,
                font=FONT,
            )

            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]

            draw.text(
                (
                    x - w // 2,
                    y - h // 2,
                ),
                text,
                fill="red",
                font=FONT,
            )
def _draw_coordinates(
    draw: ImageDraw.ImageDraw,
    puzzle: Puzzle,
    layout: Layout,
) -> None:
    """
    Draw row and column coordinate labels.
    """

    cell = layout.cell_size

    #
    # Row numbers (right)
    #

    x = layout.puzzle_x + layout.puzzle_width + 4

    for row in range(5, puzzle.height + 1, 5):

        y = (
            layout.puzzle_y
            + (row - 1) * cell
            + cell // 2
        )

        text = str(row)

        bbox = draw.textbbox(
            (0, 0),
            text,
            font=FONT,
        )

        h = bbox[3] - bbox[1]

        draw.text(
            (
                x,
                y - h // 2,
            ),
            text,
            fill="black",
            font=FONT,
        )

    #
    # Last row (if not multiple of 5)
    #

    if puzzle.height % 5:

        row = puzzle.height

        y = (
            layout.puzzle_y
            + (row - 1) * cell
            + cell // 2
        )

        text = str(row)

        bbox = draw.textbbox(
            (0, 0),
            text,
            font=FONT,
        )

        h = bbox[3] - bbox[1]

        draw.text(
            (
                x,
                y - h // 2,
            ),
            text,
            fill="black",
            font=FONT,
        )

    #
    # Column numbers (bottom)
    #

    y = layout.puzzle_y + layout.puzzle_height + 2

    for col in range(5, puzzle.width + 1, 5):

        x = (
            layout.puzzle_x
            + (col - 1) * cell
            + cell // 2
        )

        text = str(col)

        bbox = draw.textbbox(
            (0, 0),
            text,
            font=FONT,
        )

        w = bbox[2] - bbox[0]

        draw.text(
            (
                x - w // 2,
                y,
            ),
            text,
            fill="black",
            font=FONT,
        )

def _draw_cells(
    draw: ImageDraw.ImageDraw,
    puzzle: Puzzle,
    layout: Layout,
) -> None:
    """
    Draw filled cells.
    """

    cell = layout.cell_size

    for row in range(puzzle.height):

        for col in range(puzzle.width):

            value = puzzle.matrix[row][col]

            #
            # 0 = empty
            #
            if value == 0:
                continue

            left = layout.puzzle_x + col * cell
            top = layout.puzzle_y + row * cell

            draw.rectangle(
                (
                    left + 1,
                    top + 1,
                    left + cell - 1,
                    top + cell - 1,
                ),
                fill="black",
            )