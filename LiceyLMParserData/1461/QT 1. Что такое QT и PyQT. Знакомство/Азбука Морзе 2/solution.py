from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
)
from PyQt6.QtCore import Qt
import sys


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.morse_code = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }

        self.create_alphabet_buttons()

    def initUI(self):
        self.setWindowTitle("Азбука Морзе")
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()

        self.result = QLineEdit()
        self.result.setReadOnly(True)
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result)

        self.buttons_layout = QGridLayout()
        main_layout.addLayout(self.buttons_layout)

        self.setLayout(main_layout)

        self.alphabet_buttons = {}

    def create_alphabet_buttons(self):
        for i, letter in enumerate(list(self.morse_code.keys())):
            button = QPushButton(letter)
            button.setFixedSize(40, 40)
            button.clicked.connect(lambda checked, ltr=letter: self.add_morse_code(ltr))
            self.buttons_layout.addWidget(button, i // 9, i % 9)
            self.alphabet_buttons[letter] = button

    def add_morse_code(self, letter):
        self.result.setText(self.result.text() + self.morse_code[letter])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())