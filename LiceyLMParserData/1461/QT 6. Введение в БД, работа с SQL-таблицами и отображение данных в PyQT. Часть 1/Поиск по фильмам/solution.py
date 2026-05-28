from PyQt6.QtWidgets import (
    QApplication, QWidget, QComboBox, QPushButton,
    QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow)
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
        self.setWindowTitle("Поиск по фильмам")
        self.setFixedSize(500, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Поле поиска:"))
        self.parameterSelection = QComboBox()
        self.parameterSelection.addItems(['Год выпуска', 'Название', 'Продолжительность'])
        search_layout.addWidget(self.parameterSelection)
        self.queryLine = QLineEdit()
        search_layout.addWidget(self.queryLine)
        self.queryButton = QPushButton('Поиск')
        self.queryButton.clicked.connect(self.update_data)
        search_layout.addWidget(self.queryButton)
        main_layout.addLayout(search_layout)

        form_layout = QVBoxLayout()
        id_layout = QHBoxLayout()
        id_layout.addWidget(QLabel("ID:"))
        self.idEdit = QLineEdit()
        id_layout.addWidget(self.idEdit)
        form_layout.addLayout(id_layout)

        title_layout = QHBoxLayout()
        title_layout.addWidget(QLabel("Название:"))
        self.titleEdit = QLineEdit()
        title_layout.addWidget(self.titleEdit)
        form_layout.addLayout(title_layout)

        year_layout = QHBoxLayout()
        year_layout.addWidget(QLabel("Год:"))
        self.yearEdit = QLineEdit()
        year_layout.addWidget(self.yearEdit)
        form_layout.addLayout(year_layout)

        genre_layout = QHBoxLayout()
        genre_layout.addWidget(QLabel("Жанр:"))
        self.genreEdit = QLineEdit()
        genre_layout.addWidget(self.genreEdit)
        form_layout.addLayout(genre_layout)

        duration_layout = QHBoxLayout()
        duration_layout.addWidget(QLabel("Продолжительность:"))
        self.durationEdit = QLineEdit()
        duration_layout.addWidget(self.durationEdit)
        form_layout.addLayout(duration_layout)

        main_layout.addLayout(form_layout)

        self.errorLabel = QLabel("")
        self.errorLabel.setStyleSheet("color: red;")
        main_layout.addWidget(self.errorLabel)

        main_layout.addStretch(1)

    def set_labels(self, id="", title="", year="", genre="", duration="", error=""):
        self.idEdit.setText(str(id))
        self.titleEdit.setText(str(title))
        self.yearEdit.setText(str(year))
        self.genreEdit.setText(str(genre))
        self.durationEdit.setText(str(duration))
        self.errorLabel.setText(str(error))

    def update_data(self):
        if not self.queryLine.text():
            self.set_labels(error='Неправильный запрос')
            return

        con, cur = get_sql_connection()
        if self.parameterSelection.currentText() == 'Год выпуска':
            try:
                int(self.queryLine.text())
            except ValueError:
                self.set_labels(error='Неправильный запрос')
                return
            condition = "year = ?"
        elif self.parameterSelection.currentText() == 'Название':
            condition = "title = ?"
        elif self.parameterSelection.currentText() == 'Продолжительность':
            try:
                int(self.queryLine.text())
            except ValueError:
                self.set_labels(error='Неправильный запрос')
                return
            condition = "duration = ?"
        film = cur.execute(f"""SELECT id, title, year, genre, duration
FROM films WHERE {condition}""", (self.queryLine.text(),)).fetchone()
        con.close()

        if film:
            self.set_labels(*film, '')
        else:
            self.set_labels(error='Ничего не найдено')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())