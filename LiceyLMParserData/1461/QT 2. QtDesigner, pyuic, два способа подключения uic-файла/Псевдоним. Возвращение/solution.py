from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLCDNumber, QSpinBox, QPushButton, QListWidget, QLabel, QLineEdit
)
from PyQt6.QtCore import Qt


class MainWindowUI(QWidget):
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.remainLcd = QLCDNumber()
        self.remainLcd.setDigitCount(4)
        self.remainLcd.display(0)
        main_layout.addWidget(self.remainLcd)

        self.resultLabel = QLabel("")
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.resultLabel)

        stones_layout = QHBoxLayout()
        stones_layout.addWidget(QLabel("Начальное количество камней:"))
        self.stones = QSpinBox()
        self.stones.setMinimum(1)
        self.stones.setMaximum(1000)
        self.stones.setValue(20)
        stones_layout.addWidget(self.stones)
        main_layout.addLayout(stones_layout)

        self.startButton = QPushButton("Новая игра")
        self.startButton.clicked.connect(self.start_new_game)
        main_layout.addWidget(self.startButton)

        take_layout = QHBoxLayout()
        take_layout.addWidget(QLabel("Взять камней (1-3):"))
        self.takeInput = QLineEdit("")
        take_layout.addWidget(self.takeInput)
        self.takeButton = QPushButton("Взять")
        self.takeButton.clicked.connect(self.take_stones)
        take_layout.addWidget(self.takeButton)
        main_layout.addLayout(take_layout)

        self.listWidget = QListWidget()
        main_layout.addWidget(self.listWidget)

        self.setWindowTitle("Псевдоним")
        self.setGeometry(100, 100, 400, 500)


class Pseudonym(QMainWindow, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.current_stones = 0
        self.game_active = False
        self.initUI()

    def start_new_game(self):
        self.current_stones = self.stones.value()
        self.remainLcd.display(self.current_stones)
        self.listWidget.clear()
        self.resultLabel.clear()
        self.game_active = True
        self.takeButton.setEnabled(True)

    def take_stones(self):
        if not self.game_active:
            return

        user_take = int(self.takeInput.text())
        if user_take < 1 or user_take > 3 or user_take > self.current_stones:
            return
        self.current_stones -= user_take
        self.remainLcd.display(self.current_stones)
        self.add_to_history(f"Игрок взял - {user_take}")
        if self.current_stones == 0:
            self.resultLabel.setText("Победа пользователя!")
            self.game_active = False
            self.takeButton.setEnabled(False)
            return

        self.takeButton.setEnabled(False)
        if self.current_stones % 4 == 0:
            computer_take = 1
        else:
            computer_take = self.current_stones % 4
        if computer_take > 3:
            computer_take = 1
        if computer_take > self.current_stones:
            computer_take = self.current_stones
        self.current_stones -= computer_take
        self.remainLcd.display(self.current_stones)
        self.add_to_history(f"Компьютер взял - {computer_take}")
        if self.current_stones == 0:
            self.resultLabel.setText("Победа компьютера!")
            self.game_active = False
            return
        self.takeButton.setEnabled(True)

    def add_to_history(self, message):
        self.listWidget.addItem(message)
        self.listWidget.scrollToBottom()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Pseudonym()
    window.show()
    sys.exit(app.exec())