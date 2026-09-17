import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QWidget,
    QFormLayout
)

app = QApplication(sys.argv)

windows = QMainWindow()
central_widget = QWidget()
windows.setCentralWidget(central_widget)

layout = QFormLayout()
central_widget.setLayout(layout)

windows.setWindowTitle("Factor")
windows.resize(900,600)

code_input = QLineEdit()
layout.addRow("کد محصول", code_input)
name_input = QLineEdit()
layout.addRow("نام محصول", name_input)
price_input = QLineEdit()
layout.addRow("قیمت محصول", price_input)
stock_input = QLineEdit()
layout.addRow("مقدار محصول", stock_input)
button = QPushButton("ثبت محصول")
layout.addRow(button)

def push_button():
    if name_input.text() == "":
        print("is not none define")
    else:
        print(code_input.text())
        print(name_input.text())
        print(price_input.text())
        print(stock_input.text())
button.clicked.connect(push_button)    
windows.show()
sys.exit(app.exec())