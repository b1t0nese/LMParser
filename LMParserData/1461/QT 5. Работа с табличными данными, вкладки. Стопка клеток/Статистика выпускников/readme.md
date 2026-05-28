# Статистика выпускников

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64 Мб

Используя файл со сведениями и работе выпускников по полученной специальности (для отладки можно использовать [такой файл](https://assets.contest.yandex.net/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Fgw7gSGCFGgQ6cMV.c0HUlMx5aWIr_1IF6y86vXKYMicckVXPrCp6LZ08Fyt1uRF2PHA3Ts2fQqFPvnnBZfvHZchCVn9vy2XkZmdTV0JC8P1B1Gs.trXLrq4mcEAha42DyKOhvg)), напишите приложение на PyQT6 с несколькими вкладками. В основном окне на вкладке **Данные** разместите таблицу, отображающую данные из файла, который выбирается по нажатию на кнопку **Открыть файл** (возникает диалоговое окно для выбора файла).

Следующие вкладки имеют имена:

- Численность выпускников
- Соответствует
- Не соответствует

При решении используйте шаблон класса; имена виджетов и методов класса не меняйте. Вся логика решения описана в комментариях, реализуйте её вместо многоточий.

 **Шаблон кода решения**

```
import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QTableWidget,
                             QVBoxLayout, QWidget, QHeaderView, QPushButton,
                             QFileDialog, QMessageBox, QTableWidgetItem)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика выпускников")
        self.setGeometry(100, 100, 1000, 600)

        self.headers = []
        self.rows = []

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Кнопка открытия файла
        self.open_button = ...
        ...

        # Вкладки
        self.tab_widget = ...

        # Создаём пустые вкладки
        self.create_empty_tabs()

    def create_empty_tabs(self):
        """Создание пустых вкладок при запуске"""
        # Вкладка "Данные"
        data_widget = QWidget()
        data_layout = ...
        self.data_table = QTableWidget()
        ...

        # Вкладка "Численность выпускников"
        count_widget = QWidget()
        count_layout = ...
        self.count_table = QTableWidget()
        ...

        # Вкладка "Соответствует"
        match_widget = QWidget()
        match_layout = ...
        self.match_table = QTableWidget()
        ...

        # Вкладка "Не соответствует"
        no_match_widget = QWidget()
        no_match_layout = ...
        self.no_match_table = QTableWidget()
        ...

    def open_file(self):
        """Открытие файла"""
        file_path, _ = QFileDialog.getOpenFileName(
            ...
        )

        if file_path:
            try:
                self.load_csv_data(file_path)
                self.update_tables()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def load_csv_data(self, filename):
        """Загрузка данных из CSV файла"""
        self.headers = []
        self.rows = []

        ...

    def update_tables(self):
        """Обновление всех таблиц"""
        self.update_data_table()
        self.update_count_table()
        self.update_match_table()
        self.update_no_match_table()

    def update_data_table(self):
        """Обновление таблицы со всеми данными self.data_table"""
        ...

    def update_count_table(self):
        """Таблица с численностью выпускников self.count_table"""
        ...

    def update_match_table(self):
        """Таблица с соответствием специальности self.match_table"""
        ...

    def update_no_match_table(self):
        """Таблица с несоответствием специальности self.no_match_table"""
       ...

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```

---
## Информация о решении

**Урок:** QT 5. Работа с табличными данными, вкладки. Стопка клеток  
**Максимальный балл:** 25  
**Полученный балл:** 25  
**Статус:** accepted  
**Дата:** 2026-01-11T19:28:55.488688+03:00  
**Контест:** 80823  
**Вердикт:** ok  