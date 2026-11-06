from PyQt6.QtWidgets import QApplication, QFileDialog
from zipfile import ZipFile, ZIP_DEFLATED
import sys
import os


def make_reserve_arc(source: str, dest: str='archive.zip'):
    with ZipFile(dest, 'w', ZIP_DEFLATED, compresslevel=9) as zipf:
        for root, dirs, files in os.walk(source):
            for file in dirs + files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source))


def main():
    folder_path = QFileDialog.getExistingDirectory(
        None, "Выберите папку, которую хотите архивировать", "", QFileDialog.Option.ShowDirsOnly)
    if folder_path:
        zip_path, ok = QFileDialog.getSaveFileName(
            None, "Сохранить ZIP архив", "archive.zip", "ZIP архивы (*.zip);;Все файлы (*)")
        if zip_path and ok:
            if not zip_path.lower().endswith('.zip'):
                zip_path += '.zip'
            make_reserve_arc(folder_path, zip_path)
            os.startfile(zip_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec())