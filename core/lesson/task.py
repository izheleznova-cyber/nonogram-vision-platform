"""
Lesson task.
"""

from __future__ import annotations

from dataclasses import dataclass

from .answer_spec import AnswerSpec
from .asset_ref import AssetRef


@dataclass(slots=True)
class Task:
    """
    One learning task within a lesson stage.
    """

    id: str
    title: str
    asset_ref: AssetRef
    answer_spec: AnswerSpec
