import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCheckBox,
    QPushButton,
    QPlainTextEdit,
)


class MacOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.products = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]
        self.padding = 30
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 300, 600)
        self.setWindowTitle("Заказ в Макдональдсе")

        self.menu_checkboxes = []
        for i, pr in enumerate(self.products):
            new_check_button = QCheckBox(pr, self)
            new_check_button.move(0, i * self.padding)
            self.menu_checkboxes.append(new_check_button)

        self.order_btn = QPushButton("Заказать", self)
        self.order_btn.move(0, (len(self.products) + 1) * self.padding)
        self.order_btn.clicked.connect(self.order)

        self.result = QPlainTextEdit(self)
        self.result.resize(
            self.width(), (self.height() - (len(self.products) + 2) * self.padding)
        )
        self.result.move(0, (len(self.products) + 2) * self.padding)
        self.result.setEnabled(False)

    def order(self):
        result_text = "Ваш заказ:\n\n"
        for checkbox in self.menu_checkboxes:
            if checkbox.isChecked():
                result_text += checkbox.text() + "\n"
        self.result.setPlainText(result_text.strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())