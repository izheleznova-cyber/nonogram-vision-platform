"""
Render one nonogram into PNG.

Example:

    python -m examples.puzzle.render_png
"""

from pathlib import Path

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.renderer import render_puzzle


PAGE_ID = 1039


def main() -> None:
    """
    Render one puzzle from cached JavaScript.
    """

    # ---------------------------------------------------------
    # Load puzzle
    # ---------------------------------------------------------

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    # ---------------------------------------------------------
    # Output file
    # ---------------------------------------------------------

    output_dir = (
        Path(__file__).resolve().parents[2]
        / "output"
        / "renders"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output = output_dir / f"render_{PAGE_ID}.png"

    # ---------------------------------------------------------
    # Render
    # ---------------------------------------------------------

    render_puzzle(
        puzzle,
        output,
    )

    print()
    print("============================================")
    print("PUZZLE RENDERED")
    print("============================================")
    print(f"Page ID : {PAGE_ID}")
    print(f"Saved to: {output}")
    print()


if __name__ == "__main__":
    main()