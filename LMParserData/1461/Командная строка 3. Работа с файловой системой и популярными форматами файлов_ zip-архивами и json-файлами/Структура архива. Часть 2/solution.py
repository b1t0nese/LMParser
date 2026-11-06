from zipfile import ZipFile


def HRF(size):
    for format in ["Б", "КБ", "МБ", "ГБ", "ТБ"]:
        output = f"{round(size)}{format}"
        size /= 1024
        if size < 1:
            break
    return output


with ZipFile('input.zip') as myzip:
    paths = myzip.namelist()
    for path in paths:
        otstup = "  " * path.count("/")
        if path.endswith("/"):
            print(f"{otstup[:-2]}{path.split("/")[-2]}")
        else:
            print(f"{otstup}{path.split("/")[-1]} {HRF(myzip.getinfo(path).file_size)}")