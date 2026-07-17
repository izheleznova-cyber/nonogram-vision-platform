from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class LessonSettings:
    """
    Lesson rules.
    """

    #
    # Training check
    #

    auto_check: bool = False

    allow_manual_check: bool = True

    check_delay: float = 10.0

    max_error_ratio: float = 0.20

    #
    # Hints
    #

    reveal_completed_rows: bool = True

    reveal_completed_columns: bool = True

    reveal_wrong_cells: bool = False

    #
    # Predictions
    #

    allow_prediction: bool = True

    prediction_history: bool = True