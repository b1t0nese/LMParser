import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


class Arifmometr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 200, 80)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()

        self.first_value = QLineEdit("0", self)
        layout.addWidget(self.first_value)

        self.add_button = QPushButton("+", self)
        self.add_button.clicked.connect(self.arifmetic)
        layout.addWidget(self.add_button)
        self.substract_button = QPushButton("-", self)
        self.substract_button.clicked.connect(self.arifmetic)
        layout.addWidget(self.substract_button)
        self.multiply_button = QPushButton("*", self)
        self.multiply_button.clicked.connect(self.arifmetic)
        layout.addWidget(self.multiply_button)

        self.second_value = QLineEdit("0", self)
        layout.addWidget(self.second_value)

        layout.addWidget(QLabel("=", self))
        self.result = QLineEdit("0", self)
        self.result.setEnabled(False)
        layout.addWidget(self.result)

        central_widget.setLayout(layout)

    def arifmetic(self):
        first = self.first_value.text() or "0"
        second = self.second_value.text() or "0"
        self.result.setText(str(eval(f"{first}{self.sender().text()}{second}")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())