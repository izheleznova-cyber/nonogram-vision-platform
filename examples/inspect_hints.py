"""
inspect_hints.py

Generate row and column hints
from a decoded puzzle.
"""

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.hints import generate_hints


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    row_hints, column_hints = generate_hints(
        puzzle.matrix
    )

    print("=" * 60)
    print("HINTS")
    print("=" * 60)

    print()

    print("Rows:", len(row_hints))
    print("Columns:", len(column_hints))

    print()

    print("First 10 row hints")

    print("-" * 60)

    for i in range(min(10, len(row_hints))):

        print(f"{i:2d}: {row_hints[i]}")

    print()

    print("First 10 column hints")

    print("-" * 60)

    for i in range(min(10, len(column_hints))):

        print(f"{i:2d}: {column_hints[i]}")


if __name__ == "__main__":
    main()
