import sys

from PySide6.QtWidgets import QApplication , QMainWindow , QLabel , QPushButton

app = QApplication(sys.argv)

windows = QMainWindow()

windows.setWindowTitle("Factor")
windows.resize(900,600)
label = QLabel("Factor Accounting System",windows)
label.move(50,50)
buttom = QPushButton("ثبت محصول", windows)
buttom.move(50,100)
def pushbuttom():
    print("کلیک شد")
buttom.clicked.connect(pushbuttom)
windows.show()
sys.exit(app.exec())