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
layout.addRow(table)

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
    
    

    table.setColumnCount(4)
    table.setRowCount(len(products))
    table.setHorizontalHeaderLabels([
        "کد",
        "نام محصول",
        "قیمت",
        "موجودی"
    ])
    for index, product in enumerate(products):
        table.setItem(index,0,QTableWidgetItem(product["code"]))
        table.setItem(index,1,QTableWidgetItem(product["name"]))
        table.setItem(index,2,QTableWidgetItem(str(product["price"])))
        table.setItem(index,3,QTableWidgetItem(str(product["stock"])))
button.clicked.connect(push_button)







    
windows.show()
sys.exit(app.exec())