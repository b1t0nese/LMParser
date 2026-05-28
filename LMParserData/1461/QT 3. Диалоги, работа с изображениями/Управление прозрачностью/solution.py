from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QImage, QPixmap, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, image_path):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 310)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.alpha = QtWidgets.QSlider(parent=self.centralwidget)
        self.alpha.setGeometry(QtCore.QRect(10, 20, 30, 270))
        self.alpha.setMaximum(255)
        self.alpha.setValue(255)
        self.alpha.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.alpha.setObjectName("alpha")
        self.curr_imageWidget = QtWidgets.QLabel(self.centralwidget)
        self.curr_imageWidget.setGeometry(QtCore.QRect(60, 5, 300, 300))
        self.curr_imageWidget.setObjectName("curr_imageWidget")
        self.curr_imageCOXR = QImage(image_path)
        self.update_image(255)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменение прозрачности"))

    def update_image(self, opacity):
        self.curr_image = QImage(
            self.curr_imageCOXR.width(), self.curr_imageCOXR.height(),
            QImage.Format.Format_RGBA8888)
        for x in range(self.curr_imageCOXR.width()):
            for y in range(self.curr_imageCOXR.height()):
                color = QColor(self.curr_imageCOXR.pixel(x, y))
                new_color = QColor(color.red(), color.green(), color.blue(), opacity)
                self.curr_image.setPixel(x, y, new_color.rgba())
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.curr_imageWidget.setPixmap(self.pixmap)
        self.curr_image.save("new.png", "PNG")


class AlphaManagement(QMainWindow, Ui_MainWindow):
    def __init__(self, image_path="orig.jpg"):
        super().__init__()
        self.setupUi(self, image_path)
        self.alpha.valueChanged.connect(self.update_image)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec())