"""
Database field description.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class FieldInfo:
    """
    Description of one database field.
    """

    #
    # General information
    #

    name: str
    builtin: bool

    #
    # Data description
    #

    field_type: Any
    multiple: bool
    nullable: bool

    #
    # Statistics
    #

    unique_count: int

    @property
    def searchable(self) -> bool:
        """
        Whether the field is suitable for filtering.
        """

        #
        # Technical identifiers
        #

        if self.name in {
            "id",
            "url",
            "page_id",
            "worksheet_name",
        }:
            return False

        #
        # Only one value in the whole database
        #

        if self.unique_count <= 1:
            return False

        return True