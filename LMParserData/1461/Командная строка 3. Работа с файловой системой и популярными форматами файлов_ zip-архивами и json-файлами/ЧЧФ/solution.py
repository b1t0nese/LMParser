def human_read_format(size):
    for format in ["Б", "КБ", "МБ", "ГБ", "ТБ"]:
        output = f"{round(size)}{format}"
        size /= 1024
        if size < 1:
            break
    return output