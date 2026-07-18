"""
passport_reader.py

Read passport records from Excel workbook.
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet

from core.dataset.nonograms_url import get_page_id
from core.dataset.nonograms_url import get_source
from core.dataset.passport_record import PassportRecord


def _read_fields(sheet: Worksheet) -> dict[str, str]:
    """
    Read passport fields from columns J-K.
    """

    fields: dict[str, str] = {}

    row = 3

    while True:

        key = sheet[f"J{row}"].value

        if key is None:
            break

        value = sheet[f"K{row}"].value

        fields[str(key).strip()] = (
            "" if value is None else str(value).strip()
        )

        row += 1

    return fields


def _to_int(value: str | None) -> int:
    """
    Safe conversion to int.
    Empty values become zero.
    """

    if value in (None, ""):
        return 0

    return int(value)

def _to_list(value: str | None) -> list[str]:
    """
    Split comma-separated values.
    """

    if not value:
        return []

    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ] 


def read_passports(
    workbook_path: Path,
) -> list[PassportRecord]:
    """
    Read all passport sheets from workbook.
    """

    workbook = load_workbook(
        workbook_path,
        data_only=True,
    )

    passports: list[PassportRecord] = []

    # ------------------------------------------------------------------
    # Первые четыре листа служебные:
    #
    #   Dictionary
    #   Оглавление
    #   000
    #   идеи курса
    #
    # Паспорта начинаются с пятого листа.
    # ------------------------------------------------------------------

    for sheet in workbook.worksheets[4:]:

        url = sheet["B2"].value

        if url is None:
            continue

        url = str(url).strip()

        if not url.startswith("http"):
            raise ValueError(
                f"{sheet.title}: invalid URL: {url!r}"
            )

        fields = _read_fields(sheet)

        passport = PassportRecord(

            worksheet_name=sheet.title,

            id=fields.get("ID", ""),

            width=_to_int(fields.get("Width")),
            height=_to_int(fields.get("Height")),
            pixel_count=_to_int(fields.get("PixelCount")),

            category=fields.get("Category", ""),
            subcategory=fields.get("Subcategory", ""),

            title=fields.get("Title", ""),
            synonyms=_to_list(fields.get("Synonyms")),
            author_title=fields.get("AuthorTitle", ""),

            source=get_source(url),
            url=url,
            page_id=get_page_id(url),

            difficulty=_to_int(fields.get("Difficulty pic")),
            subject=fields.get("Sujet", ""),
            recognition_level=fields.get("RecognitionLevel", ""),

            has_face=fields.get("HasFace", "").lower() == "yes",
            face_size=fields.get("FaceSize", ""),
            orientation=fields.get("Orientation", ""),

            emotion=fields.get("Emotion", "").lower() == "yes",
            context=fields.get("Context", "").lower() == "yes",
            color=fields.get("Color", ""),

            uncertainty=fields.get("Uncertainty recognize", ""),
        )

        passports.append(passport)

    return passports