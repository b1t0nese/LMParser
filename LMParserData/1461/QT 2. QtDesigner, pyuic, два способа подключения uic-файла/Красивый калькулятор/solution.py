import sys
import math

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(510, 800)
        self.centralwidget = QtWidgets.QWidget(parent=Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 511, 141))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 140, 511, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridKeyboard = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridKeyboard.setContentsMargins(0, 0, 0, 0)
        self.gridKeyboard.setObjectName("gridKeyboard")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridKeyboard.addWidget(self.pushButton_8, 1, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridKeyboard.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setMouseTracking(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridKeyboard.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridKeyboard.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridKeyboard.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridKeyboard.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridKeyboard.addWidget(self.pushButton_15, 3, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridKeyboard.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridKeyboard.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridKeyboard.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridKeyboard.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridKeyboard.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridKeyboard.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridKeyboard.addWidget(self.pushButton_13, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridKeyboard.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridKeyboard.addWidget(self.pushButton_14, 3, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridKeyboard.addWidget(self.pushButton_17, 4, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridKeyboard.addWidget(self.pushButton_18, 4, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridKeyboard.addWidget(self.pushButton_19, 4, 2, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 63))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active,
            QtGui.QPalette.ColorRole.AlternateBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active,
            QtGui.QPalette.ColorRole.ToolTipBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active,
            QtGui.QPalette.ColorRole.ToolTipText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.WindowText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 63))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.BrightText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.ButtonText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.AlternateBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.ToolTipBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.ToolTipText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.WindowText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 213, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 191, 63))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.BrightText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.ButtonText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.AlternateBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.ToolTipBase,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.ToolTipText,
            brush,
        )
        self.pushButton_20.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setMouseTracking(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridKeyboard.addWidget(self.pushButton_20, 4, 3, 1, 1)
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton_8.setText(_translate("Calculator", "-"))
        self.pushButton_4.setText(_translate("Calculator", "+"))
        self.pushButton_11.setText(_translate("Calculator", "9"))
        self.pushButton_6.setText(_translate("Calculator", "5"))
        self.pushButton_10.setText(_translate("Calculator", "8"))
        self.pushButton_7.setText(_translate("Calculator", "6"))
        self.pushButton_15.setText(_translate("Calculator", "="))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_16.setText(_translate("Calculator", "/"))
        self.pushButton_12.setText(_translate("Calculator", "*"))
        self.pushButton_9.setText(_translate("Calculator", "7"))
        self.pushButton_13.setText(_translate("Calculator", "0"))
        self.pushButton_5.setText(_translate("Calculator", "4"))
        self.pushButton_14.setText(_translate("Calculator", "."))
        self.pushButton_17.setText(_translate("Calculator", "^"))
        self.pushButton_18.setText(_translate("Calculator", "√"))
        self.pushButton_19.setText(_translate("Calculator", "!"))
        self.pushButton_20.setText(_translate("Calculator", "C"))


class Calculator(QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        for i in range(self.gridKeyboard.count()):
            self.gridKeyboard.itemAt(i).widget().clicked.connect(self.calc_do)
        self.lcd_text = "0"
        self.first_number = None
        self.operator = None
        self.waiting_for_second = False
        self.result_displayed = False

    def calculate_result(self):
        try:
            second_number = float(self.lcd_text)
            if self.operator == "+":
                result = self.first_number + second_number
            elif self.operator == "-":
                result = self.first_number - second_number
            elif self.operator == "*":
                result = self.first_number * second_number
            elif self.operator == "/":
                if second_number != 0:
                    result = self.first_number / second_number
                else:
                    self.lcd_text = "Error"
                    return
            elif self.operator == "^":
                result = self.first_number**second_number
            self.lcd_text = str(int(result)) if result.is_integer() else str(round(result, 2))
        except:
            self.lcd_text = "Error"

    def calc_do(self):
        btn = self.sender().text()
        if btn.isdigit():
            if (
                self.lcd_text == "0"
                or self.lcd_text == "Error"
                or self.waiting_for_second
                or self.result_displayed
            ):
                self.lcd_text = btn
                self.waiting_for_second = False
                self.result_displayed = False
            else:
                self.lcd_text += btn
        elif btn == ".":
            if self.waiting_for_second or self.result_displayed:
                self.lcd_text = "0."
                self.waiting_for_second = False
                self.result_displayed = False
            elif "." not in self.lcd_text:
                self.lcd_text += "."
        elif btn in ["+", "-", "*", "/", "^"]:
            if self.first_number is None:
                self.first_number = float(self.lcd_text)
                self.operator = btn
                self.waiting_for_second = True
            else:
                self.operator = btn
                if not self.waiting_for_second:
                    self.calculate_result()
                    self.first_number = float(self.lcd_text)
                    self.waiting_for_second = True
        elif btn == "√":
            try:
                num = float(self.lcd_text)
                if num >= 0:
                    result = math.sqrt(num)
                    result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 2)
                    self.lcd_text = str(result)
                    self.result_displayed = True
                    self.first_number = None
                    self.operator = None
                else:
                    self.lcd_text = "Error"
            except:
                self.lcd_text = "Error"
        elif btn == "!":
            try:
                num = int(float(self.lcd_text))
                if num >= 0:
                    result = math.factorial(num)
                    result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 2)
                    self.lcd_text = str(result)
                    self.result_displayed = True
                    self.first_number = None
                    self.operator = None
                else:
                    self.lcd_text = "Error"
            except:
                self.lcd_text = "Error"
        elif btn == "=" and self.first_number is not None and self.operator is not None:
            self.calculate_result()
            self.first_number = None
            self.operator = None
            self.result_displayed = True
        elif btn == "C":
            self.lcd_text = "0"
            self.first_number = None
            self.operator = None
            self.waiting_for_second = False
            self.result_displayed = False
        self.lcdNumber.display(self.lcd_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())