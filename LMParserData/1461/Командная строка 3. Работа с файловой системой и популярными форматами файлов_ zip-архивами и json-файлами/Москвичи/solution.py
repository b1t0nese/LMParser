from zipfile import ZipFile
import json

moscvichi = 0
with ZipFile('input.zip') as myzip:
    json_paths = filter(lambda x: x.endswith(".json"), myzip.namelist())
    for path in json_paths:
        with myzip.open(path, 'r') as file:
            people = json.load(file)
            if people["city"] == "Москва" or people["city"] == "Moscow":
                moscvichi += 1
print(moscvichi)