from PyQt6.QtWidgets import QInputDialog, QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from random import randrange


with open('test.py', 'r', encoding='utf-8') as f:
    print(f.read())


class RandomFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.base = [50, 30, 200, 30]
        self.color_count = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генерация флага")
        self.setFixedSize(300, 400)
        self.button = QPushButton("Ввести кол-во цветов флага", self)
        self.button.setFixedSize(self.button.sizeHint())
        self.button.move(self.width() // 2 - self.button.width() // 2, 0)
        self.button.clicked.connect(self.choice_count)

    def choice_count(self):
        color_count, ok = QInputDialog.getInt(
            self, "Выбор цвета", "Введите количество цветов:", 3, 1, 10, 1)
        if ok:
            self.color_count = color_count
            self.update()

    def paintEvent(self, event):
        ptr = QPainter(self)
        for i in range(self.color_count):
            ptr.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
            ptr.drawRect(self.base[0], self.base[1] + self.base[3] * i, self.base[2], self.base[3])


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec())