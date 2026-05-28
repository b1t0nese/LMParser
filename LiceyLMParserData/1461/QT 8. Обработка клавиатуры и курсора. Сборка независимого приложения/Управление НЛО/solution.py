from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class UfoControl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setFixedSize(300, 300)
        self.setWindowTitle('Управление НЛО')
        self.ufo = QLabel(self)
        self.pixmap = QPixmap('ufo.png')
        self.ufo.setPixmap(self.pixmap)
        self.ufo.resize(self.pixmap.width(), self.pixmap.height())
        self.ufo.move(0, 0)
        
    def keyPressEvent(self, event):
        step = 10
        xstep, ystep = 0, 0
        if event.key() == Qt.Key.Key_Left:
            xstep = -step
        elif event.key() == Qt.Key.Key_Right:
            xstep = step
        elif event.key() == Qt.Key.Key_Up:
            ystep = -step
        elif event.key() == Qt.Key.Key_Down:
            ystep = step
        x, y = self.ufo.x(), self.ufo.y()
        self.ufo.move(x + xstep, y + ystep)
        x, y = self.ufo.x(), self.ufo.y()
        if x < 0:
            self.ufo.move(250, y)
        elif x > 250:
            self.ufo.move(0, y)
        elif y > 250:
            self.ufo.move(x, 0)
        elif y < 0:
            self.ufo.move(x, 250)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = UfoControl()
    ex.show()
    sys.exit(app.exec())