import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton


class WordTrick(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 250, 30)
        self.setWindowTitle("Фокус со словами")

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
        act = self.trick_button.text()
        if act == "->":
            self.second_value.setText(self.first_value.text())
            self.first_value.setText("")
            self.trick_button.setText("<-")
        if act == "<-":
            self.first_value.setText(self.second_value.text())
            self.second_value.setText("")
            self.trick_button.setText("->")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())