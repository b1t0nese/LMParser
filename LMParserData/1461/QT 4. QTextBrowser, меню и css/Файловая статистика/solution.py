from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QStatusBar,
                             QTextBrowser, QLineEdit, QWidget, QHBoxLayout)
from PyQt6 import QtCore, QtGui


def etdigit(strdig):
    try:
        return int(strdig)
    except Exception:
        return False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 280)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 50, 540, 210))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutWidget = QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 540, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.filenameEdit = QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.filenameEdit.setFont(font)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout.addWidget(self.filenameEdit)
        self.button = QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.horizontalLayout.addWidget(self.button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Файловая статистика"))
        self.label.setText(_translate("MainWindow", "Имя файла:"))
        self.button.setText(_translate("MainWindow", "Рассчитать"))


class FileStat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.min_med_max)

    def show_error(self, err_text):
        self.statusbar.showMessage(err_text)
        self.statusBar().showMessage(err_text)
        self.textBrowser.clear()

    def min_med_max(self):
        try:
            with open(self.filenameEdit.text(), "r", encoding="utf-8") as f:
                file_text = f.read().strip()
            if file_text:
                CHISLA = []
                for line in file_text.split():
                    for word in line.split():
                        if etdigit(word) is not False:
                            CHISLA.append(etdigit(word))
                        else:
                            self.show_error("Файл содержит некорректные данные")
                            return
                out_text = f"""Максимальное значение = {max(CHISLA)}
Минимальное значение = {min(CHISLA)}
Среднее значение = {"%.2f" % float(round(sum(CHISLA) / len(CHISLA), 2))}"""
                self.textBrowser.setText(out_text)
                with open("out.txt", "w", encoding="utf-8") as f:
                    f.write(out_text)
            else:
                self.show_error("Указанный файл пуст")
        except FileNotFoundError:
            self.show_error("Указанный файл не существует")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FileStat()
    window.show()
    sys.exit(app.exec())