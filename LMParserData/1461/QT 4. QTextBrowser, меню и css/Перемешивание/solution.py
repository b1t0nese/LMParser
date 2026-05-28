from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser


class Shuffle(QWidget):
    def __init__(self):
        super().__init__()
        self.text = ''
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Перемешивание")
        self.setFixedSize(280, 400)
        self.button = QPushButton("Загрузить строки", self)
        self.button.move(0, 0)
        self.button.clicked.connect(self.load_strings)
        self.text_field = QTextBrowser(self)
        self.text_field.setGeometry(0, 25, 280, 375)

    def load_strings(self):
        with open("lines.txt", "r", encoding="utf-8") as f:
            self.text_field.clear()
            lines = f.read().splitlines()
            for i in range(1, -1, -1):
                for j in range(i, len(lines), 2):
                    self.text_field.insertPlainText(lines[j] + "\n")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Shuffle()
    window.show()
    sys.exit(app.exec())