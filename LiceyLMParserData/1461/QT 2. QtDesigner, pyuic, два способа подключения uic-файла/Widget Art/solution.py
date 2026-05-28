from PyQt6 import QtCore, QtGui, QtWidgets


class WidgetArt:
    def __init__(self, matrix):
        self.width, self.height = len(matrix[0]) * 45, len(matrix) * 45
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi()
        self.visualize_matrix(matrix)
        self.MainWindow.show()

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(self.width, self.height)
        self.MainWindow.setMinimumSize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widgetArt = QtWidgets.QGridLayout(self.centralwidget)
        self.widgetArt.setObjectName("widgetArt")

        self.MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def visualize_matrix(self, matrix):
        for i, line in enumerate(matrix):
            for j, num in enumerate(line):
                button = QtWidgets.QPushButton(text="*" if num == 1 else "")
                button.setFixedSize(40, 40)
                button.setFont(QtGui.QFont("Arial", 18))
                self.widgetArt.addWidget(button, i, j)