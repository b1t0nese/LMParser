import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QRadioButton,
    QLabel,
    QGridLayout,
)


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.button_grid = [[], [], []]
        self.is_x = True
        self.first_x = True
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 400, 400)
        self.setWindowTitle("Крестики-Нолики")

        self.new_game_button = QPushButton("Заново", self)
        self.new_game_button.move(200, 0)
        self.new_game_button.clicked.connect(self.restart)

        self.x_radio = QRadioButton("X", self)
        self.x_radio.move(100, 0)
        self.x_radio.clicked.connect(
            lambda: self.restart() if not self.first_x else None
        )
        self.x_radio.setChecked(True)

        self.result = QLabel(self)
        self.result.move(150, 370)

        self.o_radio = QRadioButton("O", self)
        self.o_radio.move(140, 0)
        self.o_radio.clicked.connect(lambda: self.restart() if self.first_x else None)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(5)
        for i in range(9):
            new_button = QPushButton()
            new_button.setFixedSize(100, 100)
            new_button.clicked.connect(self.click)
            grid_layout.addWidget(new_button, i // 3, i % 3)
            self.button_grid[i // 3].append(new_button)
        self.setLayout(grid_layout)

    def restart(self):
        self.result.setText("")
        self.is_x = self.x_radio.isChecked()
        self.first_x = self.is_x
        for row in self.button_grid:
            for button in row:
                button.setText("")
                button.setEnabled(True)

    def win(self):
        for row in self.button_grid:
            for button in row:
                button.setEnabled(False)

    def click(self):
        button = self.sender()
        if button.text():
            return
        button.setText("X" if self.is_x else "O")
        self.is_x = not self.is_x
        self.check_game_state()

    def check_game_state(self):
        winner = self.get_winner()
        if winner:
            self.result.setText(f"Выиграл {winner}!")
            self.win()
        elif self.is_board_full():
            self.result.setText("Ничья!")
            self.win()

    def get_winner(self):
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for condition in win_conditions:
            cells = [self.button_grid[i][j] for i, j in condition]
            symbols = [cell.text() for cell in cells]
            if symbols[0] and symbols[0] == symbols[1] == symbols[2]:
                return symbols[0]

        return None

    def is_board_full(self):
        return all(button.text() for row in self.button_grid for button in row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec())