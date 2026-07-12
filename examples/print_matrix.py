"""
print_matrix.py

Print decoded puzzle matrix.
"""

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    print("=" * 80)
    print("DECODED MATRIX")
    print("=" * 80)

    print()

    for row in puzzle.matrix:

        line = "".join(
            "██" if cell else "  "
            for cell in row
        )

        print(line)


if __name__ == "__main__":
    main()
