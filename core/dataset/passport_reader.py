"""
passport_reader.py

Чтение паспортов японских кроссвордов из Excel.

Модуль преобразует книгу nonogram_passports.xlsm
в список объектов PassportRecord.

Никакой другой обработки здесь не выполняется.
"""

from pathlib import Path

from openpyxl import load_workbook

from core.dataset.excel_schema import (
    FIRST_PASSPORT_SHEET,
    PassportCells,
)
from core.dataset.nonograms_url import (
    get_page_id,
    get_source,
)
from core.dataset.passport_record import PassportRecord


def read_passports(workbook_path: Path) -> list[PassportRecord]:
    """
    Считывает все паспорта из Excel-книги.

    Parameters
    ----------
    workbook_path : Path
        Путь к файлу nonogram_passports.xlsm.

    Returns
    -------
    list[PassportRecord]
        Список паспортов.
    """

    workbook = load_workbook(
        workbook_path,
        data_only=True,
    )

    passports: list[PassportRecord] = []

    worksheets = workbook.worksheets

    for sheet in worksheets[FIRST_PASSPORT_SHEET - 1:]:

        url = sheet[PassportCells.URL].value

        if url is None:
            continue

        url = str(url).strip()

        color_type = sheet[PassportCells.COLOR_TYPE].value

        if color_type is None:
            color_type = ""

        passport = PassportRecord(
            worksheet_name=sheet.title,
            url=url,
            source=get_source(url),
            page_id=get_page_id(url),
            color_type=str(color_type).strip(),
        )

        passports.append(passport)

    return passports
