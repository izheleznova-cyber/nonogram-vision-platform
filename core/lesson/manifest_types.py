"""
Typed lesson manifest.
"""

from __future__ import annotations

from typing import TypedDict


class ManifestAssetRef(TypedDict):
    asset_id: str


class ManifestAnswerSpec(TypedDict):
    type: str


class ManifestTask(TypedDict):
    id: str
    title: str
    asset_ref: ManifestAssetRef
    answer_spec: ManifestAnswerSpec


class ManifestStage(TypedDict):
    number: int
    tasks: list[ManifestTask]


class Manifest(TypedDict):
    name: str
    title: str
    max_width: int
    max_height: int
    stages: list[ManifestStage]
