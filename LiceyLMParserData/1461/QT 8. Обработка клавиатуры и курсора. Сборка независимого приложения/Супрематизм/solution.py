import sys
import random

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QPointF, QRectF
from PyQt6.QtGui import QPolygonF


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.clicked_button, self.click_pos = None, [0, 0]

    def initUI(self):
        self.setFixedSize(1000, 1000)
        self.setWindowTitle('Супрематизм')
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.m_pos = (event.pos().x(), event.pos().y())

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked_button = "m_left"
        elif event.button() == Qt.MouseButton.RightButton:
            self.clicked_button = "m_right"
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space and not event.isAutoRepeat():
            self.clicked_button = "space"
            self.update()

    def paintEvent(self, event):
        if self.clicked_button:
            painter = QPainter(self)
            rad = random.randint(20, 101)
            painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            painter.setPen(QPen(QColor(0, 0, 0)))
            if self.clicked_button == "m_right":
                painter.drawRect(QRectF(int(self.m_pos[0] - rad / 2), int(self.m_pos[1] - rad / 2), rad, rad))
            elif self.clicked_button == "m_left":
                painter.drawEllipse(self.m_pos[0] - rad, self.m_pos[1] - rad, rad * 2, rad * 2)
            elif self.clicked_button == "space":
                n = rad * 3 ** 0.5 / 2
                painter.drawPolygon(QPolygonF([
                    QPointF(self.m_pos[0] - n, self.m_pos[1] + rad / 2),
                    QPointF(self.m_pos[0] + n, self.m_pos[1] + rad / 2),
                    QPointF(self.m_pos[0], self.m_pos[1] - rad)]))
            self.clicked_button = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())