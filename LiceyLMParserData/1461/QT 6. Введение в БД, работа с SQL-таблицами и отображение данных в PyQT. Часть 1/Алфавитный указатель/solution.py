from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QHBoxLayout, QStatusBar)
import sys
import sqlite3


def get_sql_connection():
    con = sqlite3.connect('films_db.sqlite')
    return con, con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Алфавитный указатель")
        self.setGeometry(100, 100, 800, 600)
        main_layout = QVBoxLayout()

        buttons_layout = QHBoxLayout()
        self.buttons = []
        for char in [
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
            'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
        ]:
            button = QPushButton(char)
            button.setStyleSheet("font: 16px")
            button.setFixedSize(25, 30)
            button.clicked.connect(self.search_films)
            buttons_layout.addWidget(button)
            self.buttons.append(button)
        main_layout.addLayout(buttons_layout)

        self.tableWidget = QTableWidget()
        main_layout.addWidget(self.tableWidget, stretch=1)
        self.statusbar = QStatusBar()
        main_layout.addWidget(self.statusbar)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def search_films(self):
        con, cur = get_sql_connection()
        films = cur.execute(
            f"SELECT * FROM films WHERE title LIKE '{self.sender().text()}%'").fetchall()
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(films) if films else 0)
        self.tableWidget.setColumnCount(len(films[0]) if films else 0)
        if films:
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Год", "Жанр", "Продолжительность"])
            for r, film in enumerate(films):
                for c, col in enumerate(film):
                    self.tableWidget.setItem(r, c, QTableWidgetItem(str(col)))
            self.statusBar().showMessage(f"Нашлось {len(films)} записей")
        else:
            self.statusBar().showMessage("К сожалению, ничего не нашлось")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())