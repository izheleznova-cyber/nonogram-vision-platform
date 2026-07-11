"""
Пример чтения коллекции паспортов.
"""

from collections import Counter

from core.dataset.paths import WORKBOOK
from core.dataset.passport_reader import read_passports


def main() -> None:

    passports = read_passports(WORKBOOK)

    print("=" * 60)
    print("NONOGRAM PASSPORT COLLECTION")
    print("=" * 60)

    print(f"Total passports : {len(passports)}")

    print()

    # ------------------------------------------------------------
    # Statistics by color
    # ------------------------------------------------------------

    color_stats = Counter(
        passport.color_type
        for passport in passports
    )

    print("Color types:")

    for color, count in sorted(color_stats.items()):
        print(f"  {color:8} : {count}")

    print()

    # ------------------------------------------------------------
    # Statistics by source
    # ------------------------------------------------------------

    source_stats = Counter(
        passport.source
        for passport in passports
    )

    print("Sources:")

    for source, count in sorted(source_stats.items()):
        print(f"  {source:12} : {count}")

    print()

    print("-" * 60)
    print("First five passports:")
    print("-" * 60)

    for passport in passports[:5]:
        print(passport)


if __name__ == "__main__":
    main()
