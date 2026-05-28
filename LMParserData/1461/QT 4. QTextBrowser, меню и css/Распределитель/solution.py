from PyQt6.QtWidgets import QMainWindow, QApplication, QTextBrowser, QFileDialog


class Distributor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_text = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Распределитель файлов")
        self.setGeometry(100, 100, 800, 600)
        self.text_browser = QTextBrowser()
        self.setCentralWidget(self.text_browser)
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        open_action = file_menu.addAction("Открыть")
        open_action.triggered.connect(self.load_file)
        save_action = file_menu.addAction("Сохранить")
        save_action.triggered.connect(self.save_file)
        spread_menu = menubar.addMenu("Распределить")
        extensions = ["TXT", "CSV", "PNG", "PY", "Другие"]
        for ext in extensions:
            action = spread_menu.addAction(ext)
            action.triggered.connect(lambda checked, e=ext: self.spread(e.lower()))
    
    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.current_text = file.read()
                self.text_browser.setPlainText(self.current_text)
    
    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_browser.toPlainText())

    def spread(self, ext="другие"):
        files = filter(lambda f: f.endswith(f'.{ext}') or (
            ext == "другие" and not f.endswith(('.txt', '.csv', '.png', '.py'))
        ), self.current_text.split("\n"))
        self.text_browser.setPlainText('\n'.join(sorted(files)))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Distributor()
    window.show()
    sys.exit(app.exec())