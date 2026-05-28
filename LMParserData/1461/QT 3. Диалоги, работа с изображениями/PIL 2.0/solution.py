from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, image_path):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 330)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.channelButtons = QtWidgets.QButtonGroup(self)
        self.rotateButtons = QtWidgets.QButtonGroup(self)

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.channelButtonsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.channelButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.channelButtonsLayout.setObjectName("channelButtonsLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.channelButtonsLayout.addWidget(self.pushButton)
        self.channelButtons.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.channelButtonsLayout.addWidget(self.pushButton_2)
        self.channelButtons.addButton(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.channelButtonsLayout.addWidget(self.pushButton_3)
        self.channelButtons.addButton(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.channelButtonsLayout.addWidget(self.pushButton_4)
        self.channelButtons.addButton(self.pushButton_4)

        self.curr_imageWidget = QtWidgets.QLabel(self.centralwidget)
        self.curr_imageWidget.setGeometry(QtCore.QRect(200, 10, 256, 256))
        self.curr_imageWidget.setObjectName("curr_imageWidget")
        self.curr_imageCOXR = QImage(image_path)
        self.curr_image = self.curr_imageCOXR.copy()
        self.update_image()

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 280, 430, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.rotateButtonsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.rotateButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.rotateButtonsLayout.setObjectName("rotateButtonsLayout")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.rotateButtonsLayout.addWidget(self.pushButton_5)
        self.rotateButtons.addButton(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.rotateButtonsLayout.addWidget(self.pushButton_6)
        self.rotateButtons.addButton(self.pushButton_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIL 2.0"))
        self.pushButton.setText(_translate("MainWindow", "R"))
        self.pushButton_2.setText(_translate("MainWindow", "G"))
        self.pushButton_3.setText(_translate("MainWindow", "B"))
        self.pushButton_4.setText(_translate("MainWindow", "ALL"))
        self.pushButton_5.setText(_translate("MainWindow", "Против часовой стрелки"))
        self.pushButton_6.setText(_translate("MainWindow", "По часовой стрелке"))

    def update_image(self):
        pixmap = QPixmap.fromImage(self.curr_image)
        self.curr_imageWidget.setPixmap(
            pixmap.scaled(
                256,
                256,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.curr_imageWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)


class MyPillow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.image_path = self.init_file_dialog()[0]
        self.setupUi(self, self.image_path)
        for btn in self.channelButtons.buttons():
            btn.clicked.connect(self.change_img_channel)
        self.pushButton_5.clicked.connect(self.rotate_img_l)
        self.pushButton_6.clicked.connect(self.rotate_img_r)

    def init_file_dialog(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.file_dialog.setNameFilter("Images (*.png *.jpg)")
        return self.file_dialog.getOpenFileName()

    def rotate_img_do(self, gradus):
        self.curr_imageCOXR = self.curr_imageCOXR.transformed(
            QTransform().rotate(gradus)
        )
        self.curr_image = self.curr_image.transformed(QTransform().rotate(gradus))
        self.update_image()

    def rotate_img_l(self):
        self.rotate_img_do(-90)

    def rotate_img_r(self):
        self.rotate_img_do(90)

    def channel_to_grayscale(self, channel="R"):
        for y in range(self.curr_imageCOXR.height()):
            for x in range(self.curr_imageCOXR.width()):
                color = self.curr_imageCOXR.pixelColor(x, y)
                if channel == "R":
                    ncolor = QColor(color.red(), 0, 0)
                elif channel == "G":
                    ncolor = QColor(0, color.green(), 0)
                elif channel == "B":
                    ncolor = QColor(0, 0, color.blue())
                else:
                    ncolor = self.curr_imageCOXR.pixelColor(x, y)
                self.curr_image.setPixelColor(x, y, ncolor)
        self.update_image()

    def change_img_channel(self):
        channel = self.sender().text()
        self.channel_to_grayscale(channel)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())