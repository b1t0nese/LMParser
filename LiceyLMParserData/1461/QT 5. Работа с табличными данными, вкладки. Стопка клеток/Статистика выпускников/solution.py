from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QTableWidget, QVBoxLayout,
    QHeaderView, QPushButton, QFileDialog, QTableWidgetItem, QWidget)
import csv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика выпускников")
        self.setGeometry(100, 100, 1000, 600)
        self.headers, self.rows = [], []
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.open_button = QPushButton("Открыть файл")
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)
        self.create_empty_tabs()

    def create_empty_tabs(self):
        data_widget = QWidget()
        data_layout = QVBoxLayout(data_widget)
        self.data_table = QTableWidget()
        data_layout.addWidget(self.data_table)
        self.tab_widget.addTab(data_widget, "Данные")

        count_widget = QWidget()
        count_layout = QVBoxLayout(count_widget)
        self.count_table = QTableWidget()
        count_layout.addWidget(self.count_table)
        self.tab_widget.addTab(count_widget, "Численность выпускников")

        match_widget = QWidget()
        match_layout = QVBoxLayout(match_widget)
        self.match_table = QTableWidget()
        match_layout.addWidget(self.match_table)
        self.tab_widget.addTab(match_widget, "Соответствует")

        no_match_widget = QWidget()
        no_match_layout = QVBoxLayout(no_match_widget)
        self.no_match_table = QTableWidget()
        no_match_layout.addWidget(self.no_match_table)
        self.tab_widget.addTab(no_match_widget, "Не соответствует")

    def open_file(self):
        file_path, ok = QFileDialog.getOpenFileName(
            self, "Открыть файл CSV", "", "CSV файлы (*.csv);;Все файлы (*)")
        if file_path:
            self.load_csv_data(file_path)
            self.update_tables()

    def load_csv_data(self, filename):
        self.headers, self.rows = [], []
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            self.headers = next(reader)
            for row in reader:
                if len(row) == len(self.headers):
                    self.rows.append(row)

    def update_tables(self):
        self.update_data_table()
        self.update_count_table()
        self.update_match_table()
        self.update_no_match_table()

    def update_data_table(self):
        self.data_table.clear()
        self.data_table.setColumnCount(len(self.headers))
        self.data_table.setRowCount(len(self.rows))
        self.data_table.setHorizontalHeaderLabels(self.headers)
        for r, row in enumerate(self.rows):
            for c, col in enumerate(row):
                self.data_table.setItem(r, c, QTableWidgetItem(col))
        self.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def update_count_table(self):
        self.count_table.clear()
        self.count_table.setColumnCount(2)
        self.count_table.setRowCount(len(self.rows))
        self.count_table.setHorizontalHeaderLabels(['Специальность', 'Численность выпускников, тыс. чел.'])
        for row_idx, row_data in enumerate(self.rows):
            self.count_table.setItem(row_idx, 0, QTableWidgetItem(row_data[0]))
            self.count_table.setItem(row_idx, 1, QTableWidgetItem(row_data[1]))
        self.count_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def update_match_table(self):
        self.match_table.clear()
        self.match_table.setColumnCount(3)
        self.match_table.setRowCount(len(self.rows))
        self.match_table.setHorizontalHeaderLabels([
            'Специальность', 'Соответствует, тыс. чел.', 'Соответствует, %'])
        for row_idx, row_data in enumerate(self.rows):
            self.match_table.setItem(row_idx, 0, QTableWidgetItem(row_data[0]))
            self.match_table.setItem(row_idx, 1, QTableWidgetItem(row_data[2]))
            self.match_table.setItem(row_idx, 2, QTableWidgetItem(row_data[4]))
        self.match_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def update_no_match_table(self):
        self.no_match_table.clear()
        self.no_match_table.setColumnCount(3)
        self.no_match_table.setRowCount(len(self.rows))
        self.no_match_table.setHorizontalHeaderLabels([
            'Специальность', 'Не соответствует, тыс. чел.', 'Не соответствует, %'])
        for row_idx, row_data in enumerate(self.rows):
            self.no_match_table.setItem(row_idx, 0, QTableWidgetItem(row_data[0]))
            self.no_match_table.setItem(row_idx, 1, QTableWidgetItem(row_data[3]))
            self.no_match_table.setItem(row_idx, 2, QTableWidgetItem(row_data[5]))
        self.no_match_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


def main():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()