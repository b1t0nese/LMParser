import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLCDNumber, QPushButton)


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.new_game()

    def initUI(self):
        self.setWindowTitle('Ним наносит ответный удар')
        self.setFixedSize(300, 200)
        layout = QVBoxLayout()

        self.moves_lcd = QLCDNumber()
        layout.addWidget(self.moves_lcd)
        self.now_number_lcd = QLCDNumber()
        layout.addWidget(self.now_number_lcd)
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.btnp = QPushButton('Увеличить')
        self.btnp.clicked.connect(self.change)
        layout.addWidget(self.btnp)
        self.btnm = QPushButton('Уменьшить')
        self.btnm.clicked.connect(self.change)
        layout.addWidget(self.btnm)
        
        self.setLayout(layout)

    def new_game(self):
        self.X, self.Y, self.Z = [random.randint(1, 10) for i in range(3)]
        self.moves = 10
        self.result_label.clear()
        self.update_lcd()
        self.btnp.setText(str(self.Y))
        self.btnm.setText(f"-{self.Z}")

    def update_lcd(self):
        self.moves_lcd.display(self.moves)
        self.now_number_lcd.display(self.X)

    def change(self):
        if self.X == 0 or self.moves <= 0:
            self.new_game()
        self.X += int(self.sender().text())
        self.moves -= 1
        self.check()

    def check(self):
        self.update_lcd()
        if not self.X:
            self.result_label.setText('Вы победили, начинаем новую игру')
        if self.moves <= 0:
            self.result_label.setText('Вы проиграли, начинаем новую игру')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = NimStrikesBack()
    window.show()
    sys.exit(app.exec())