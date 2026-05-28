import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton


class Evaluator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 250, 30)
        self.setWindowTitle("Вычисление выражений")

        self.first_value = QLineEdit(self)
        self.first_value.resize(100, 30)
        self.first_value.move(0, 0)

        self.trick_button = QPushButton("->", self)
        self.trick_button.resize(50, 30)
        self.trick_button.move(100, 0)

        self.second_value = QLineEdit(self)
        self.second_value.resize(100, 30)
        self.second_value.move(150, 0)

        self.trick_button.clicked.connect(self.trick)

    def trick(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())