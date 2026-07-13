from pathlib import Path

from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.player import PlayerBoard
from core.puzzle.renderer import render_puzzle


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    board = PlayerBoard.create(
        puzzle.width,
        puzzle.height,
    )

    #
    # Simulate student actions
    #

    board.fill(5, 5)
    board.fill(5, 6)
    board.fill(5, 7)

    board.fill(10, 15)

    board.cross(3, 4)
    board.cross(8, 12)
    board.cross(20, 20)

    output = Path("player_board.png")

    render_puzzle(
        puzzle,
        output,
        board=board,
    )

    print(f"Saved to {output}")


if __name__ == "__main__":
    main()
