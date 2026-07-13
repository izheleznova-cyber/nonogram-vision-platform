from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LessonSettings:

    auto_check: bool = False

    check_delay: int = 10

    allow_manual_check: bool = True

    max_checks: int | None = None

    reveal_completed_rows: bool = True

    reveal_completed_columns: bool = True

    reveal_wrong_cells: bool = False

    allow_prediction: bool = True

    prediction_history: bool = True
