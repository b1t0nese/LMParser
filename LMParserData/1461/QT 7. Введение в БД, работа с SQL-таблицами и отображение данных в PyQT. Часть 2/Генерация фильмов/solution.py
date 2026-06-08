import sqlite3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QHBoxLayout, QTableWidgetItem, 
                             QTextEdit, QPushButton, QVBoxLayout, QWidget, QStatusBar, QMessageBox)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("films_db.sqlite")
        self.films = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("eq")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        top_layout = QHBoxLayout()

        self.textEdit = QTextEdit()
        top_layout.addWidget(self.textEdit, stretch=3)

        self.pushButton = QPushButton("Запуск")
        self.pushButton.clicked.connect(self.start)
        top_layout.addWidget(self.pushButton)

        self.saveButton = QPushButton("Изменить")
        self.saveButton.clicked.connect(self.edit)
        top_layout.addWidget(self.saveButton)

        main_layout.addLayout(top_layout)

        self.tableWidget = QTableWidget()
        main_layout.addWidget(self.tableWidget, stretch=1)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

    def start(self):
        text = self.textEdit.toPlainText().strip()

        if text:
            try:
                if "=" in text:
                    p = text.split("=")
                    f = p[0].strip()
                    v = p[1].strip()
                    if v.isdigit():
                        query = f"SELECT * FROM films WHERE {f} = ?"
                        params = (int(v),)
                    else:
                        query = f"SELECT * FROM films WHERE {f} = ?"
                        params = (v,)
                elif ">" in text:
                    p = text.split(">")
                    f = p[0].strip()
                    v = p[1].strip()
                    if v.isdigit():
                        query = f"SELECT * FROM films WHERE {f} > ?"
                        params = (int(v),)
                    else:
                        query = f"SELECT * FROM films WHERE {f} > ?"
                        params = (v,)
                elif "<" in text:
                    p = text.split("<")
                    f = p[0].strip()
                    v = p[1].strip()
                    if v.isdigit():
                        query = f"SELECT * FROM films WHERE {f} < ?"
                        params = (int(v),)
                    else:
                        query = f"SELECT * FROM films WHERE {f} < ?"
                        params = (v,)
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

            for i, obj1 in enumerate(self.films):
                for j, obj2 in enumerate(obj1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(obj2)))

    def edit(self):
        sr = self.tableWidget.currentRow()
        if not self.films or sr >= len(self.films):
            self.statusbar.showMessage("Нет данных для изменения")
            return
        
        sf = self.films[sr]
        fi = sf[0]
        r = QMessageBox.question(self, "Подтверждение", f"Вы действительно хотите изменить фильм с id={fi}?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if r == QMessageBox.StandardButton.Yes:
            nt = sf[1][::-1]
            ny = sf[2] + 1000
            ng = sf[3]
            nd = sf[4] * 2
            cur = self.con.cursor()
            cur.execute("""UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?""",
                        (nt, ny, ng, nd, fi))
            self.con.commit()
            cur.close()
            self.statusbar.showMessage(f"Фильм с id={fi} успешно изменен")
            self.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())