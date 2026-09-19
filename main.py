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
    try:
            
        product = {
            "code": code_input.text(),
            "name": name_input.text(),
            "price": price_input.text(),
            "stock": stock_input.text()
        }
    except ValueError:
        print("باید عدد وارد کنید")
    if name_input.text() == "":
        print("is not none define")
    else:
            for i in product.values():
                print(i)
        
button.clicked.connect(push_button)    
windows.show()
sys.exit(app.exec())