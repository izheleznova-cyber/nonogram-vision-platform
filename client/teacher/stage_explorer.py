"""
Stage explorer widget.
"""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
)

from core.lesson.stage import Stage


class StageExplorer(QTreeWidget):
    """
    Displays lesson stages.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setHeaderLabel("Stages")

    def set_stages(
        self,
        stages: list[Stage],
    ) -> None:
        """
        Populate the tree.
        """

        self.clear()

        for stage in stages:
            self.addTopLevelItem(
                QTreeWidgetItem(
                    [f"Stage {stage.number}"]
                )
            )

        if self.topLevelItemCount():
            self.setCurrentItem(
                self.topLevelItem(0)
            )
