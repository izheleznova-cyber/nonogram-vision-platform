"""
Inspect database schema.
"""

from core.dataset.passport_database import PassportDatabase


def main() -> None:

    database = PassportDatabase()

    print("=" * 60)
    print("DATABASE SCHEMA")
    print("=" * 60)
    print()

    for info in database.schema().values():

        print(info.name)
        print(f"  builtin : {info.builtin}")
        print(f"  type     : {info.field_type}")
        print(f"  multiple : {info.multiple}")
        print(f"  unique   : {info.unique_count}")
        print()


if __name__ == "__main__":
    main()