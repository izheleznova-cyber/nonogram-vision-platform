from core.dataset.d_parser import load_d
from core.dataset.d_decoder import decode
from core.dataset.paths import CACHE_DIR

from core.puzzle.hints import generate_hints
from core.puzzle.runs import (
    matrix_runs,
    column_runs,
)

PAGE_ID = 1039


def main() -> None:

    # ---------------------------------------------------------
    # Load puzzle
    # ---------------------------------------------------------

    script = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script)

    puzzle = decode(data)

    # ---------------------------------------------------------
    # Build hints
    # ---------------------------------------------------------

    row_hints, column_hints = generate_hints(
        puzzle.matrix
    )

    puzzle.row_hints = row_hints
    puzzle.column_hints = column_hints

    # ---------------------------------------------------------
    # Build cached runs
    # ---------------------------------------------------------

    puzzle.row_runs = matrix_runs(
        puzzle.matrix
    )

    puzzle.column_runs = column_runs(
        puzzle.matrix
    )

    # ---------------------------------------------------------
    # Puzzle info
    # ---------------------------------------------------------

    print("=" * 80)
    print("PUZZLE")
    print("=" * 80)

    print(
        f"Size: {puzzle.width} x {puzzle.height}"
    )

    print()

    # ---------------------------------------------------------
    # Rows
    # ---------------------------------------------------------

    print("=" * 80)
    print("ROWS")
    print("=" * 80)

    for row in range(puzzle.height):

        hints = puzzle.row_hints[row]
        runs = puzzle.row_runs[row]

        print(
            f"{row:3d}  "
            f"hints={str(hints):20s} "
            f"runs={runs}"
        )

    print()

    # ---------------------------------------------------------
    # Columns
    # ---------------------------------------------------------

    print("=" * 80)
    print("COLUMNS")
    print("=" * 80)

    for col in range(puzzle.width):

        hints = puzzle.column_hints[col]
        runs = puzzle.column_runs[col]

        print(
            f"{col:3d}  "
            f"hints={str(hints):20s} "
            f"runs={runs}"
        )

    print()

    # ---------------------------------------------------------
    # Verify rows
    # ---------------------------------------------------------

    print("=" * 80)
    print("VERIFY ROWS")
    print("=" * 80)

    row_errors = 0

    for row in range(puzzle.height):

        hint_lengths = [
            hint[0]
            for hint in puzzle.row_hints[row]
        ]

        run_lengths = [
            length
            for _, length in puzzle.row_runs[row]
        ]

        ok = hint_lengths == run_lengths

        status = "OK" if ok else "ERROR"

        print(
            f"Row {row:2d}: "
            f"{status:5s} "
            f"hints={str(hint_lengths):18s} "
            f"runs={str(run_lengths):18s} "
            f"coords={puzzle.row_runs[row]}"
        )

        if not ok:
            row_errors += 1

    print()

    # ---------------------------------------------------------
    # Verify columns
    # ---------------------------------------------------------

    print("=" * 80)
    print("VERIFY COLUMNS")
    print("=" * 80)

    column_errors = 0

    for col in range(puzzle.width):

        hint_lengths = [
            hint[0]
            for hint in puzzle.column_hints[col]
        ]

        run_lengths = [
            length
            for _, length in puzzle.column_runs[col]
        ]

        ok = hint_lengths == run_lengths

        status = "OK" if ok else "ERROR"

        print(
            f"Col {col:2d}: "
            f"{status:5s} "
            f"hints={str(hint_lengths):18s} "
            f"runs={str(run_lengths):18s} "
            f"coords={puzzle.column_runs[col]}"
        )

        if not ok:
            column_errors += 1

    print()
    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print(f"Puzzle size     : {puzzle.width} x {puzzle.height}")
    print(f"Rows checked    : {puzzle.height}")
    print(f"Columns checked : {puzzle.width}")
    print()
    print(f"Row errors      : {row_errors}")
    print(f"Column errors   : {column_errors}")

    print()

    if row_errors == 0 and column_errors == 0:
        print("SUCCESS")
        print("All cached runs match puzzle hints.")
    else:
        print("FAILED")

    print("=" * 80)

if __name__ == "__main__":
    main()
