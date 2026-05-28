# Страны мира в стеке

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64 Мб

В файле (для отладки можно использовать [файл](https://yastatic.net/s3/lyceum/files/cd6ca088-769d-430e-be55-8ad421b661d8/upload.csv)) содержится информация обо всех странах мира. Напишите приложение, использующее модель QAbstractTableModel, на нескольких страницах стека выводящих страны и одну из характеристик из файла.

В меню Файл должны быть два пункта: *Открыть* и *Выход*.

На первой странице стека при загрузке приложения появляется надпись: *Откройте файл через меню Файл -> Открыть.*

Открывается файл через диалоговое окно.

Вверху окна расположен `QComboBox`, в котором можно выбирать страницу из стека (названия страниц совпадают с названиями полей в файле. На первой странице при загрузке файла отображается таблица с первой по счёту характеристикой.

При решении используйте шаблон класса окна и класс модели; имена виджетов и методов класса не меняйте. Вся логика решения описана в комментариях, реализуйте её вместо многоточий.

**Шаблон кода решения**

```
import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QTableView,
                             QVBoxLayout, QWidget, QHeaderView,
                             QFileDialog, QComboBox, QHBoxLayout, QLabel, QSizePolicy)
from PyQt6.QtCore import Qt, QVariant, QModelIndex, QAbstractTableModel
from PyQt6.QtGui import QAction, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Данные о странах")
        self.setGeometry(100, 100, 1000, 600)

        self.headers = []
        self.rows = []

        # Центральный виджет и основной layout
        central_widget = QWidget()
        ...
        main_layout = ...

        # Создаём панель выбора страницы
        self.selection_layout = QHBoxLayout()
        self.selection_label = QLabel("Выберите характеристику:")
        self.page_combo = QComboBox()
        ...

        # Создаём стек виджетов
        self.stack_widget = ...

        # Создаём меню
        self.create_menu()

        # Инициализируем пустые страницы
        self.init_empty_pages()

    def create_menu(self):
        """Создание меню"""
        menubar = self.menuBar()

        # Меню Файл
        file_menu = ...

        open_action = ...
        ...

        exit_action = ...
        ...

    def init_empty_pages(self):
        """Инициализация пустых страниц при запуске"""
        empty_label = QLabel("Откройте файл через меню 'Файл → Открыть'")
        ...

        empty_widget = QWidget()
        ...

    def open_file(self):
        """Открытие CSV файла"""
        file_path, _ = QFileDialog.getOpenFileName(
            ...
        )

        if file_path:
            self.load_csv_data(file_path)

    def load_csv_data(self, filename):
        """Загрузка данных из CSV файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                ...

            self.create_pages()

        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def create_pages(self):
        """Создание страниц для каждой характеристики"""
        # Очищаем предыдущие данные
        ...

        self.page_combo.clear()

        # Создаём страницы для каждой характеристики (кроме Country)
        characteristic_columns = [1, 2, 3, 4, 5, 6, 7]  # Region, Capital, etc.

        ...

        # Показываем первую страницу
        if self.stack_widget.count() > 0:
            ...

    def change_page(self, index):
        """Переключение между страницами"""
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
            return self._rows[index.row()][index.column()]
        return QVariant()

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        if orientation == Qt.Orientation.Horizontal and 0 <= section < len(self._headers):
            return self._headers[section]
        return section + 1

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
**Дата:** 2026-01-07T16:04:28.984902+03:00  
**Контест:** 80823  
**Вердикт:** ok  