import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLineEdit,
    QPushButton,
    QLabel,
    QLCDNumber,
)


class MiniCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 350, 130)
        self.setWindowTitle("Вычисление выражений")

        number1_label = QLabel("Первое число:", self)
        number1_label.move(0, 0)

        self.number_1 = QLineEdit(self)
        self.number_1.resize(100, 30)
        self.number_1.move(0, 25)

        self.calculate_button = QPushButton("->", self)
        self.calculate_button.resize(50, 30)
        self.calculate_button.move(100, 57)

        number2_label = QLabel("Второе число:", self)
        number2_label.move(0, 60)

        self.number_2 = QLineEdit(self)
        self.number_2.resize(100, 30)
        self.number_2.move(0, 85)

        result_sum_label = QLabel("Сумма:", self)
        result_sum_label.move(180, 0)
        self.result_sum = QLCDNumber(self)
        self.result_sum.move(180 + result_sum_label.sizeHint().width(), 0)

        result_sub_label = QLabel("Разность:", self)
        result_sub_label.move(180, 30)
        self.result_sub = QLCDNumber(self)
        self.result_sub.move(180 + result_sub_label.sizeHint().width(), 30)

        result_mul_label = QLabel("Умножение:", self)
        result_mul_label.move(180, 60)
        self.result_mul = QLCDNumber(self)
        self.result_mul.move(180 + result_mul_label.sizeHint().width(), 60)

        result_div_label = QLabel("Разность:", self)
        result_div_label.move(180, 90)
        self.result_div = QLCDNumber(self)
        self.result_div.move(180 + result_div_label.sizeHint().width(), 90)

        self.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        try:
            csum = int(self.number_1.text()) + int(self.number_2.text())
        except Exception:
            csum = "Error"
        self.result_sum.display(csum)

        try:
            csub = int(self.number_1.text()) - int(self.number_2.text())
        except Exception:
            csub = "Error"
        self.result_sub.display(csub)

        try:
            cmul = int(self.number_1.text()) * int(self.number_2.text())
        except Exception:
            cmul = "Error"
        self.result_mul.display(cmul)

        try:
            cdiv = round(int(self.number_1.text()) / int(self.number_2.text()), 3)
        except Exception:
            cdiv = "Error"
        self.result_div.display(cdiv)