"""
Educational asset.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Asset:
    """
    Educational resource.

    Asset exists independently of lessons and can be used
    by multiple tasks.
    """

    id: str
    type: str
    passport: str 