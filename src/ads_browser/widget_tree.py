from collections.abc import Generator
from typing import Any, NamedTuple

from PySide6.QtWidgets import (
    QPushButton,
    QTreeWidget,
    QVBoxLayout,
    QWidget,
)

from ads_browser.widget_tree_item import TreeItemWidget


class Variable(NamedTuple):
    type: str
    value: str = "0"


EmptyVariable = Variable(type="", value="")


class TreeWidget(QWidget):
    """Main item - containing a big tree of all ADS variables."""

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(4)
        self.tree.setHeaderLabels(["Name", "Type", "Value", ""])
        main_layout.addWidget(self.tree)

        variables = {
            "GVL_Main": {
                "iNumber": Variable("INT"),
                "fValue": Variable("LREAL"),
                "sStruct": {
                    "field1": Variable("BOOL"),
                    "field2": Variable("BOOL"),
                },
            },
        }

        items = list(self.make_items(variables))

        self.tree.insertTopLevelItems(0, items)

        self.tree.setItemWidget(items[0], 3, QPushButton("Refresh"))

    @classmethod
    def make_items(
        cls, variables: dict[str, Any], parent: TreeItemWidget | None = None
    ) -> Generator[TreeItemWidget, None, None]:

        for key, value in variables.items():
            path = (parent.path + "." + key) if parent else key

            has_children = not isinstance(value, Variable)
            var = EmptyVariable if has_children else value

            new_widget = TreeItemWidget(
                name=key, path=path, typ=var.type, value=var.value
            )
            if parent:
                parent.addChild(new_widget)
            else:
                yield new_widget

            if has_children:
                yield from cls.make_items(value, parent=new_widget)
