from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QHBoxLayout, QTextEdit, QPushButton,
    QVBoxLayout, QWidget, QStatusBar,
    QMessageBox, QTableWidgetItem)
import sqlite3
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("films_db.sqlite")
        self.films = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Генерация фильмов")
        self.setGeometry(100, 100, 500, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        top_layout = QHBoxLayout()

        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(100)
        top_layout.addWidget(self.textEdit, stretch=3)

        self.pushButton = QPushButton("Запуск")
        self.pushButton.setFixedSize(self.pushButton.sizeHint())
        self.pushButton.clicked.connect(self.start)
        top_layout.addWidget(self.pushButton)
        top_layout.addSpacing(10)

        self.saveButton = QPushButton("Изменить")
        self.saveButton.setFixedSize(self.saveButton.sizeHint())
        self.saveButton.clicked.connect(self.edit)
        top_layout.addWidget(self.saveButton)

        main_layout.addLayout(top_layout)

        self.tableWidget = QTableWidget()
        main_layout.addWidget(self.tableWidget, stretch=1)

        main_layout.setStretch(0, 0)
        main_layout.setStretch(1, 1)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("")

    def start(self):
        text = self.textEdit.toPlainText().strip()
        self.films = []
        if text:
            try:
                if '=' in text or '>' in text or '<' in text:
                    operator = None
                    for op in ['=', '>', '<']:
                        if op in text:
                            operator = op
                            break
                    if operator:
                        field, value = text.split(operator, 1)
                        if field not in ['id', 'title', 'year', 'genre', 'duration']:
                            self.statusbar.showMessage("Некорректное поле в запросе")
                            return
                        if field in ['id', 'year', 'duration']:
                            if value.isdigit():
                                value = int(value)
                        query = f"SELECT * FROM films WHERE {field} {operator} ?"
                        params = (value,)
                    else:
                        self.statusbar.showMessage("Некорректный запрос")
                        return
                elif text.isdigit():
                    query = "SELECT * FROM films WHERE id = ?"
                    params = (int(text),)
                else:
                    query = "SELECT * FROM films WHERE title LIKE ?"
                    params = (f'%{text}%',)
                self.films = self.con.cursor().execute(query, params).fetchall()
            except Exception:
                self.statusbar.showMessage("Некорректный запрос")
                self.films = []
        else:
            self.films = self.con.cursor().execute("SELECT * FROM films").fetchall()
        self.tableWidget.clear()
        if not self.films:
            self.statusbar.showMessage("По этому запросу ничего не найдено")
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
        else:
            self.statusbar.showMessage("")
            self.tableWidget.setColumnCount(len(self.films[0]))
            self.tableWidget.setRowCount(len(self.films))
            for i, film in enumerate(self.films):
                for j, item in enumerate(film):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))

    def edit(self):
        selected_row = self.tableWidget.currentRow()
        if not self.films or selected_row >= len(self.films):
            self.statusbar.showMessage("Нет данных для изменения")
            return
        selected_film = self.films[selected_row]
        film_id = selected_film[0]
        reply = QMessageBox.question(self, "Подтверждение", f"Вы действительно хотите изменить фильм с id={film_id}?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            cur = self.con.cursor()
            cur.execute(
                "UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?",
                (selected_film[1][::-1], selected_film[2] + 1000, selected_film[3], selected_film[4] * 2, film_id))
            self.con.commit()
            self.statusbar.showMessage(f"Фильм с id={film_id} успешно изменен")
            self.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())