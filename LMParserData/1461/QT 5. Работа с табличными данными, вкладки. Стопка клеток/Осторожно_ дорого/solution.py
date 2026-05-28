from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QHeaderView, QTableWidget, QTableWidgetItem,
                             QLineEdit, QPushButton)
import random
import csv


class Expensive(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Интерактивный чек")
        self.setFixedSize(300, 430)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setFixedSize(300, 400)
        self.tableWidget.setSortingEnabled(True)
        self.updateButton = QPushButton("Обновить", self)
        self.updateButton.clicked.connect(self.open_csv)
        self.updateButton.move(0, 400)
        out_text = QLabel("Итого: ", self)
        out_text.setMaximumSize(40, 30)
        out_text.move(160, 405)
        self.total = QLineEdit(self)
        self.total.setMaximumSize(100, 30)
        self.total.move(200, 400)

        self.open_csv()

    def open_csv(self):
        with open("price.csv", newline='', encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            rows = list(reader)
        if not rows:
            return
        rows = [rows[0] + ["Количество"]] + sorted(rows[1:], key=lambda x: int(x[1]), reverse=True)

        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(rows) - 1)
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.setHorizontalHeaderLabels(rows[0])
        self.tableWidget.cellChanged.connect(self.get_output)

        top_colors = [QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(5)]

        for r, row in enumerate(rows[1:]):
            for c, val in enumerate(row):
                item = QTableWidgetItem(val if val else "0")
                if val.isdigit():
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                if r < 5:
                    item.setBackground(top_colors[r])
                self.tableWidget.setItem(r, c, item)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

    def get_output(self):
        sum = 0
        for row in range(self.tableWidget.rowCount()):
            try:
                sum += int(self.tableWidget.item(row, 1).text()) * int(self.tableWidget.item(row, 2).text())
            except Exception:
                pass
        self.total.setText(str(sum))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Expensive()
    w.show()
    sys.exit(app.exec())