from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QTextBrowser, QLineEdit, QVBoxLayout, QHBoxLayout)


dark_style = """
QMainWindow {background-color: #2b2b2b;}
QTextBrowser {
    background-color: #1e1e1e;
    color: #d4d4d4;
    border: 1px solid #3e3e3e;
    border-radius: 5px;
}
QLineEdit {
    background-color: #3c3c3c;
    color: #d4d4d4;
    border: 1px solid #3e3e3e;
    border-radius: 5px;
    padding: 10px 15px;
}
QPushButton {
    background-color: #0078d4;
    color: white;
    border-radius: 5px;
    padding: 10px 15px;
}
QPushButton:pressed {background-color: #006cbd;}
QPushButton:hover {background-color: #1083e0;}"""

light_style = """
QMainWindow {background-color: #f5f5f5;}
QTextBrowser {
    background-color: white;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 5px;
}
QLineEdit {
    background-color: white;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 5px;
    padding: 10px 15px;
}
QPushButton {
    background-color: #0078d4;
    color: white;
    border-radius: 5px;
    padding: 10px 15px;
}
QPushButton:pressed {background-color: #006cbd;}
QPushButton:hover {background-color: #1083e0;}"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_dark_theme = True
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Приложение со стилем")
        self.setFixedSize(700, 550)

        self.textBrowser = QTextBrowser()
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Введите сообщение...")
        self.lineEdit.returnPressed.connect(self.send_message)

        self.pushButton = QPushButton("Отправить")
        self.pushButton.clicked.connect(self.send_message)
        self.pushButton1 = QPushButton("Светлая тема")
        self.pushButton1.clicked.connect(self.change_theme)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        main_layout.addWidget(self.textBrowser)
        main_layout.addWidget(self.lineEdit)

        buttons = QHBoxLayout()
        buttons.addWidget(self.pushButton)
        buttons.addWidget(self.pushButton1)
        main_layout.addLayout(buttons)

        self.setStyleSheet(dark_style)
        self.pushButton1.setText("Светлая тема")

    def send_message(self):
        if self.lineEdit.text():
            self.textBrowser.append(f"<b>Message:</b> {self.lineEdit.text()}")
            self.lineEdit.clear()

    def change_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        self.setStyleSheet(dark_style if self.is_dark_theme else light_style)
        self.pushButton1.setText("Светлая тема" if self.is_dark_theme else "Тёмная тема")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())