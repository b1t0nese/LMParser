from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox
import sys


class WidgetsHideNSeek(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 180, 130)
        self.setWindowTitle("Прятки для виджетов")

        self.checkbox1 = QCheckBox("edit1", self)
        self.checkbox1.move(0, 0)
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(self.show_checkbox)
        self.edit1 = QLineEdit("Поле edit1", self)
        self.edit1.move(self.checkbox1.sizeHint().width(), 0)
        self.checkbox1.link_to_edit = self.edit1

        self.checkbox2 = QCheckBox("edit2", self)
        self.checkbox2.move(0, 30)
        self.checkbox2.setChecked(True)
        self.checkbox2.stateChanged.connect(self.show_checkbox)
        self.edit2 = QLineEdit("Поле edit2", self)
        self.edit2.move(self.checkbox2.sizeHint().width(), 30)
        self.checkbox2.link_to_edit = self.edit2

        self.checkbox3 = QCheckBox("edit3", self)
        self.checkbox3.move(0, 60)
        self.checkbox3.setChecked(True)
        self.checkbox3.stateChanged.connect(self.show_checkbox)
        self.edit3 = QLineEdit("Поле edit3", self)
        self.edit3.move(self.checkbox3.sizeHint().width(), 60)
        self.checkbox3.link_to_edit = self.edit3

        self.checkbox4 = QCheckBox("edit4", self)
        self.checkbox4.move(0, 90)
        self.checkbox4.setChecked(True)
        self.checkbox4.stateChanged.connect(self.show_checkbox)
        self.edit4 = QLineEdit("Поле edit4", self)
        self.edit4.move(self.checkbox4.sizeHint().width(), 90)
        self.checkbox4.link_to_edit = self.edit4

    def show_checkbox(self):
        self.sender().link_to_edit.setVisible(self.sender().isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())