from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QTextBrowser, QLineEdit, QComboBox,
                             QWidget)
from PyQt6 import QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 510)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(5, 5, 550, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(5, 60, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_2 = QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(325, 60, 115, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(445, 60, 115, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(5, 105, 550, 400))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заголовки в цвете"))
        self.comboBox.setItemText(0, _translate("MainWindow", "p"))
        self.comboBox.setItemText(1, _translate("MainWindow", "h1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "h2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "h3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "h4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "h5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "h6"))
        self.lineEdit_2.setText(_translate("MainWindow", "#000"))
        self.pushButton.setText(_translate("MainWindow", "Вывести"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))


class HeadersInColor(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = ''
        self.setupUi(self)
        self.pushButton.clicked.connect(self.write_text)
        self.pushButton_2.clicked.connect(self.clear_text)

    def write_text(self):
        self.text = self.lineEdit.text()
        self.textBrowser.insertHtml(
            f'''<{self.comboBox.currentText()} style="color: {self.lineEdit_2.text()};">
{self.lineEdit.text()}</{self.comboBox.currentText()}><br>''')

    def clear_text(self):
        self.text = ''
        self.textBrowser.setText('')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = HeadersInColor()
    window.show()
    sys.exit(app.exec())