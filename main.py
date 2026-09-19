import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QWidget,
    QFormLayout,
    QTableWidget,
    QTableWidgetItem,
)

app = QApplication(sys.argv)

windows = QMainWindow()
central_widget = QWidget()
table = QTableWidget()
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

products = []
def ClearInput():
        code_input.clear()
        name_input.clear()
        price_input.clear()
        stock_input.clear()
def push_button():
    try:
        code = str(code_input.text())
        name = str(name_input.text())
        price = int(price_input.text())
        stock = int(stock_input.text())
    except ValueError:
        print("باید عدد وارد کنید")    
        return
    product = {
        "code": code,
        "name": name,
        "price": price,
        "stock": stock
    }
    if name == "":
            print("نام محصول را وارد کنید")
            return
        
    
    products.append(product)
    
    
    ClearInput()
    
    for product in products:
        print(product)
button.clicked.connect(push_button)

layout.addRow(table)
table.setRowCount(3)
table.setColumnCount(4)

table.setHorizontalHeaderLabels([
    "کد",
    "نام محصول",
    "قیمت",
    "موجودی"
])
table.setItem(0,0,QTableWidgetItem("110"))
table.setItem(0,1,QTableWidgetItem("pipe 110"))
table.setItem(0,2,QTableWidgetItem("100000"))
table.setItem(0,3,QTableWidgetItem("1"))





    
windows.show()
sys.exit(app.exec())