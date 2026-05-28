from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QCheckBox,
    QPushButton, QPlainTextEdit, QLineEdit)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.products = {
            "Чизбургер": 10,
            "Гамбургер": 20,
            "Кока-кола": 15,
            "Наггетсы": 30
        }
        self.padding = 30
        self.checkboxes = []
        self.inputs = []
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 300, 400)
        self.setWindowTitle("Заказ в Макдональдсе")

        for i, pr in enumerate(self.products.keys()):
            new_check_button = QCheckBox(pr, self)
            new_check_button.move(0, i * self.padding)
            new_product_count_edit = QLineEdit("0", self)
            new_product_count_edit.move(new_check_button.sizeHint().width() + 10, i * self.padding)
            new_check_button.product_count_edit = new_product_count_edit
            new_check_button.stateChanged.connect(self.check_product)
            self.check_product(False, new_check_button)
            self.checkboxes.append(new_check_button)
            self.inputs.append(new_product_count_edit)

        self.orderButton = QPushButton("Заказать", self)
        self.orderButton.move(0, (len(self.products) + 1) * self.padding)
        self.orderButton.clicked.connect(self.order_func)

        self.order = QPlainTextEdit(self)
        self.order.resize(self.width(), (self.height() - (len(self.products) + 2) * self.padding))
        self.order.move(0, (len(self.products) + 2) * self.padding)
        self.order.setEnabled(False)

    def check_product(self, check=None, checkbox=None):
        if not checkbox:
            checkbox = self.sender()
        if check is None:
            check = checkbox.isChecked()
        else:
            checkbox.setChecked(check)
        if not check:
            checkbox.product_count_edit.setText("0")
            checkbox.product_count_edit.setEnabled(False)
        else:
            checkbox.product_count_edit.setText("1")
            checkbox.product_count_edit.setEnabled(True)

    def order_func(self):
        full_price = 0
        result_text = "Ваш заказ\n\n"
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                product_count = int(checkbox.product_count_edit.text())
                price = self.products[checkbox.text()] * product_count
                full_price += price
                result_text += f"{checkbox.text()}-----{product_count}-----{price}\n"
        result_text += f"\nИтого: {full_price}"
        self.order.setPlainText(result_text.strip())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())