from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QPushButton, QHBoxLayout)
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import QPointF


class Square2(QWidget):
    def __init__(self):
        super().__init__()
        self.color = QColor(255, 0, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Квадрат объектив - 2")
        self.setGeometry(100, 100, 500, 500)
        
        self.kv = 0.9
        self.nv = 10
        self.initial_square_coords = [
            QPointF(150.0, 150.0),
            QPointF(350.0, 150.0),
            QPointF(350.0, 350.0),
            QPointF(150.0, 350.0)
        ]

        self.layoutWidget = QWidget(self)
        self.inputlayout = QHBoxLayout(self.layoutWidget)
        self.draw = QPushButton("Рисовать", self)
        self.draw.clicked.connect(self.drawf)
        self.inputlayout.addWidget(self.draw)
        self.k = QLineEdit(str(self.kv), self)
        self.inputlayout.addWidget(self.k)
        self.n = QLineEdit(str(self.nv), self)
        self.inputlayout.addWidget(self.n)
        self.layoutWidget.setLayout(self.inputlayout)

    def calc(self, points):
        next_points = []
        for P_start, P_end in [
            (points[0], points[1]),
            (points[1], points[2]),
            (points[2], points[3]),
            (points[3], points[0])
        ]:
            next_points.append(QPointF(
                P_start.x() + (1 - self.kv) * (P_end.x() - P_start.x()),
                P_start.y() + (1 - self.kv) * (P_end.y() - P_start.y())))
        return next_points

    def drawf(self):
        self.kv, self.nv = float(self.k.text()), int(self.n.text())
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.color)
        points = self.initial_square_coords[:]
        for i in range(self.nv):
            painter.drawPolygon(QPolygonF(points))
            if i < self.nv - 1:
                points = self.calc(points)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exit(app.exec())