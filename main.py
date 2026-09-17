import sys

from PySide6.QtWidgets import QApplication , QMainWindow , QLabel , QPushButton , QLineEdit

app = QApplication(sys.argv)

windows = QMainWindow()

windows.setWindowTitle("Factor")
windows.resize(900,600)
label = QLabel("Factor Accounting System",windows)
label.move(50,50)
buttom = QPushButton("ثبت محصول", windows)
buttom.move(50,100)
InputUser = QLineEdit(windows)

InputUser.move(200,50)
def pushbuttom():
    if InputUser.text() == "":
        print("is not none define")
    else:
        print(InputUser.text())
buttom.clicked.connect(pushbuttom)    
windows.show()
sys.exit(app.exec())