from PySide6.QtWidgets import (
    QTreeWidgetItem,
)


class TreeItemWidget(QTreeWidgetItem):
    """Widget for a single item (row) in the variables tree."""

    def __init__(self, name: str, path: str, **kwargs):
        self.name = name
        self.path = path

        super().__init__([name], **kwargs)
