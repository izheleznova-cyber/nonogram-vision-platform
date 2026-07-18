"""
Read passports from Excel workbook.
"""

from __future__ import annotations

from core.dataset.passport_reader import read_passports
from core.dataset.paths import WORKBOOK


def main() -> None:

    passports = read_passports(WORKBOOK)

    print("=" * 60)
    print("PASSPORTS")
    print("=" * 60)
    print()

    print(f"Workbook : {WORKBOOK}")
    print(f"Total    : {len(passports)}")
    print()

    # ------------------------------------------------------------
    # Проверяем, что основные текстовые поля читаются корректно
    # ------------------------------------------------------------

    first = passports[0]

    print("First passport")
    print(f"  ID          : {first.id}")
    print(f"  Title       : {first.title}")
    print(f"  Synonyms    : {first.synonyms}")
    print(f"  AuthorTitle : {first.author_title}")
    print()

    # ------------------------------------------------------------
    # Краткая информация по первым пяти паспортам
    # ------------------------------------------------------------

    for passport in passports[:5]:

        print(passport.id)
        print(f"  title        : {passport.title}")
        print(f"  synonyms     : {passport.synonyms}")
        print(f"  author_title : {passport.author_title}")
        print(f"  size         : {passport.width} x {passport.height}")
        print(f"  source       : {passport.source}")
        print(f"  page_id      : {passport.page_id}")
        print(f"  color        : {passport.color}")
        print()


if __name__ == "__main__":
    main()