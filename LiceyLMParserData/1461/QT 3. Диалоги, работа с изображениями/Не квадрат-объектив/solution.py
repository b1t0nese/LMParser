from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QLineEdit, QPushButton, QColorDialog)
from PyQt6.QtGui import QPolygonF, QColor, QPainter
from PyQt6.QtCore import QPointF
import math


class NoTSquare(QMainWindow):
    def __init__(self):
        super().__init__()
        self.knm = (0.9, 6, 10)
        self.center, self.rad = (250, 250), 100
        self.start_point = [350, 250]
        self.points, self.color = [], QColor(255, 0, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Не квадрат-объектив")
        self.setFixedSize(500, 500)

        container = QWidget(self)
        container.setGeometry(50, 10, 450, 25)
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)

        self.k = QLineEdit(str(self.knm[0]))
        self.n = QLineEdit(str(self.knm[1]))
        self.m = QLineEdit(str(self.knm[2]))
        self.draw = QPushButton("Рисовать")
        self.draw.clicked.connect(self.choose_color)

        self.k.setFixedSize(80, 25)
        self.n.setFixedSize(80, 25)
        self.m.setFixedSize(80, 25)
        self.draw.setFixedSize(100, 25)

        layout.addWidget(self.k)
        layout.addWidget(self.n)
        layout.addWidget(self.m)
        layout.addWidget(self.draw)
        
    def create_initial_polygon(self):
        self.points = []
        for i in range(self.knm[1]):
            angle = i * (2 * math.pi / self.knm[1]) + (math.pi / 2)
            x = self.center[0] + self.rad * math.sin(angle)
            y = self.center[1] - self.rad * math.cos(angle)
            self.points.append(QPointF(x, y))

    def choose_color(self):
        new_color = QColorDialog().getColor()
        if new_color.isValid():
            self.color = new_color
        self.knm = (float(self.k.text()), int(self.n.text()), int(self.m.text()))
        self.create_initial_polygon()

    def calc(self, cur_points):
        next_points = []
        for i in range(len(cur_points)):
            start, end = cur_points[i], cur_points[(i + 1) % len(cur_points)]
            next_points.append(QPointF(start.x() + (1 - self.knm[0]) * (end.x() - start.x()),
                                       start.y() + (1 - self.knm[0]) * (end.y() - start.y())))
        return next_points        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.color)
        cur_points = self.points[:]
        for i in range(self.knm[2]):
            pol = QPolygonF()
            for pnt in cur_points:
                pol.append(pnt)
            painter.drawPolygon(pol)
            if i <= self.knm[2]:
                cur_points = self.calc(cur_points)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = NoTSquare()
    window.show()
    sys.exit(app.exec())