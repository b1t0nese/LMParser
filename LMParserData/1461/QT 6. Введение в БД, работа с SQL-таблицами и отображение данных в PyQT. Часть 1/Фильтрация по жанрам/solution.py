from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QComboBox,
    QTableWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem)
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
        self.setWindowTitle("Фильтрация по жанрам")
        self.setGeometry(100, 100, 600, 400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        self.parameterSelection = QComboBox()
        self.parameterSelection.addItems(
            map(lambda x: x[1], self.get_genres().items()))
        left_layout.addWidget(self.parameterSelection)
        self.queryButton = QPushButton("Пуск")
        self.queryButton.clicked.connect(self.search_films)
        left_layout.addWidget(self.queryButton)
        left_layout.addStretch(0)
        main_layout.addWidget(left_widget)

        self.tableWidget = QTableWidget()
        main_layout.addWidget(self.tableWidget, stretch=2)

        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 3)

    def get_genres(self):
        con, cur = get_sql_connection()
        return dict(cur.execute("SELECT * FROM genres"))

    def search_films(self):
        con, cur = get_sql_connection()
        films = cur.execute("""SELECT films.title, films.genre, films.year FROM films 
INNER JOIN genres ON films.genre = genres.id 
WHERE genres.title=?""", (self.parameterSelection.currentText(),)).fetchall()
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(films) if films else 0)
        self.tableWidget.setColumnCount(len(films[0]) if films else 0)
        if films:
            self.tableWidget.setHorizontalHeaderLabels(["Название", "Жанр", "Год"])
            for r, film in enumerate(films):
                for c, col in enumerate(film):
                    self.tableWidget.setItem(r, c, QTableWidgetItem(str(col)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())