"""
Build reference datasets.
"""

from __future__ import annotations

from core.dataset.passport_record import PassportRecord


REFERENCE_SIZES = [

    # square
    (5, 5),
    (10, 10),
    (20, 20),
    (35, 35),

    # portrait
    (15, 30),
    (20, 45),
    (25, 40),

    # landscape
    (32, 17),
    (40, 20),

    # large
    (45, 40),
]


def build_reference_dataset(
    passports: list[PassportRecord],
) -> list[PassportRecord]:
    """
    Select reference puzzles of different geometry.
    """

    dataset: list[PassportRecord] = []

    for width, height in REFERENCE_SIZES:

        passport = next(
            (
                p
                for p in passports
                if p.width == width
                and p.height == height
            ),
            None,
        )

        if passport is not None:
            dataset.append(passport)

    return dataset