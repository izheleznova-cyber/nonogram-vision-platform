from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True)
class Action:

    timestamp: float

    action: str

    row: int

    column: int
