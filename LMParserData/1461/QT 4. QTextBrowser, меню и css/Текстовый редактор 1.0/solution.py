from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QLineEdit, QPlainTextEdit)
from PyQt6 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 300)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 190, 130))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filename_edit = QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filename_edit.setFont(font)
        self.filename_edit.setObjectName("filename_edit")
        self.verticalLayout.addWidget(self.filename_edit)
        self.new_button = QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_button.setFont(font)
        self.new_button.setObjectName("new_button")
        self.verticalLayout.addWidget(self.new_button)
        self.save_button = QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.open_button = QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_button.setFont(font)
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        self.text_edit = QPlainTextEdit(parent=self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(210, 10, 270, 280))
        self.text_edit.setObjectName("text_edit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовый редактор"))
        self.new_button.setText(_translate("MainWindow", "Создать новый"))
        self.save_button.setText(_translate("MainWindow", "Сохранить файл"))
        self.open_button.setText(_translate("MainWindow", "Открыть файл"))


class Notebook(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_button.clicked.connect(self.new_file)
        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

    def new_file(self):
        self.text_edit.clear()
        self.filename_edit.clear()

    def save_file(self):
        filename = self.filename_edit.text().strip()
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
            except Exception:
                pass

    def open_file(self):
        filename = self.filename_edit.text().strip()
        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    self.text_edit.setPlainText(f.read())
            except Exception:
                pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Notebook()
    window.show()
    sys.exit(app.exec())