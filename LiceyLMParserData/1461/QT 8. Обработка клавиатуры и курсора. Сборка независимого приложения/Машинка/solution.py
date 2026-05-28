from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class Car(QWidget):
    def __init__(self):
        super().__init__()
        self.current_car, self.car_images = 1, ['car1.png', 'car2.png', 'car3.png']
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setWindowTitle('Машинка')
        self.lbl = QLabel(self)
        self.pixmap = QPixmap(self.car_images[0])
        self.lbl.setPixmap(self.pixmap)
        self.lbl.resize(self.pixmap.width(), self.pixmap.height())
        self.lbl.move(0, 0)
        self.setMouseTracking(True)
        self.lbl.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.lbl.move(
            max(0, min(min(250, event.pos().x()), self.width() - self.lbl.width())),
            max(0, min(min(250, event.pos().y()), self.height() - self.lbl.height())))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.current_car = (self.current_car % 3) + 1
            self.pixmap = QPixmap(self.car_images[self.current_car - 1])
            self.lbl.setPixmap(self.pixmap)
            self.lbl.resize(self.pixmap.width(), self.pixmap.height())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())