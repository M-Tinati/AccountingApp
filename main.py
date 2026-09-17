import sys

from PySide6.QtWidgets import QApplication , QMainWindow

app = QApplication(sys.argv)

windows = QMainWindow()

windows.setWindowTitle("Factor")
windows.resize(900,600)
windows.show()
sys.exit(app.exec())