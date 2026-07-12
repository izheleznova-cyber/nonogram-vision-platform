"""
inspect_d.py

Исследование структуры массива d.

На данном этапе программа НЕ пытается понять смысл данных.
Она только показывает первые записи массива и статистику.
"""

from collections import Counter

from core.dataset.d_parser import load_d
from core.dataset.paths import CACHE_DIR


PAGE_ID = 1039


def main() -> None:

    script_path = CACHE_DIR / f"{PAGE_ID}_script.js"

    data = load_d(script_path)

    print("=" * 60)
    print("ARRAY d INSPECTION")
    print("=" * 60)

    print()

    print(f"Page ID      : {PAGE_ID}")
    print(f"Records      : {len(data)}")

    print()

    print("First 30 records")
    print("-" * 60)

    for i, row in enumerate(data[:30]):
        print(f"{i:3d}: {row}")

    print()

    print("Last 10 records")
    print("-" * 60)

    start = max(0, len(data) - 10)

    for i in range(start, len(data)):
        print(f"{i:3d}: {data[i]}")

    print()

    print("Tuple sizes")
    print("-" * 60)

    lengths = Counter(len(row) for row in data)

    for size, count in sorted(lengths.items()):
        print(f"{size:2d} values : {count}")

    print()

    print("Column statistics")
    print("-" * 60)

    for column in range(4):

        values = [row[column] for row in data]

        print(
            f"Column {column}: "
            f"min={min(values):3d} "
            f"max={max(values):3d}"
        )


if __name__ == "__main__":
    main()
