"""
Read passport database from JSON files.
"""

from __future__ import annotations

import json
from dataclasses import fields
from pathlib import Path

from core.dataset.passport_record import PassportRecord
from core.dataset.paths import JSON_DIR


def read_passport(json_path: Path) -> PassportRecord:
    """
    Read one passport from JSON.
    """

    with json_path.open(
        "r",
        encoding="utf-8",
    ) as file:

        data = json.load(file)

    passport_fields = {
        field.name
        for field in fields(PassportRecord)
    }

    values = {
        key: value
        for key, value in data.items()
        if key in passport_fields
    }

    return PassportRecord(**values)


def read_database(
    database_dir: Path = JSON_DIR,
) -> list[PassportRecord]:
    """
    Read all passports from JSON database.
    """

    passports: list[PassportRecord] = []

    for json_path in sorted(database_dir.glob("*.json")):

        passports.append(
            read_passport(json_path)
        )

    return passports
