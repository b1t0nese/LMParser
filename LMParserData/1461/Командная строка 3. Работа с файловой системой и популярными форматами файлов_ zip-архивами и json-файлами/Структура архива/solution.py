from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    paths = myzip.namelist()
    for path in paths:
        otstup = "  " * path.count("/")
        if path.endswith("/"):
            print(f"{otstup[:-2]}{path.split("/")[-2]}")
        else:
            print(f"{otstup}{path.split("/")[-1]}")