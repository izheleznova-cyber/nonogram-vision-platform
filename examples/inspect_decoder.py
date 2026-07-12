"""
inspect_decoder.py

First test of d_decoder.
"""

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    print("=" * 60)
    print("PUZZLE")
    print("=" * 60)

    print()

    print(f"Rows    : {puzzle.rows}")
    print(f"Columns : {puzzle.columns}")
    print(f"Colors  : {puzzle.colors}")

    print()

    print("Matrix size:")

    print(len(puzzle.matrix))

    print(len(puzzle.matrix[0]))


if __name__ == "__main__":
    main()
