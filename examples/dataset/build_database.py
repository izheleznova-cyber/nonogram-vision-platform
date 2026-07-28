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

    created = 0
    updated = 0
    skipped = 0

    for passport in passports:

        json_path = JSON_DIR / f"{passport.id}.json"

        if json_path.exists():
            skipped += 1
            continue

        save_passport(
            passport,
            JSON_DIR,
        )

        created += 1

    existing = skipped

    print("-" * 60)
    print(f"Existing : {existing}")
    print(f"Created  : {created}")
    print(f"Updated  : {updated}")
    print(f"Skipped  : {skipped}")


if __name__ == "__main__":
    main()