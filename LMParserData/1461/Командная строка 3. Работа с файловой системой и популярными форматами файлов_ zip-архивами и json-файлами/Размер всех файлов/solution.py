import os


def human_read_format(size):
    for format in ["Б", "КБ", "МБ", "ГБ", "ТБ"]:
        output = f"{round(size)}{format}"
        size /= 1024
        if size < 1:
            break
    return output


def get_files_sizes():
    dir = os.path.dirname(__file__)
    paths = filter(lambda i: os.path.isfile(os.path.join(dir, i)), os.listdir(dir))
    output = [f"{p} {human_read_format(os.path.getsize(p))}" for p in paths]
    return str("\n".join(output))


if __name__ == "__main__":
    print(get_files_sizes())