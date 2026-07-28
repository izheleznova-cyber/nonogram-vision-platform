"""
Read JSON database.
"""

from __future__ import annotations

from core.dataset.json_reader import read_database


def main() -> None:

    passports = read_database()

    print("=" * 60)
    print("READ DATABASE")
    print("=" * 60)
    print()

    print(f"Loaded: {len(passports)} passports")


if __name__ == "__main__":
    main()
