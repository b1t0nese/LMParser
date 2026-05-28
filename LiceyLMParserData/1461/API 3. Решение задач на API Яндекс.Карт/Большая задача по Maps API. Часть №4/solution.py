from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QFont, QKeyEvent
from PyQt6.QtCore import Qt
import qdarktheme
import requests
import sys
import os


STATIC_MAPS_API_KEY = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"


class TheyMaps(QMainWindow):
    def __init__(self, latitude: float, longitude: float, map_scale: int, move_step: float=0.01, logging: bool=True):
        super().__init__()
        self.move_step, self.logging, self.map_file = move_step, logging, "map.png"
        self.latitude, self.longitude, self.map_scale = latitude, longitude, map_scale
        self.initUI()
        self.update_map()

    def get_image(self):
        map_request = f"""http://static-maps.yandex.ru/1.x/?ll={self.longitude},{self.latitude}&z={
            self.map_scale}&size={self.image.width()},{self.image.height()}&l=map&theme={
                self.theme}&apikey={STATIC_MAPS_API_KEY}"""
        response = requests.get(map_request)
        if self.logging:
            print(f"""\nRequest: {map_request}\nHttp статус: {response.status_code} ({
                response.reason})\nResponse: {response.text if not response else "image"}""")
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        self.setWindowTitle('TheyMaps')
        self.setFixedSize(650, 480)
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 650, 450)
        self.choice_theme = QPushButton("Светлая тема", self)
        self.choice_theme.setFont(QFont("Arial", pointSize=14))
        self.choice_theme.move(0, 450)
        self.choice_theme.setFixedSize(self.choice_theme.sizeHint())
        self.choice_theme.clicked.connect(self.change_theme)
        self.theme = "light"
        self.setStyleSheet(qdarktheme.load_stylesheet("light"))

    def change_theme(self):
        if self.theme == "light":
            self.theme = "dark"
            self.choice_theme.setText("Чёрная тема")
            self.setStyleSheet(qdarktheme.load_stylesheet("dark"))
        elif self.theme == "dark":
            self.theme = "light"
            self.choice_theme.setText("Светлая тема")
            self.setStyleSheet(qdarktheme.load_stylesheet("light"))
        self.update_map()

    def update_map(self):
        self.get_image()
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event: QKeyEvent):
        move_step = self.move_step / (self.map_scale % 11.5)
        if event.key() == Qt.Key.Key_PageUp and self.map_scale < 21:
            self.map_scale += 1
        elif event.key() == Qt.Key.Key_PageDown and self.map_scale > 0:
            self.map_scale -= 1
        elif event.key() == Qt.Key.Key_Up and self.latitude < 180:
            self.latitude += move_step
        elif event.key() == Qt.Key.Key_Down and self.latitude > 0:
            self.latitude -= move_step
        elif event.key() == Qt.Key.Key_Right and self.longitude<180:
            self.longitude += move_step
        elif event.key() == Qt.Key.Key_Left and self.longitude>0:
            self.longitude -= move_step
        self.update_map()

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TheyMaps(60.938545, 76.558902, 12)
    window.show()
    sys.exit(app.exec())