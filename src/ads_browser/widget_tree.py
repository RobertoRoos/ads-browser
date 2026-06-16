from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class TreeWidget(QWidget):
    """Main item - containing a big tree of all ADS variables."""

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        self.tree = QTreeWidget(columnCount=1)
        main_layout.addWidget(self.tree)

        self.tree.insertTopLevelItem(
            0,
            QTreeWidgetItem(["Item"]),
        )
