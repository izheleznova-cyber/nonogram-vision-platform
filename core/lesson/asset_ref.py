"""
Reference to an educational asset.

AssetRef links a Task with an Asset stored in the dataset.

The object contains only a reference to the resource and
never owns the resource itself.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AssetRef:
    """
    Reference to an educational resource.

    AssetRef does not contain the resource itself.
    It stores only the identifier of an Asset.
    """

    asset_id: str