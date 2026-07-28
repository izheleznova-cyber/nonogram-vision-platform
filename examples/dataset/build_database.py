"""
Build JSON database from Excel passports.
"""

from __future__ import annotations

from core.dataset.json_writer import save_passport
from core.dataset.passport_reader import read_passports
from core.dataset.paths import (
    JSON_DIR,
    WORKBOOK,
)


def main() -> None:

    passports = read_passports(WORKBOOK)

    print("=" * 60)
    print("BUILD JSON DATABASE")
    print("=" * 60)
    print()

    for passport in passports:

        save_passport(
            passport,
            JSON_DIR,
        )

    print(f"Saved {len(passports)} passports.")


if __name__ == "__main__":
    main()
