from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLineEdit, QHBoxLayout)
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtCore import Qt, QRectF


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.color = QColor(255, 0, 0)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Квадрат-объектив — 1")
        self.setGeometry(0, 0, 800, 900)
        layout = QHBoxLayout(self)
        self.btn = QPushButton('Показать')
        self.btn.clicked.connect(self.update)
        layout.addWidget(self.btn)
        self.lineEdit = QLineEdit('300')
        layout.addWidget(self.lineEdit)
        self.lineEdit_2 = QLineEdit('0.9')
        layout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QLineEdit('10')
        layout.addWidget(self.lineEdit_3)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.move(0, 0)
        self.layoutWidget.setLayout(layout)

    def paintEvent(self, event):
        pen = QPen()
        pen.setColor(self.color) 
        pen.setWidth(1)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter = QPainter(self)
        painter.setPen(pen)
        x, y = 50.0, 130.0
        wh = int(self.lineEdit.text())
        for i in range(int(self.lineEdit_3.text())):
            rect = QRectF(x, y, wh, wh)
            painter.drawRect(rect)
            wh *= float(self.lineEdit_2.text())
            x = 50 + (float(self.lineEdit.text()) - wh) / 2
            y = 130 + (float(self.lineEdit.text()) - wh) / 2


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exit(app.exec())