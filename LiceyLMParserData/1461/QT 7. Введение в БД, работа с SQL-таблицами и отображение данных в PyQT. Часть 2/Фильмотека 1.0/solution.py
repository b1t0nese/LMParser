from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QLabel, QPlainTextEdit, QComboBox)
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
        self.setWindowTitle("Фильмотека")
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)
        self.addButton = QPushButton('Добавить фильм')
        self.addButton.clicked.connect(self.adding)
        layout.addWidget(self.addButton)
        self.update_result()

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()

    def update_result(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels([
            'ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])
        con, cur = get_sql_connection()
        result = reversed(cur.execute("""
SELECT films.id, films.title, films.year, genres.title, films.duration FROM films
INNER JOIN genres ON films.genre = genres.id ORDER BY films.id""").fetchall())
        con.close()
        for row, rdata in enumerate(result):
            self.tableWidget.insertRow(row)
            for col, cdata in enumerate(rdata):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(cdata)))


class AddWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.params = {}
        self.load_genres()

    def initUI(self):
        self.setWindowTitle('Добавление фильма')
        self.setGeometry(350, 250, 400, 300)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.title = QPlainTextEdit()
        self.year = QPlainTextEdit()
        self.duration = QPlainTextEdit()
        self.comboBox = QComboBox()
        self.pushButton = QPushButton('Сохранить')
        self.pushButton.clicked.connect(self.save_film)

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

    def load_genres(self):
        self.comboBox.clear()
        self.params.clear()
        con, cur = get_sql_connection()
        genres = cur.execute('SELECT id, title FROM genres ORDER BY title').fetchall()
        con.close()
        for id, name in genres:
            self.comboBox.addItem(name)
            self.params[name] = id
    
    def validate_input(self):
        if not self.title.toPlainText():
            return True
        if not self.year.toPlainText().isdigit():
            return True
        if int(self.year.toPlainText()) > 2025:
            return True
        if not self.duration.toPlainText().isdigit():
            return True
        if int(self.duration.toPlainText()) <= 0:
            return True
        return False

    def get_adding_verdict(self):
        if not self.validate_input():
            con, cur = get_sql_connection()
            cur.execute("""INSERT INTO films (title, year, duration, genre)
            VALUES (?, ?, ?, ?)""", (
                self.title.toPlainText(), int(self.year.toPlainText()),
                int(self.duration.toPlainText()), self.params.get(self.comboBox.currentText())))
            con.commit()
            con.close()
            return True
        return False

    def save_film(self):
        if self.get_adding_verdict():
            if self.parent():
                self.parent().update_result()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())