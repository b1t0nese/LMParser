from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLineEdit,
    QTableWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem, QLabel)
import sqlite3
import sys


def get_sql_connection():
    con = sqlite3.connect('films_db.sqlite')
    return con, con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Поиск по фильмам 2.0")
        self.setGeometry(100, 100, 800, 400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.addWidget(QLabel("Год"))
        self.year = QLineEdit()
        left_layout.addWidget(self.year)
        left_layout.addWidget(QLabel("Название"))
        self.title = QLineEdit()
        left_layout.addWidget(self.title)
        left_layout.addWidget(QLabel("Длина"))
        self.duration = QLineEdit()
        left_layout.addWidget(self.duration)
        left_layout.addStretch(1)
        self.queryButton = QPushButton("Пуск")
        self.queryButton.clicked.connect(self.search_films)
        left_layout.addWidget(self.queryButton)
        main_layout.addWidget(left_widget)

        self.tableWidget = QTableWidget()
        main_layout.addWidget(self.tableWidget, stretch=2)

        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 3)

    def search_films(self):
        conditions = []
        if self.year.text():
            conditions.append(f" year {self.year.text()}")
        if self.title.text():
            conditions.append(f" title {self.title.text()}")
        if self.duration.text():
            conditions.append(f" duration {self.duration.text()}")
        sql = "SELECT * FROM films"
        if conditions:
            sql += " WHERE" + " AND".join(conditions)
        con, cur = get_sql_connection()
        films = cur.execute(sql).fetchall()
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(films) if films else 0)
        self.tableWidget.setColumnCount(len(films[0]) if films else 0)
        if films:
            self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Год", "Жанр", "Продолжительность"])
            for r, film in enumerate(films):
                for c, col in enumerate(film):
                    self.tableWidget.setItem(r, c, QTableWidgetItem(str(col)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())