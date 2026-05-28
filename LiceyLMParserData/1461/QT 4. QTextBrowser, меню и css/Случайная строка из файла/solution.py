from PyQt6.QtWidgets import (QApplication, QWidget, QTextBrowser,
                             QVBoxLayout, QPushButton)
from random import choice


class RandomString(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайная строка")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout(self)
        self.button = QPushButton("Вывести", self)
        self.button.clicked.connect(self.load_random_string)
        layout.addWidget(self.button)
        self.textBrowser = QTextBrowser()
        layout.addWidget(self.textBrowser)

    def load_random_string(self):
        try:
            with open("lines.txt", "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
                if lines:
                    self.textBrowser.setHtml(f"<h1>{choice(lines).strip()}</h1>")
                    return
        except Exception:
            pass
        self.textBrowser.setHtml("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = RandomString()
    window.show()
    sys.exit(app.exec())