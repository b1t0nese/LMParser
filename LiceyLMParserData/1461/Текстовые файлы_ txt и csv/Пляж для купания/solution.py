import csv

with open("beaches.csv", "r", encoding="utf-8") as f:
    for beach in csv.DictReader(f, delimiter=";"):
        if (
            beach["rescuers"] == beach["equipped"] == "1"
            and float(beach["pollution"]) <= 0.5
            and int(beach["temperature"]) >= 18
        ):
            print(beach["beach"])