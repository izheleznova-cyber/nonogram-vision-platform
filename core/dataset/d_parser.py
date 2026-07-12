"""
d_parser.py

Разбор массива 'var d' из JavaScript сайта nonograms.ru.

На первом этапе модуль только преобразует строку JavaScript
в обычный Python list.

Дальнейшие версии будут декодировать структуру массива.
"""

from __future__ import annotations

import ast
from pathlib import Path


def load_d(script_path: Path) -> list[list[int]]:
    """
    Загружает массив d из файла JavaScript.

    Parameters
    ----------
    script_path : Path
        Путь к файлу *.js.

    Returns
    -------
    list[list[int]]
        Содержимое массива d.
    """

    text = script_path.read_text(encoding="utf-8")

    prefix = "var d="

    position = text.find(prefix)

    if position == -1:
        raise ValueError("Variable 'd' not found.")

    text = text[position + len(prefix):]

    text = text.strip()

    if text.endswith(";"):
        text = text[:-1]

    return ast.literal_eval(text)


def number_of_records(data: list[list[int]]) -> int:
    """
    Возвращает количество записей массива d.
    """

    return len(data)


def tuple_size(data: list[list[int]]) -> int:
    """
    Возвращает длину одной записи.
    """

    if not data:
        return 0

    return len(data[0])


def min_value(data: list[list[int]]) -> int:
    """
    Минимальное число массива.
    """

    return min(v for row in data for v in row)


def max_value(data: list[list[int]]) -> int:
    """
    Максимальное число массива.
    """

    return max(v for row in data for v in row)
