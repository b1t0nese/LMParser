from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QTextEdit,
                             QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame, QSlider)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QEvent
import qdarktheme
import requests
import sys
import os


GEOCODE_MAPS_API_KEY = "8013b162-6b42-4997-9691-77b7074026e0"
STATIC_MAPS_API_KEY = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"


def get_location_data(toponym: str, logging: bool=False):
    api_url, params = "http://geocode-maps.yandex.ru/1.x/", {
        "apikey": GEOCODE_MAPS_API_KEY, "geocode": toponym, "format": "json"}
    response = requests.get(api_url, params)
    if logging:
        print(f"""\nRequest: {api_url}, {params}\nHttp статус: {response.status_code} ({
            response.reason})\nResponse: {response.text}""")
    if not response:
        return
    json_response = response.json()
    feature_member = json_response["response"]["GeoObjectCollection"]["featureMember"]
    if feature_member:
        return feature_member[0]["GeoObject"]


class StaticMapAPI:
    def __init__(self, start_longitude: float, start_latitude: float, map_scale: int=10, map_size: tuple=(650, 450),
                 map_theme: str="light", move_step: float=0.001, logging: bool=True, map_file_path: str="map.png"):
        self.logging = logging
        self.map_file = map_file_path
        self.longitude = start_longitude
        self.latitude = start_latitude
        self.map_scale = map_scale
        self.map_theme = map_theme
        self.map_size = map_size
        self.move_step = move_step
        self.move_step_now = self.move_step
        self.points = []

    def get_image(self):
        api_url, params = "http://static-maps.yandex.ru/1.x/", {
            "apikey": STATIC_MAPS_API_KEY, "ll": f"{self.longitude},{self.latitude}",
            "z": self.map_scale, "size": f"{self.map_size[0]},{self.map_size[1]}", "l": "map",
            "theme": self.map_theme, "pt": "~".join([",".join(map(str, pt)) for pt in self.points])}
        response = requests.get(api_url, params)
        if self.logging:
            print(f"""\nRequest: {api_url}, {params}\nHttp статус: {response.status_code} ({
                response.reason})\nResponse: {response.text if not response else "image"}""")
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def set_move_step(self, x: int):
        if x > 0:
            self.move_step_now = self.move_step * x
        elif x < 0:
            self.move_step_now = self.move_step / abs(x)

    def calc_move(self):
        step = self.move_step_now * max(1, (1.3 ** (23 - self.map_scale)))
        return step * 2 if self.map_scale <= 14 else step / 2

    def add_scale(self):
        if self.map_scale < 21: self.map_scale += 1

    def subt_scale(self):
        if self.map_scale > 0: self.map_scale -= 1

    def add_point(self, longitude: float, latitude: float, style: str="comma"):
        self.points.append([longitude, latitude, style])
    
    def pop_point(self, index: int=-1):
        if self.points and len(self.points) > index:
            self.points.pop(index)

    def move_to_location(self, toponym: str, map_scale: int=None, add_postcode: bool=False) -> tuple[float, float, str] | None:
        loc_data = get_location_data(toponym, self.logging)
        if not loc_data:
            return
        self.longitude, self.latitude = map(float, loc_data["Point"]["pos"].split(" "))
        loc_metadata = loc_data["metaDataProperty"]["GeocoderMetaData"]
        if not map_scale:
            self.map_scale = {
                "entrance": 20,
                "house": 18, "metro": 18, "railway_station": 18, "station": 18, "route": 18,
                "street": 15, "district": 15, "airport": 15,
                "hydro": 13, "vegetation": 13, "other": 13,
                "locality": 11, "province": 11,
                "area": 5, "country": 5,
            }.get(loc_metadata["kind"], 10)
        else:
            self.map_scale = map_scale
        postal_code = loc_metadata["Address"].get("postal_code", "")
        address = loc_metadata["Address"]["formatted"] + (
            f", {postal_code}" if add_postcode and postal_code else "")
        return self.longitude, self.latitude, address

    def close(self):
        os.remove(self.map_file)


