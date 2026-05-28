from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLineEdit, QTextBrowser, QVBoxLayout)
import csv


class CatBreeds(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = self.load_csv('cat_breeds.csv')
        self.colors = ['Cornsilk', 'BlanchedAlmond', 'Bisque',
                       'NavajoWhite', 'Wheat', 'BurlyWood', 'Tan']
        self.color_index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Кошечки")
        self.setGeometry(100, 100, 400, 400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.write)
        main_layout.addWidget(self.lineEdit)
        self.textBrowser = QTextBrowser()
        main_layout.addWidget(self.textBrowser, stretch=1)

    def load_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            return [{k: v.strip() for k, v in row.items()} for row in reader]

    def write(self):
        self.textBrowser.clear()
        text = self.lineEdit.text().lower()
        found_cats = filter(lambda x: text in x['Breed'].lower(), self.data)
        self.color_index = 0
        for cat in list(found_cats):
            s = str((f'<b>{cat['Breed']}</b>, {cat['Location of origin']},',
                     f' {cat['Type']}, {cat['Body type']},',
                     f' {cat['Coat type and length']}, {cat['Coat pattern']}'))
            self.textBrowser.append(f'<p style="background: {
                self.colors[self.color_index % len(self.colors)]}">{s}</p>')
            self.color_index += 1


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CatBreeds()
    window.show()
    sys.exit(app.exec())