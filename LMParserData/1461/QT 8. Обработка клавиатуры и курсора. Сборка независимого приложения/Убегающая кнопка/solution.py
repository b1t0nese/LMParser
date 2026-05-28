from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import Qt
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle('Убегающая кнопка')
        self.button = QPushButton("Нажми на меня", self)
        self.button.setFixedSize(100, 40)
        self.button.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.button.move(
            (self.width() - self.button.width()) // 2,
            (self.height() - self.button.height()) // 2)

    def mouseMoveEvent(self, event):
        mx, my = event.pos().x(), event.pos().y()
        bx, by = self.button.x(), self.button.y()
        bw, bh = self.button.width(), self.button.height()

        if bx <= mx <= bx + bw and by <= my <= by + bh:
            self.button.move(randint(0, self.width() - bw),
                             randint(0, self.height() - bh))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())