import sys

from PySide6.QtWidgets import QApplication , QMainWindow , QLabel , QPushButton , QLineEdit

app = QApplication(sys.argv)

windows = QMainWindow()

windows.setWindowTitle("Factor")
windows.resize(900,600)
label = QLabel("Factor Accounting System",windows)
label.move(50,50)

label_name = QLabel("کد محصول",windows)
label_name.move(50,150)
code_input = QLineEdit(windows)
code_input.move(150,150)
label_name = QLabel("نام محصول",windows)
label_name.move(50,180)
name_input = QLineEdit(windows)
name_input.move(150,180)
label_name = QLabel("قیمت محصول",windows)
label_name.move(50,210)
price_input = QLineEdit(windows)
price_input.move(150,210)
label_name = QLabel("مقدار محصول",windows)
label_name.move(50,240)
stock_input = QLineEdit(windows)
stock_input.move(150,240)
button = QPushButton("ثبت محصول", windows)
button.move(150,270)
input_user = QLineEdit(windows)

input_user.move(200,50)
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

