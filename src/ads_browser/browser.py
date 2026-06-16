from PySide6.QtWidgets import QLabel, QMainWindow


class AdsBrowser(QMainWindow):
    """Main application class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = QLabel("Welcome!")
        self.setCentralWidget(label)
