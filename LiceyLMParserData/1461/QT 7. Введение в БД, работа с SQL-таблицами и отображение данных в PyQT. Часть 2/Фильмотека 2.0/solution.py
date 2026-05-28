from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTableWidget,
    QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QComboBox, QTabWidget, QMessageBox)
import sys
import sqlite3


def get_sql_connection():
    con = sqlite3.connect('films_db.sqlite')
    return con, con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.add_film_widget = None
        self.edit_film_widget = None
        self.add_genre_widget = None
        self.edit_genre_widget = None
        self.initUI()
        self.selected_items, self.ids = [], []
        self.update_films()
        self.update_genres()

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Фильмотека")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.tabWidget = QTabWidget()
        self.filmsTab = QWidget()
        self.filmsTab.setObjectName("filmsTab")
        films_layout = QVBoxLayout(self.filmsTab)
        films_buttons_layout = QHBoxLayout()
        self.addFilmButton = QPushButton("Добавить фильм")
        self.addFilmButton.clicked.connect(self.add_film)
        self.editFilmButton = QPushButton("Изменить фильм")
        self.editFilmButton.clicked.connect(self.edit_film)
        self.deleteFilmButton = QPushButton("Удалить фильм")
        self.deleteFilmButton.clicked.connect(self.delete_film)
        films_buttons_layout.addWidget(self.addFilmButton)
        films_buttons_layout.addWidget(self.editFilmButton)
        films_buttons_layout.addWidget(self.deleteFilmButton)
        films_buttons_layout.addStretch()
        self.filmsTable = QTableWidget()
        self.filmsTable.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)
        films_layout.addLayout(films_buttons_layout)
        films_layout.addWidget(self.filmsTable)

        self.genresTab = QWidget()
        self.genresTab.setObjectName("genresTab")
        genres_layout = QVBoxLayout(self.genresTab)
        genres_buttons_layout = QHBoxLayout()
        self.addGenreButton = QPushButton("Добавить жанр")
        self.addGenreButton.clicked.connect(self.add_genre)
        self.editGenreButton = QPushButton("Редактировать жанр")
        self.editGenreButton.clicked.connect(self.edit_genre)
        self.deleteGenreButton = QPushButton("Удалить жанр")
        self.deleteGenreButton.clicked.connect(self.delete_genre)
        genres_buttons_layout.addWidget(self.addGenreButton)
        genres_buttons_layout.addWidget(self.editGenreButton)
        genres_buttons_layout.addWidget(self.deleteGenreButton)
        genres_buttons_layout.addStretch()
        self.genresTable = QTableWidget()
        self.genresTable.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)
        genres_layout.addLayout(genres_buttons_layout)
        genres_layout.addWidget(self.genresTable)

        self.tabWidget.addTab(self.filmsTab, "Фильмы")
        self.tabWidget.addTab(self.genresTab, "Жанры")
        self.tabWidget.currentChanged.connect(self.tab_changed)
        main_layout.addWidget(self.tabWidget)

    def add_film(self):
        self.add_film_widget = AddFilmWidget(self)
        self.add_film_widget.show()

    def edit_film(self):
        self.selected_items = self.filmsTable.selectedItems()
        if self.selected_items:
            self.ids = [self.filmsTable.item(self.selected_items[0].row(), 0).text()]
            if len(set(i.row() for i in self.selected_items)) == 1:
                self.edit_film_widget = AddFilmWidget(self, 1)
                self.edit_film_widget.update_edit_window()
                self.edit_film_widget.show()

    def delete_film(self):
        self.selected_items = self.filmsTable.selectedItems()
        if len(self.selected_items):
            ids = []
            for i in self.selected_items:
                id = self.filmsTable.item(i.row(), 0).text()
                if id not in ids:
                    ids.append(id)
            valid = QMessageBox.question(
                self, '', "Действительно удалить элементы с id " + ",".join(ids),
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if valid == QMessageBox.StandardButton.Yes:
                con, cur = get_sql_connection()
                cur.execute(f"DELETE FROM films WHERE id IN ({", ".join('?' * len(ids))})", ids)
                con.commit()
                con.close()
            else:
                for selected_range in self.selected_items:
                    selected_range.setSelected(False)
            self.update_films()

    def add_genre(self):
        self.add_genre_widget = AddGenreWidget(self)
        self.add_genre_widget.show()

    def edit_genre(self):
        self.selected_items = self.genresTable.selectedItems()
        if self.selected_items:
            self.ids = [self.genresTable.item(self.selected_items[0].row(), 0).text()]
            if len(set(i.row() for i in self.selected_items)) == 1:
                self.edit_genre_widget = AddGenreWidget(self, 1)
                self.edit_genre_widget.update_edit_window()
                self.edit_genre_widget.show()

    def delete_genre(self):
        self.selected_items = self.genresTable.selectedItems()
        if len(self.selected_items):
            ids = []
            for i in self.selected_items:
                id = self.genresTable.item(i.row(), 0).text()
                if id not in ids:
                    ids.append(id)
            yes = QMessageBox.question(
                self, '', "Действительно удалить элементы с id " + ",".join(ids),
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if yes == QMessageBox.StandardButton.Yes:
                con, cur = get_sql_connection()
                cur.execute("DELETE FROM genres WHERE id IN (" + ", ".join(
                    '?' * len(ids)) + ")", ids)
                con.commit()
                con.close()
            else:
                for selected_range in self.selected_items:
                    selected_range.setSelected(False)
            self.update_films()
            self.update_genres()

    def update_films(self):
        con, cur = get_sql_connection()
        result = cur.execute("""SELECT films.id, films.title, films.year, 
COALESCE(genres.title, films.genre), films.duration FROM films
LEFT JOIN genres ON films.genre = genres.id""").fetchall()[::-1]
        self.filmsTable.setRowCount(len(result))
        self.filmsTable.setColumnCount(len(result[0]))
        self.filmsTable.setHorizontalHeaderLabels(
            ['ИД', 'Название', 'Год выпуска', 'Жанр', 'Продолжительность'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                self.filmsTable.setItem(i, j, item)

    def update_genres(self):
        con, cur = get_sql_connection()
        result = cur.execute("SELECT * FROM genres").fetchall()
        self.genresTable.setRowCount(len(result))
        try:
            if result[0]:
                self.genresTable.setColumnCount(len(result[0]))
        except Exception:
            self.genresTable.setColumnCount(0)
        self.genresTable.setHorizontalHeaderLabels(
            ['ИД', 'Название жанра'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                self.genresTable.setItem(i, j, item)

    def tab_changed(self, index):
        if index == 0:
            self.update_films()
        else:
            self.update_genres()


class AddFilmWidget(QMainWindow):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        self.parent, self.film_id = parent, film_id
        self.initUI()
        if film_id is not None:
            self.pushButton.clicked.connect(self.get_editing_verdict)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
        else:
            self.pushButton.clicked.connect(self.get_adding_verdict)
            self.setWindowTitle('Добавление фильма')
        con, cur = get_sql_connection()
        self.params = {j: i for i, j in cur.execute("SELECT * FROM genres").fetchall()}
        for i in self.params.keys():
            self.comboBox.addItem(i)

    def initUI(self):
        self.setGeometry(350, 250, 400, 300)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.title = QPlainTextEdit()
        self.year = QPlainTextEdit()
        self.duration = QPlainTextEdit()
        self.comboBox = QComboBox()
        self.pushButton = QPushButton('Сохранить')
        layout = QVBoxLayout(central_widget)
        layout.addWidget(QLabel('Название фильма'))
        layout.addWidget(self.title)
        layout.addWidget(QLabel('Год выпуска'))
        layout.addWidget(self.year)
        layout.addWidget(QLabel('Продолжительность'))
        layout.addWidget(self.duration)
        layout.addWidget(QLabel('Жанр'))
        layout.addWidget(self.comboBox)
        layout.addWidget(self.pushButton)
        layout.addStretch()

    def update_edit_window(self):
        self.title.setPlainText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 1).text())
        self.year.setPlainText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 2).text())
        self.comboBox.addItem(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 3).text())
        self.comboBox.setCurrentText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 3).text())
        self.duration.setPlainText(self.parent.filmsTable.item(self.parent.selected_items[0].row(), 4).text())

    def get_adding_verdict(self):
        try:
            if not self.title.toPlainText() or not self.year.toPlainText() or not self.duration.toPlainText() or \
                    not int(self.duration.toPlainText()) > 0 or not 0 <= int(self.year.toPlainText()) < 2025:
                raise ValueError
        except ValueError:
            return False
        con, cur = get_sql_connection()
        cur.execute('INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)', [
            self.title.toPlainText(), int(self.year.toPlainText()),
            cur.execute('SELECT id FROM genres WHERE title = ?',
                        (self.comboBox.currentText(),)).fetchall()[0][0],
            int(self.duration.toPlainText())])
        con.commit()
        con.close()
        self.parent.update_films()
        return True

    def get_editing_verdict(self):
        try:
            genre = self.comboBox.currentText()
            if not self.title.toPlainText() or not self.year.toPlainText() or not self.duration.toPlainText() or \
                    not int(self.duration.toPlainText()) > 0 or not 0 <= int(self.year.toPlainText()) < 2025:
                raise ValueError
        except ValueError:
            return False
        con, cur = get_sql_connection()
        cur.execute(
            'UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?',
            (self.title.toPlainText(), int(self.year.toPlainText()),
             cur.execute('SELECT id FROM genres WHERE title = ?',
                         (genre,)).fetchall()[0][0] if genre.isalpha() else genre,
             self.duration.toPlainText(), int(self.parent.ids[0])))
        con.commit()
        con.close()
        self.parent.update_films()
        self.close()
        return True


