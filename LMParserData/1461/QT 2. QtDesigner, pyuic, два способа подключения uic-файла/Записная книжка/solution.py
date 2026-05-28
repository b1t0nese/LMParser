import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

# from notes_ui import (
#     Ui_MyNotesWindow,
# )  # python -m PyQt6.uic.pyuic -x notes.ui -o notes_ui.py
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MyNotesWindow(object):
    def setupUi(self, MyNotesWindow):
        MyNotesWindow.setObjectName("MyNotesWindow")
        MyNotesWindow.resize(445, 405)
        self.centralwidget = QtWidgets.QWidget(parent=MyNotesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.contactName = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contactName.setFont(font)
        self.contactName.setObjectName("contactName")
        self.gridLayout.addWidget(self.contactName, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.contactNumber = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.contactNumber.setFont(font)
        self.contactNumber.setObjectName("contactNumber")
        self.gridLayout.addWidget(self.contactNumber, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.addContactBtn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addContactBtn.setFont(font)
        self.addContactBtn.setObjectName("addContactBtn")
        self.horizontalLayout.addWidget(self.addContactBtn)
        self.contactList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.contactList.setGeometry(QtCore.QRect(10, 160, 420, 210))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contactList.setFont(font)
        self.contactList.setObjectName("contactList")
        MyNotesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MyNotesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 21))
        self.menubar.setObjectName("menubar")
        MyNotesWindow.setMenuBar(self.menubar)

        self.retranslateUi(MyNotesWindow)
        QtCore.QMetaObject.connectSlotsByName(MyNotesWindow)

    def retranslateUi(self, MyNotesWindow):
        _translate = QtCore.QCoreApplication.translate
        MyNotesWindow.setWindowTitle(_translate("MyNotesWindow", "Записная книжка"))
        self.label.setText(_translate("MyNotesWindow", "Имя:"))
        self.label_2.setText(_translate("MyNotesWindow", "Телефон:"))
        self.addContactBtn.setText(_translate("MyNotesWindow", "Добавить"))


class MyNotes(QMainWindow, Ui_MyNotesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.addContactBtn.clicked.connect(self.add_contact)

    def add_contact(self):
        self.contactList.addItem(
            f"{self.contactName.text()} {self.contactNumber.text()}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())