class WindowUI(QMainWindow):
    def initUI(self):
        self.setWindowTitle('TheyMaps')
        self.setFixedSize(650, 540)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        top_panel = QWidget()
        top_panel.setFixedHeight(40)
        top_panel_layout = QHBoxLayout(top_panel)
        top_panel_layout.setContentsMargins(5, 5, 5, 5)

        title_label = QLabel("TheyMaps")
        title_label.setFont(QFont("Arial", pointSize=16, weight=QFont.Weight.Bold))
        top_panel_layout.addWidget(title_label)
        
        top_panel_layout.addStretch()

        self.menu_button = QPushButton("☰")
        self.menu_button.setFont(QFont("Arial", pointSize=18))
        self.menu_button.setFixedSize(40, 30)
        self.menu_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.menu_button.clicked.connect(self.toggle_settings_panel)
        top_panel_layout.addWidget(self.menu_button)

        main_layout.addWidget(top_panel)

        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        self.image = QLabel()
        self.image.setStyleSheet("background-color: #f0f0f0;")
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image.setText("Карта")
        self.image.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.image.update_image = lambda: None
        content_layout.addWidget(self.image, 1)

        self.settings_panel = QWidget()
        self.settings_panel.setFixedWidth(200)
        self.settings_panel.setVisible(False)

        settings_layout = QVBoxLayout(self.settings_panel)
        settings_layout.setContentsMargins(10, 15, 10, 15)
        settings_layout.setSpacing(15)

        settings_title = QLabel("Настройки")
        settings_title.setFont(QFont("Arial", pointSize=14, weight=QFont.Weight.Bold))
        settings_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        settings_layout.addWidget(settings_title)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("background-color: #ccc;")
        settings_layout.addWidget(line)

        self.theme_button = QPushButton("☀️ Светлая тема")
        self.theme_button.clicked.connect(self.change_theme)
        settings_layout.addWidget(self.theme_button)

        self.index_button = QPushButton("📍 Показывать почтовый индекс")
        self.index_button.setCheckable(True)
        self.index_button.setChecked(False)
        settings_layout.addWidget(self.index_button)

        self.points_button = QPushButton("📍 Ставить метки")
        self.points_button.setCheckable(True)
        self.points_button.setChecked(True)
        settings_layout.addWidget(self.points_button)

        self.speed_label = QLabel("⚡ Скорость движения:")
        self.speed_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        settings_layout.addWidget(self.speed_label)

        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(-1000)
        self.speed_slider.setMaximum(1000)
        self.speed_slider.setValue(0)
        settings_layout.addWidget(self.speed_slider)

        settings_layout.addStretch()
        content_layout.addWidget(self.settings_panel)
        main_layout.addWidget(content_widget, 1)

        search_container = QWidget()
        search_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(2)

        self.reset_button = QPushButton("Сброс")
        self.reset_button.setFont(QFont("Arial", pointSize=12))
        self.reset_button.setFixedHeight(40)
        self.reset_button.setFixedWidth(self.reset_button.sizeHint().width())
        search_layout.addWidget(self.reset_button)

        self.search_entry = QTextEdit("Нижневартовск")
        self.search_entry.setFont(QFont("Arial", pointSize=12))
        self.search_entry.setFixedHeight(40)
        self.search_entry.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.search_entry.installEventFilter(self)
        search_layout.addWidget(self.search_entry)

        self.search_button = QPushButton("Поиск")
        self.search_button.setFont(QFont("Arial", pointSize=12))
        self.search_button.setFixedHeight(40)
        self.search_button.setFixedWidth(self.search_button.sizeHint().width())
        search_layout.addWidget(self.search_button)

        bottom_panel = QWidget()
        bottom_panel.setFixedHeight(50)
        bottom_panel_layout = QHBoxLayout(bottom_panel)
        bottom_panel_layout.setContentsMargins(5, 5, 5, 5)
        bottom_panel_layout.setSpacing(5)
        bottom_panel_layout.addWidget(search_container)
        main_layout.addWidget(bottom_panel)

        self.change_theme(None, "light")

    def toggle_settings_panel(self):
        self.settings_panel.setVisible(not self.settings_panel.isVisible())
        if self.settings_panel.isVisible():
            self.menu_button.setText("✕")
        else:
            self.menu_button.setText("☰")

    def change_theme(self, event: QEvent, theme: str=None) -> str:
        if theme == "dark" or (not theme and self.theme == "light"):
            self.theme = "dark"
            self.theme_button.setText("🌙 Тёмная тема")
            self.setStyleSheet(qdarktheme.load_stylesheet("dark"))
        elif theme == "light" or (not theme and self.theme == "dark"):
            self.theme = "light"
            self.theme_button.setText("☀️ Светлая тема")
            self.setStyleSheet(qdarktheme.load_stylesheet("light"))
        self.image.update_image()
        return self.theme


class TheyMaps(WindowUI):
    def __init__(self, StaticMapAPI_args: tuple):
        super().__init__()
        self.static_map_api = StaticMapAPI(*StaticMapAPI_args)
        self.startUI()

    def startUI(self):
        self.initUI()
        self.image.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.image.mousePressEvent = self.image_focus
        self.image.keyPressEvent = self.image_keyPressEvent
        self.reset_button.clicked.connect(self.reset_search)
        self.search_entry.orig_keyPressEvent = self.search_entry.keyPressEvent
        self.search_entry.keyPressEvent = self.search_keyPressEvent
        self.search_button.clicked.connect(self.on_search)
        self.image.update_image = self.update_map
        self.speed_slider.valueChanged.connect(self.set_speed)
        self.index_button.clicked.connect(lambda e: self.on_search(e, False))
        self.update_map()

    def update_map(self):
        self.static_map_api.map_theme = self.theme
        self.static_map_api.get_image()
        self.pixmap = QPixmap(self.static_map_api.map_file)
        self.image.setPixmap(self.pixmap)
        self.image.setFocus()

    def on_search(self, event: QEvent=None, set_point: bool=None):
        point = self.static_map_api.move_to_location(
            self.search_entry.toPlainText(), None, self.index_button.isChecked())
        if point:
            if set_point or (set_point is None and self.points_button.isChecked()):
                self.static_map_api.add_point(*point[:2])
            self.search_entry.setText(point[2])
            self.update_map()
        self.image_focus()

    def reset_search(self, event: QEvent):
        self.static_map_api.pop_point()
        self.search_entry.clear()
        self.update_map()

    def set_speed(self, event: QEvent):
        koef = int(self.sender().value()) / 100
        self.static_map_api.set_move_step(koef)
        self.speed_label.setText(f"⚡ Скорость движения (x: {koef}):")

    def image_keyPressEvent(self, event: QEvent):
        key = event.key()
        if key == Qt.Key.Key_PageUp:
            self.static_map_api.add_scale()
        elif key == Qt.Key.Key_PageDown:
            self.static_map_api.subt_scale()
        elif key == Qt.Key.Key_Up:
            self.static_map_api.latitude += self.static_map_api.calc_move() / 3
        elif key == Qt.Key.Key_Down:
            self.static_map_api.latitude -= self.static_map_api.calc_move() / 3
        elif key == Qt.Key.Key_Left:
            self.static_map_api.longitude -= self.static_map_api.calc_move()
        elif key == Qt.Key.Key_Right:
            self.static_map_api.longitude += self.static_map_api.calc_move()
        else:
            super().keyPressEvent(event)
            return
        self.update_map()
        event.accept()

    def search_keyPressEvent(self, event: QEvent):
        key = event.key()
        if key in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.on_search()
        else:
            self.search_entry.orig_keyPressEvent(event)
            return
        event.accept()

    def image_focus(self, event=None):
        self.search_entry.clearFocus()
        self.image.setFocus()

    def closeEvent(self, event):
        self.static_map_api.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TheyMaps((76.558902, 60.938545, 10))
    window.show()
    sys.exit(app.exec())