class AddGenreWidget(QMainWindow):
    def __init__(self, parent=None, genre_id=None):
        super().__init__(parent)
        self.parent = parent
        self.genre_id = genre_id
        self.initUI()
        if genre_id is not None:
            self.pushButton.clicked.connect(self.get_editing_verdict)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
        else:
            self.pushButton.clicked.connect(self.get_adding_verdict)
            self.setWindowTitle('Добавление записи')

    def initUI(self):
        self.setGeometry(350, 250, 400, 200)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.title = QPlainTextEdit()
        self.pushButton = QPushButton('Сохранить')
        layout = QVBoxLayout(central_widget)
        layout.addWidget(QLabel('Название жанра'))
        layout.addWidget(self.title)
        layout.addWidget(self.pushButton)
        layout.addStretch()

    def update_edit_window(self):
        self.title.setPlainText(self.parent.genresTable.item(self.parent.selected_items[0].row(), 1).text())

    def get_adding_verdict(self):
        try:
            if not self.title.toPlainText():
                raise ValueError
        except ValueError:
            return False
        con, cur = get_sql_connection()
        cur.execute('INSERT INTO genres (title) VALUES (?)', (self.title.toPlainText(),))
        con.commit()
        con.close()
        self.parent.update_genres()
        self.close()
        return True

    def get_editing_verdict(self):
        try:
            if not self.title.toPlainText():
                raise ValueError
        except ValueError:
            return False
        con, cur = get_sql_connection()
        cur.execute('UPDATE genres SET title = ? WHERE id = ?',
                    (self.title.toPlainText(), self.parent.ids[0]))
        con.commit()
        con.close()
        self.parent.update_genres()
        self.close()
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())