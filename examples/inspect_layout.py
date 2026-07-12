"""
inspect_layout.py

Inspect puzzle layout.
"""

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.hints import generate_hints
from core.puzzle.layout import calculate_layout


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    # Generate hints
    row_hints, column_hints = generate_hints(
        puzzle.matrix
    )

    # Store hints inside Puzzle
    puzzle.row_hints = row_hints
    puzzle.column_hints = column_hints

    # Calculate layout
    layout = calculate_layout(puzzle)

    print("=" * 60)
    print("PUZZLE LAYOUT")
    print("=" * 60)

    print()

    print(f"Puzzle size       : {puzzle.width} x {puzzle.height}")
    print(f"Cell size         : {layout.cell_size}")

    print()

    print(f"Left hint columns : {layout.left_hint_cells}")
    print(f"Top hint rows     : {layout.top_hint_cells}")

    print()

    print(f"Puzzle origin     : ({layout.puzzle_x}, {layout.puzzle_y})")

    print()

    print(f"Puzzle pixels     : {layout.puzzle_width} x {layout.puzzle_height}")

    print(f"Image size        : {layout.image_width} x {layout.image_height}")


if __name__ == "__main__":
    main()
