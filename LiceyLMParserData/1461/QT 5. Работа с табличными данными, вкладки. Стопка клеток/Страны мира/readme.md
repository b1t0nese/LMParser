# Страны мира

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64 Мб

В файле [countries.csv](https://yastatic.net/s3/lyceum/files/753cb9ff-c526-44f0-a85f-998e91342605/upload.csv) содержится информация обо всех странах мира. Напишите приложение на PyQt для наглядного отображения этих данных. При запуске программа должна загрузить содержимое файла `countries.csv`.

Основное окно приложения представляет собой набор вкладок (`QTabWidget`). Вместо вывода всех данных в одной громоздкой таблице, информация должна быть разделена. Для **каждой характеристики** страны (такой, как "Region", "Capital", "Official languages" и так далее) создается **отдельная вкладка**. Название каждой вкладки должно соответствовать названию характеристики.

Содержимым каждой вкладки является простая таблица из двух столбцов: первый столбец — **"Country"**, а второй — **значение той характеристики, которой посвящена вкладка**. Например, на вкладке "Capital" будет таблица со столбцами "Country" и "Capital". Все таблицы должны использовать единую модель данных `CsvTableModel` и автоматически растягивать столбцы по ширине окна.

Если файл `countries.csv` не будет найден, для демонстрации работы должны использоваться встроенные тестовые данные.

При решении используйте шаблон класса окна и класс модели; имена виджетов и методов класса не меняйте. Вся логика решения описана в комментариях, реализуйте её вместо многоточий.

 **Шаблон кода решения**

```
import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QTableView,
                             QVBoxLayout, QWidget, QHeaderView)
from PyQt6.QtCore import Qt, QVariant, QAbstractTableModel, QModelIndex
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Данные о странах")
        self.setGeometry(100, 100, 1000, 600)

        # Центральный виджет и основной layout
        central_widget = QWidget()
        ...
        layout = ...

        # Создаем виджет с вкладками
        self.tab_widget = ...
        ...

        # Загружаем данные из CSV
        self.headers, self.rows = ...

        # Создаем вкладки для каждой характеристики
        self.create_tabs()

    def load_csv_data(self, filename):
        """Загрузка данных из CSV файла"""
        headers = []
        rows = []
        try:
            ...
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            # Создаем тестовые данные для демонстрации
            headers = ["Country", "Region", "Capital", "Official languages",
                       "Area, km 2", "Population, ppl.",
                       "Population density, ppl./km2", "International phone code"]
            rows = [
                ["Russia", "Europe/Asia", "Moscow", "Russian", "17098242", "146780720", "8.4", "+7"],
                ["Germany", "Europe", "Berlin", "German", "357022", "83149300", "232", "+49"],
                ["France", "Europe", "Paris", "French", "551695", "67390000", "122", "+33"]
            ]

        return headers, rows

    def create_tabs(self):
        """Создание вкладок для каждой характеристики"""
        # Индексы столбцов для отображения (кроме Country)
        ...

    def create_full_data_tab(self):
        """Создание вкладки со всеми данными (опционально)"""
        full_model = CsvTableModel(self.headers, self.rows)
        full_table = QTableView()
        ...

# Класс модели
class CsvTableModel(QAbstractTableModel):
    def __init__(self, headers=None, rows=None, parent=None):
        super().__init__(parent)
        self._headers = headers or []
        self._rows = rows or []

    def rowCount(self, parent=None):
        return len(self._rows)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return str(self._rows[index.row()][index.column()])
        return QVariant()

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if orientation == Qt.Orientation.Horizontal and 0 <= section < len(self._headers):
            return self._headers[section]
        return str(section + 1)

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled
        return (Qt.ItemFlag.ItemIsSelectable |
                Qt.ItemFlag.ItemIsEnabled |
                Qt.ItemFlag.ItemIsEditable)

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole and index.isValid():
            self._rows[index.row()][index.column()] = str(value)
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def insertRows(self, row, count, parent=None):
        self.beginInsertRows(parent or QModelIndex(), row, row + count - 1)
        for _ in range(count):
            self._rows.insert(row, [""] * len(self._headers))
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=None):
        self.beginRemoveRows(parent or QModelIndex(), row, row + count - 1)
        for _ in range(count):
            self._rows.pop(row)
        self.endRemoveRows()
        return True

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
**Максимальный балл:** 34  
**Полученный балл:** 34  
**Статус:** accepted  
**Дата:** 2026-01-07T15:19:15.053320+03:00  
**Контест:** 80823  
**Вердикт:** ok  