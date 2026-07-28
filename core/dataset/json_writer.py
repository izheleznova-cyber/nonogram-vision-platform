from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from core.dataset.passport_record import PassportRecord


def save_passport(
    passport: PassportRecord,
    output_dir: Path,
) -> Path:

    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / f"{passport.id}.json"

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            asdict(passport),
            file,
            ensure_ascii=False,
            indent=4,
        )

    return path