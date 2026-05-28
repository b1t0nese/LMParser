import csv
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem,
    QLabel, QLineEdit, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QColor


class TitanicSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.data = self.load_csv('titanic.csv')
        self.setup_window()

    def initUI(self):
        self.setWindowTitle("Поиск на Титанике")
        self.setMinimumSize(800, 700)
        main_layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        label = QLabel('Поиск: ', self)
        self.searchEdit = QLineEdit(self)
        top_layout.addWidget(label)
        top_layout.addWidget(self.searchEdit)
        top_layout.addStretch()
        bottom_layout = QVBoxLayout()
        self.resultTable = QTableWidget(self)
        bottom_layout.addWidget(self.resultTable)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 9)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

    def setup_window(self):
        self.initUI()
        self.searchEdit.textChanged.connect(self.update_table)
        self.update_table()

    def load_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return list(csv.reader(f))

    def update_table(self):
        local_data, search_text = self.data.copy()[1:], self.searchEdit.text()
        if len(search_text) >= 3:
            local_data = list(filter(lambda x: search_text.lower() in x[1].lower(), local_data))
        self.resultTable.clear()
        self.resultTable.setColumnCount(len(self.data[0]))
        self.resultTable.setRowCount(len(local_data))
        self.resultTable.setHorizontalHeaderLabels(self.data[0])
        for i, row in enumerate(local_data):
            for j, col in enumerate(row):
                col_item = QTableWidgetItem(col)
                col_item.setBackground(QColor(["#FF0000", "#00FF00"][int(row[5])]))
                self.resultTable.setItem(i, j, col_item)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TitanicSearch()
    window.show()
    sys.exit(app.exec())