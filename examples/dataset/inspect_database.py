"""
Inspect passport database.
"""

from __future__ import annotations

from core.dataset.passport_database import PassportDatabase


def main() -> None:

    database = PassportDatabase()

    print("=" * 60)
    print("PASSPORT DATABASE")
    print("=" * 60)
    print()

    print(f"Passports : {len(database)}")
    print()

    print("FIELDS")
    print("-" * 60)

    for field in database.fields():
        print(field)


if __name__ == "__main__":
    main()
