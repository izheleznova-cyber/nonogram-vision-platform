"""
Select reference dataset.
"""

from __future__ import annotations

from core.dataset.builder import build_reference_dataset
from core.dataset.passport_reader import read_passports
from core.dataset.paths import WORKBOOK


def main() -> None:

    passports = read_passports(WORKBOOK)

    dataset = build_reference_dataset(passports)

    print("=" * 60)
    print("REFERENCE DATASET")
    print("=" * 60)
    print()

    for passport in dataset:

        print(
            f"{passport.width:2} x {passport.height:2}"
            f"   page={passport.page_id:<6}"
            f"   id={passport.id:<10}"
            f"   {passport.title}"
        )

    print()
    print(f"Selected: {len(dataset)} puzzles")


if __name__ == "__main__":
    main()