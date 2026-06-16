from PySide6.QtWidgets import (
    QTreeWidgetItem,
)


class TreeItemWidget(QTreeWidgetItem):
    """Widget for a single item (row) in the variables tree."""

    def __init__(self, name: str, path: str, typ: str, value: str, **kwargs):
        self.name = name
        self.path = path
        self.type = typ
        self.value = value

        super().__init__([name, typ, value], **kwargs)
