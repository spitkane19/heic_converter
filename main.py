import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory

from ui import ui_window


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Heic Converter")
        self.ui = ui_window()
        self.ui.show()


if __name__ == "__main__":
    app = QApplication()
    app.setStyle(QStyleFactory.create("Fusion"))
    widget = MainWindow()
    sys.exit(app.exec())
