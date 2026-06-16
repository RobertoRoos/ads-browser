from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from ads_browser.widget_connect import ConnectWidget
from ads_browser.widget_manage import ManageWidget
from ads_browser.widget_tree import TreeWidget


class AdsBrowser(QMainWindow):
    """Main application class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        self.widget_connect = ConnectWidget()
        main_layout.addWidget(self.widget_connect)

        self.widget_manage = ManageWidget()
        main_layout.addWidget(self.widget_manage)

        self.widget_tree = TreeWidget()
        main_layout.addWidget(self.widget_tree)
