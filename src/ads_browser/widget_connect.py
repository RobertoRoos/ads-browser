from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget


class ConnectWidget(QWidget):
    """Widget at the top to manage the ADS connection."""

    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout(self)

        main_layout.addWidget(QLabel("Host:"))
        self.edit_host = QLineEdit(placeholderText="127.0.0.1")
        main_layout.addWidget(self.edit_host)

        main_layout.addWidget(QLabel("AMS ID:"))
        self.edit_ams_id = QLineEdit(placeholderText="127.0.0.1.1.1")
        main_layout.addWidget(self.edit_ams_id)

        main_layout.addWidget(QLabel("AMS Port:"))
        self.edit_ams_port = QLineEdit(placeholderText="851")
        main_layout.addWidget(self.edit_ams_port)

        main_layout.addWidget(QPushButton("Connect"))
