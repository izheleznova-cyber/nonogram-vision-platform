"""
inspect_script.py

Исследование JavaScript-файла, извлеченного из HTML.

Скрипт НЕ выполняет парсинг кроссворда.
Он только исследует структуру массива d.
"""

import ast

from core.dataset.paths import CACHE_DIR


PAGE_ID = 1039


def main() -> None:

    script_path = CACHE_DIR / f"{PAGE_ID}_script.js"

    print("=" * 60)
    print("JAVASCRIPT INSPECTION")
    print("=" * 60)
    print()

    print(f"File : {script_path}")

    text = script_path.read_text(
        encoding="utf-8",
    )

    # ------------------------------------------------------------
    # Находим переменную d
    # ------------------------------------------------------------

    text = text.lstrip()

    prefix = "var d="

    position = text.find(prefix)

    if position == -1:
        print("Variable 'd' not found.")
        return

    text = text[position + len(prefix):]

    text = text.strip()

    if text.endswith(";"):
        text = text[:-1]

    print()
    print("First 100 characters:")
    print(text[:100])
    print()

    # ------------------------------------------------------------
    # Преобразуем JavaScript-массив в Python
    # ------------------------------------------------------------

    data = ast.literal_eval(text)

    print(f"Elements : {len(data)}")

    print()
    print("First element:")
    print(data[0])

    print()
    print("Last element:")
    print(data[-1])

    lengths = {len(item) for item in data}

    print()
    print(f"Tuple sizes : {sorted(lengths)}")

    if lengths == {4}:
        print("All elements contain exactly 4 integers.")

    values = [value for row in data for value in row]

    print()
    print(f"Minimum value : {min(values)}")
    print(f"Maximum value : {max(values)}")

    print()
    print("Column statistics:")

    for column in range(4):

        column_values = [row[column] for row in data]

        print(
            f"Column {column}: "
            f"min={min(column_values)}  "
            f"max={max(column_values)}"
        )

    print()
    print("First 10 records:")

    for row in data[:10]:
        print(row)


if __name__ == "__main__":
    main()
