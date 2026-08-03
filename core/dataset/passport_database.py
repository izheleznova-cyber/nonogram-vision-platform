"""
Passport database.

High-level interface for working with the passport JSON database.
"""

from __future__ import annotations

from dataclasses import fields
from pathlib import Path
from typing import Any
from dataclasses import fields

from core.dataset.json_reader import read_database
from core.dataset.passport_record import PassportRecord
from core.dataset.paths import JSON_DIR
from core.dataset.field_info import FieldInfo

from core.lesson.query import LessonQuery

class PassportDatabase:
    """
    Collection of passport records.
    """

    def __init__(
        self,
        database_dir: Path =JSON_DIR,
    ) -> None:

        self._database_dir = database_dir
        self._records: list[PassportRecord] = read_database(database_dir)

    @property
    def records(self) -> list[PassportRecord]:
        """
        Return all passport records.
        """
        return self._records

    def __len__(self) -> int:
        """
        Return number of passports.
        """
        return len(self._records)

    def record(
        self,
        passport_id: str,
    ) -> PassportRecord:
        """
        Return passport by identifier.
        """

        for record in self._records:

            if record.id == passport_id:
                return record

        raise KeyError(
            f"Unknown passport: {passport_id}"
        )

    def search(
        self,
        query: LessonQuery,
    ) -> list[PassportRecord]:
        """
        Search passports matching lesson query.
        """

        result: list[PassportRecord] = []

        for passport in self.records:

            #
            # Width
            #

            if (
                query.max_width is not None
                and passport.width > query.max_width
            ):
                continue

            #
            # Height
            #

            if (
                query.max_height is not None
                and passport.height > query.max_height
            ):
                continue

            #
            # Category
            #

            if (
                query.category is not None
                and passport.category != query.category
            ):
                continue

            #
            # Difficulty
            #

            if (
                query.difficulty is not None
                and passport.difficulty != query.difficulty
            ):
                continue

            #
            # Color
            #

            if (
                query.color is not None
                and passport.color != query.color
            ):
                continue

            result.append(passport)

        return result


    @property
    def builtin_fields(self) -> list[str]:
        """
        Return standard PassportRecord fields.
        """

        return sorted(
            field.name
            for field in fields(PassportRecord)
            if field.name != "extra"
        )

    @property
    def custom_fields(self) -> list[str]:
        """
        Return dynamically discovered fields.
        """

        names: set[str] = set()

        for record in self._records:

            if record.extra:
                names.update(record.extra.keys())

        return sorted(names)

    def fields(self) -> list[str]:
        """
        Return every available field.
        """

        return sorted(
            set(self.builtin_fields)
            | set(self.custom_fields)
        )

    def values(
        self,
        field_name: str,
    ) -> list[Any]:
        """
        Return every distinct value of a field.
        """

        values: set[Any] = set()

        for record in self._records:

            #
            # Built-in field
            #

            if hasattr(record, field_name):

                value = getattr(record, field_name)

                if value is None:
                    continue

                #
                # Простые типы
                #

                if isinstance(value, (str, int, float, bool)):
                    values.add(value)

                #
                # Список
                #

                elif isinstance(value, list):
                    values.update(value)

                #
                # Кортеж
                #

                elif isinstance(value, tuple):
                    values.update(value)

                #
                # Остальное пока пропускаем
                #

                continue

            #
            # Custom field
            #

            if field_name in record.extra:

                value = record.extra[field_name]

                if value is not None:
                    values.add(value)

        return sorted(values)

    def schema(self) -> dict[str, FieldInfo]:
        """
        Return database schema.
        """

        schema: dict[str, FieldInfo] = {}

        #
        # Built-in fields
        #

        for field in fields(PassportRecord):

            if field.name == "extra":
                continue

            #
            # All unique values of this field
            #

            values = self.values(field.name)

            #
            # Does the field contain None?
            #

            nullable = any(
                getattr(record, field.name) is None
                for record in self.records
            )

            #
            # Create field description
            #

            schema[field.name] = FieldInfo(
                name=field.name,
                builtin=True,
                field_type=field.type,
                multiple="list" in str(field.type),
                nullable=nullable,
                unique_count=len(values),
            )

        #
        # Custom fields
        #

        for name in self.custom_fields:

            values = self.values(name)

            #
            # Determine field type
            #

            if values:
                value_type = type(values[0])
            else:
                value_type = str

            #
            # Is the field absent in at least one passport?
            #

            nullable = any(
                name not in record.extra
                or record.extra[name] is None
                for record in self.records
            )

            #
            # Create field description
            #

            schema[name] = FieldInfo(
                name=name,
                builtin=False,
                field_type=value_type,
                multiple=False,
                nullable=nullable,
                unique_count=len(values),
            )

        return schema