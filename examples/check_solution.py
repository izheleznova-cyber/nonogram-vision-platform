from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.player import PlayerBoard
from core.puzzle.checker import is_solved


PAGE_ID = 1039


def main():

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    board = PlayerBoard.create(
        puzzle.width,
        puzzle.height,
    )

    print("Empty board:")
    print(is_solved(puzzle, board))

    #
    # Copy solution
    #

    for r in range(puzzle.height):

        for c in range(puzzle.width):

            if puzzle.matrix[r][c] != 0:

                board.fill(r, c)

    print("Solved board:")
    print(is_solved(puzzle, board))


if __name__ == "__main__":
    main()
