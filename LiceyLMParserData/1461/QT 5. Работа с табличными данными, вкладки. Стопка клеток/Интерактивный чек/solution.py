import csv

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QTableWidget, QTableWidgetItem, QLineEdit)
from PyQt6.QtWidgets import QHeaderView


class InteractiveReceipt(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Интерактивный чек")
        self.setFixedSize(300, 430)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setFixedSize(300, 400)
        self.tableWidget.setSortingEnabled(True)
        out_text = QLabel("Итого: ", self)
        out_text.setMaximumSize(40, 30)
        out_text.move(0, 400)
        self.total = QLineEdit(self)
        self.total.setMaximumSize(150, 30)
        self.total.move(45, 400)

        self.open_csv()

    def open_csv(self):
        with open("price.csv", newline='', encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            rows = list(reader)
        if not rows:
            return
        rows[0] += ["Количество"]

        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(rows) - 1)
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.setHorizontalHeaderLabels(rows[0])
        self.tableWidget.cellChanged.connect(self.get_output)

        for r, row in enumerate(rows[1:]):
            for c, val in enumerate(row):
                item = QTableWidgetItem(val if val else "0")
                if val.isdigit():
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
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
    app = QApplication([])
    w = InteractiveReceipt()
    w.resize(900, 600)
    w.show()
    app.exec()