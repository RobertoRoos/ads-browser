from collections.abc import Generator
from typing import Any

from PySide6.QtWidgets import (
    QTreeWidget,
    QVBoxLayout,
    QWidget,
)

from ads_browser.widget_tree_item import TreeItemWidget


class TreeWidget(QWidget):
    """Main item - containing a big tree of all ADS variables."""

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(["Name"])
        main_layout.addWidget(self.tree)

        variables = {
            "GVL_Main": {
                "iNumber": None,
                "fValue": None,
                "sStruct": {
                    "field1": None,
                    "field2": None,
                },
            },
        }

        # items = [
        #     TreeItemWidget(["GVL_Main"]),
        #     TreeItemWidget(["GVL_Main.iNumber"]),
        #     TreeItemWidget(["GVL_Main.fValue"]),
        #     TreeItemWidget(["GVL_Main.sStruct"]),
        #     TreeItemWidget(["GVL_Main.sStruct.field1"]),
        #     TreeItemWidget(["GVL_Main.sStruct.field2"]),
        # ]

        items = list(self.make_items(variables))

        self.tree.insertTopLevelItems(0, items)

    @classmethod
    def make_items(
        cls, variables: dict[str, Any], parent: TreeItemWidget | None = None
    ) -> Generator[TreeItemWidget, None, None]:

        for key, value in variables.items():
            path = (parent.path + "." + key) if parent else key
            new_widget = TreeItemWidget(name=key, path=path)
            if parent:
                parent.addChild(new_widget)
            else:
                yield new_widget

            if value is not None:
                yield from cls.make_items(value, parent=new_widget)
