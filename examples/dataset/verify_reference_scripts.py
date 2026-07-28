"""
Verify decoding of all reference scripts.
"""

from __future__ import annotations

from core.dataset.builder import build_reference_dataset
from core.dataset.d_decoder import decode
from core.dataset.d_parser import load_d
from core.dataset.passport_reader import read_passports
from core.dataset.paths import (
    CACHE_DIR,
    WORKBOOK,
)


def main() -> None:

    passports = read_passports(WORKBOOK)

    dataset = build_reference_dataset(passports)

    print("=" * 90)
    print("VERIFY REFERENCE SCRIPTS")
    print("=" * 90)
    print()

    ok = 0

    for passport in dataset:

        script_path = (
            CACHE_DIR
            / f"{passport.page_id}_script.js"
        )

        try:

            d = load_d(script_path)

            puzzle = decode(d)

            print(
                f"{passport.worksheet_name:<10} "
                f"{passport.page_id:<6} "
                f"{puzzle.width:>2}x{puzzle.height:<2} "
                f"{passport.title}"
            )

            ok += 1

        except Exception as exc:

            print(
                f"{passport.worksheet_name:<10} "
                f"{passport.page_id:<6} "
                f"FAILED   "
                f"{passport.title}"
            )

            print(f"    {exc}")

    print()
    print("-" * 90)
    print(f"Decoded: {ok}/{len(dataset)}")


if __name__ == "__main__":
    main()