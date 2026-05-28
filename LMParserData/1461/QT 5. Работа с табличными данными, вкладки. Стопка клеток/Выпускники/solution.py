import csv

procent = int(input())

with open("vps.csv", "r", encoding="utf-8", newline="") as f:
    vipuskniki = csv.DictReader(f, delimiter=";")
    for specialitet in vipuskniki:
        if int(specialitet["соответствует в %"]) >= procent:
            print(specialitet["Специальность"])