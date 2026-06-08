import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QDialog, QSpinBox, QPushButton)
from PyQt6.QtGui import QPainter, QColor, QPen
from random import randint as r


class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("eqq")
        self.setFixedSize(300, 300)

        self.edit_spin_box = QSpinBox(self)
        self.edit_spin_box.setValue(3)
        
        self.accept_button = QPushButton("Ок", self)
        self.accept_button.move(0, 100)
        self.accept_button.clicked.connect(self.accept_f)
        self.reject_button = QPushButton("Закрыть", self)
        self.reject_button.move(0, 200)
        self.reject_button.clicked.connect(self.reject_f)
        
    def get_value(self):
        self.exec()
        return self.edit_spin_box.value()
    
    def accept_f(self):
        self.accept()
    
    def reject_f(self):
        self.reject()

    
class RandomFlag(QWidget):
    def __init__(self):
        super().__init__()
        self.base = [50, 50, 100, 30]
        self.num_of_colors = 0
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("eq")
        self.setFixedSize(300, 400)

        self.button = QPushButton("Настройка", self)
        self.button.clicked.connect(self.settings)

    def settings(self):
        dialog_window = DialogWindow()
        self.num_of_colors = dialog_window.get_value()
        
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for i in range(0, self.num_of_colors):
            painter.setBrush(QColor(r(0, 255), r(0, 255), r(0, 255)))
            painter.setPen(QPen(QColor(0, 0, 0)))
            
            painter.drawRect(*[self.base[0], self.base[1] + i * 30, self.base[2], self.base[3]])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec())
