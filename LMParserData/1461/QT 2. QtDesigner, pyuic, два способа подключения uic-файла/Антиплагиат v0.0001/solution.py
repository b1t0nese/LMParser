from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QDoubleSpinBox,
    QPlainTextEdit, QPushButton, QLabel)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Антиплагиат")
        MainWindow.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        MainWindow.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        threshold_layout = QHBoxLayout()
        threshold_label = QLabel("Порог срабатывания (%):")
        self.alert_value = QDoubleSpinBox()
        self.alert_value.setRange(0.0, 100.0)
        self.alert_value.setValue(20.0)
        self.alert_value.setDecimals(2)
        self.alert_value.setSingleStep(0.5)

        threshold_layout.addWidget(threshold_label)
        threshold_layout.addWidget(self.alert_value)
        threshold_layout.addStretch()
        main_layout.addLayout(threshold_layout)

        text_layout = QHBoxLayout()

        text1_layout = QVBoxLayout()
        text1_label = QLabel("Текст 1:")
        self.text1 = QPlainTextEdit()
        self.text1.setPlaceholderText("Введите первый текст здесь...")
        text1_layout.addWidget(text1_label)
        text1_layout.addWidget(self.text1)

        text2_layout = QVBoxLayout()
        text2_label = QLabel("Текст 2:")
        self.text2 = QPlainTextEdit()
        self.text2.setPlaceholderText("Введите второй текст здесь...")
        text2_layout.addWidget(text2_label)
        text2_layout.addWidget(self.text2)

        text_layout.addLayout(text1_layout)
        text_layout.addLayout(text2_layout)
        main_layout.addLayout(text_layout)

        self.checkBtn = QPushButton("Проверить на плагиат")
        main_layout.addWidget(self.checkBtn)


class AntiPlagiarism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBtn.clicked.connect(self.check_plagiat)

    def calculate_similarity(self, text1, text2):
        unique_lines1 = set(text1.splitlines() if text1 else [''])
        unique_lines2 = set(text2.splitlines() if text2 else [''])
        total_unique_lines = len(unique_lines1.union(unique_lines2))
        if total_unique_lines == 0:
            return 0.0
        return (len(unique_lines1.intersection(unique_lines2)) / total_unique_lines) * 100

    def check_plagiat(self):
        similarity = self.calculate_similarity(self.text1.toPlainText(), self.text2.toPlainText())
        if similarity >= self.alert_value.value():
            message = f"Тексты похожи на {similarity:.2f}%, плагиат"
        else:
            message = f"Тексты похожи на {similarity:.2f}%, не плагиат"
        self.statusBar().showMessage(message)


if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    w = AntiPlagiarism()
    w.show()
    sys.exit(app.exec())