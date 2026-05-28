import os


def human_read_format(size):
    for format in ["Б", "КБ", "МБ", "ГБ", "ТБ"]:
        output = f"{round(size)}{format}"
        size /= 1024
        if size < 1:
            break
    return output


def get_size(path):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            try:
                total += get_size(entry.path)
            except Exception:
                continue
    return total


def main():
    path = input("Введите путь (по умолчанию C:\\\\): ").strip()
    if not os.path.isdir(path):
        path = "C:\\\\"

    dir_sizes = []
    for root, dirs, files in os.walk(path):
        for dir_name in dirs + files:
            dir_path = os.path.join(root, dir_name)
            try:
                size = get_size(dir_path)
                dir_sizes.append((dir_path, size))
            except Exception:
                continue
    dir_sizes.sort(key=lambda x: x[1], reverse=True)

    for i, (dir_path, size) in enumerate(dir_sizes[:10], 1):
        print(f"{os.path.basename(dir_path).ljust(50)} - {human_read_format(size)}")


if __name__ == "__main__":
    main()