from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QMenu, QFileDialog
from PyQt6.QtGui import QAction
import sys
import csv


class ClosestStars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ближайшие звёзды')
        self.setGeometry(100, 100, 800, 600)
        self.text_browser = QTextBrowser()
        self.setCentralWidget(self.text_browser)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('Файл')
        open_action = QAction('Открыть', self)
        open_action.triggered.connect(self.load_file)
        file_menu.addAction(open_action)
        save_action = QAction('Сохранить', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        select_menu = menubar.addMenu('Выбор')
        spectral_menu = QMenu('Спектральный класс', self)
        for sp_class in ['O', 'B', 'A', 'F', 'G', 'K', 'M']:
            action = QAction(sp_class, self)
            action.triggered.connect(lambda checked, c=sp_class: self.filter_by_spectral(c))
            spectral_menu.addAction(action)
        select_menu.addMenu(spectral_menu)
        distance_menu = QMenu('Расстояние', self)
        for name, limit in [('до 10', 10), ('до 20', 20), ('до 30', 30), ('свыше 30', 30)]:
            action = QAction(name, self)
            if name == 'свыше 30':
                action.triggered.connect(lambda checked, lim=limit: self.filter_by_distance(lim, is_greater=True))
            else:
                action.triggered.connect(lambda checked, lim=limit: self.filter_by_distance(lim))
            distance_menu.addAction(action)
        select_menu.addMenu(distance_menu)

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, 'Открыть файл', '', 'CSV файлы (*.csv);;Все файлы (*)')
        if filename:
            self.text = []
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)
                for row in reader:
                    if len(row) >= 8:
                        self.text.append(row)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, 'Сохранить файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)')
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.current_content)

    def filter_by_spectral(self, spectral_class):
        filtered_stars = []
        for star in self.text:
            if (len(star) >= 3 and star[2].strip()) and (star[2].strip()[0].upper() == spectral_class):
                filtered_stars.append(star)
        self.display_results(filtered_stars, f'Спектральный класс {spectral_class}')

    def filter_by_distance(self, distance_limit, is_greater=False):
        filtered_stars = []
        for star in self.text:
            if len(star) >= 8 and star[7].strip():
                try:
                    distance = float(star[7].strip())
                    if is_greater and distance > distance_limit:
                        filtered_stars.append(star)
                    elif distance <= distance_limit:
                        filtered_stars.append(star)
                except ValueError:
                    continue
        if is_greater and distance_limit == 30:
            title = 'Расстояние свыше 30'
        else:
            title = f'Расстояние до {distance_limit}'
        self.display_results(filtered_stars, title)

    def display_results(self, stars, title):
        full_names = []
        for star in stars:
            designation, component = star[0].strip(), star[1].strip()
            full_names.append(f'{designation} {component}' if component else designation)
        self.current_content = f'<h3>{title}</h3>'
        for name in sorted(full_names):
            self.current_content += f'<p>{name}</p>'
        self.text_browser.setHtml(self.current_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClosestStars()
    window.show()
    sys.exit(app.exec())