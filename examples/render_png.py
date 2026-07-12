from pathlib import Path

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.renderer import render_puzzle


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    output = Path("matrix.png")

    render_puzzle(
        puzzle,
        output,
    )

    print(f"Saved to {output}")


if __name__ == "__main__":
    main()
