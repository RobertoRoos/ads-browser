from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QWidget


class ManageWidget(QWidget):
    """Second widget that holds filters, refresh rate, etc."""

    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)

        self.edit_filter = QLineEdit(placeholderText="Regex filter")
        main_layout.addWidget(self.edit_filter)

        self.button_refresh = QPushButton("Refresh All")
        main_layout.addWidget(self.button_refresh)
