import csv
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QComboBox, 
    QPushButton, QTableWidgetItem, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QColor


class OlympResultWin(QWidget):
    def __init__(self):
        super().__init__()
        self.data = self.load_csv('rez.csv')
        self.classes_data = []
        self.schools_data = []
        self.school_classes = {}
        self.setup_window()

    def initUI(self):
        self.setWindowTitle("Результаты олимпиады: фильтрация")
        self.setMinimumSize(600, 600)
        main_layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        self.classes = QComboBox(self)
        self.schools = QComboBox(self)
        self.resultButton = QPushButton('Узнать результаты', self)
        top_layout.addWidget(self.classes)
        top_layout.addWidget(self.schools)
        top_layout.addWidget(self.resultButton)
        bottom_layout = QVBoxLayout()
        self.tableWidget = QTableWidget(self)
        bottom_layout.addWidget(self.tableWidget)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 9)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

    def setup_window(self):
        self.initUI()
        self.resultButton.clicked.connect(self.update_table)
        schools_set, classes_set = set(), set()
        for obj in self.data:
            log = obj.get('login', '').split('-')
            if len(log) >= 4:
                school = log[2]
                class_name = log[3]
                schools_set.add(school)
                classes_set.add(class_name)
                if school not in self.school_classes:
                    self.school_classes[school] = set()
                self.school_classes[school].add(class_name)
        self.schools_data = ['Все'] + sorted(schools_set)
        self.classes_data = ['Все'] + sorted(classes_set)
        self.schools.addItems(self.schools_data)
        self.classes.addItems(self.classes_data)
        self.schools.currentTextChanged.connect(self.update_classes_combo)

    def update_classes_combo(self, school):
        self.classes.clear()
        if school == 'Все':
            self.classes.addItems(self.classes_data)
        else:
            school_classes = sorted(self.school_classes.get(school, []))
            self.classes.addItems(['Все'] + school_classes)

    def load_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def update_table(self):
        selected_class, selected_school = self.classes.currentText(), self.schools.currentText()
        filtered_data = []
        for row in self.data:
            login_parts = row.get('login', '').split('-')
            if len(login_parts) >= 4:
                school_match = selected_school == 'Все' or login_parts[2] == selected_school
                class_match = selected_class == 'Все' or login_parts[3] == selected_class
                if school_match and class_match:
                    score_str = row.get('Score', '0')
                    score = int(score_str) if score_str.isdigit() else 0
                    name_parts = row.get('user_name', '').split()
                    last_name = name_parts[3] if len(name_parts) > 3 else ''
                    place_str = row.get('place', '')
                    if '-' in place_str:
                        place_min = int(place_str.split('-')[0])
                        place_max = int(place_str.split('-')[1])
                    else:
                        place_min = int(place_str) if place_str.isdigit() else 999
                        place_max = place_min
                    filtered_data.append((score, place_min, place_max, last_name, row.get('login')))
        filtered_data.sort(key=lambda x: (-x[0], x[1], x[2]))
        scores = sorted(set(map(lambda x: x[0], filtered_data)), reverse=True)

        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(filtered_data))
        self.tableWidget.setHorizontalHeaderLabels(['Фамилия', 'Результат', 'Логин'])
        place_colors = {1: QColor('#CCCC00'), 2: QColor('#B5B5BD'), 3: QColor('#9C5221')}
        for i, (score, place_min, place_max, last_name, login) in enumerate(filtered_data):
            items = [QTableWidgetItem(last_name), QTableWidgetItem(str(score)), QTableWidgetItem(login)]
            place = scores.index(score) + 1
            if place in [1, 2, 3]:
                for item in items:
                    item.setBackground(place_colors[place])
            for j, item in enumerate(items):
                self.tableWidget.setItem(i, j, item)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = OlympResultWin()
    window.show()
    sys.exit(app.exec())