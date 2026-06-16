import sys

from PySide6.QtWidgets import QApplication

from ads_browser.browser import AdsBrowser


def main():
    qapp = QApplication(sys.argv)

    browser_app = AdsBrowser()
    browser_app.show()

    sys.exit(qapp.exec())


if __name__ == "__main__":
    main()
