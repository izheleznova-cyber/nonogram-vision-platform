"""
checker.py

Rules controlling when a player is allowed
to check the puzzle.
"""

from __future__ import annotations

import time

from core.game.session import GameSession


def can_check(
    session: GameSession,
) -> tuple[bool, str]:
    """
    Check whether puzzle verification
    is currently allowed.
    """

    settings = session.settings

    #
    # Manual checking disabled.
    #

    if not settings.allow_manual_check:

        return (
            False,
            "Manual checking is disabled.",
        )

    #
    # Maximum number of checks.
    #

    if (
        settings.max_checks is not None
        and session.check_count >= settings.max_checks
    ):

        return (
            False,
            "Maximum number of checks exceeded.",
        )

    #
    # Delay between checks.
    #

    elapsed = time.time() - session.last_check_time

    if elapsed < settings.check_delay:

        remaining = settings.check_delay - elapsed

        return (
            False,
            f"Please wait {remaining:.1f} s",
        )

    return (
        True,
        "OK",
    )


def register_check(
    session: GameSession,
) -> None:
    """
    Register a successful check.
    """

    session.check_count += 1

    session.last_check_time = time.time()

def checks_left(
    session: GameSession,
) -> int | None:
    """
    Number of remaining checks.
    """

    if session.settings.max_checks is None:
        return None

    return max(
        0,
        session.settings.max_checks - session.check_count,
    )