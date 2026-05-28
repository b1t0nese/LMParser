from PyQt6.QtWidgets import (QApplication, QMainWindow, QSlider)
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QPoint


class GoodMoodRising(QMainWindow):
    def __init__(self):
        super().__init__()
        self.color = QColor(255, 255, 255)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Рост хорошего настроения")
        self.resize(1000, 1000)

        self.slider = QSlider(Qt.Orientation.Vertical, self)
        self.slider.setGeometry(970, 40, 20, 500)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider_value = 50

        self.slider.valueChanged.connect(self.change_size)

    def change_size(self, size):
        self.slider_value = size
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(Qt.GlobalColor.transparent)
        painter.setPen(self.color)
        r_value = 2 * self.slider_value
        painter.drawEllipse(0, 0, r_value * 5, r_value * 5)
        painter.drawEllipse(*[r_value for i in range(4)])
        painter.drawEllipse(r_value * 5 - r_value * 2, r_value, r_value, r_value)
        painter.drawArc(r_value, r_value * 3, r_value * 3, r_value, -480, -1920)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec())