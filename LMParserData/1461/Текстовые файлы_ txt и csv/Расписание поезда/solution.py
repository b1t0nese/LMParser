import csv

speed = 60

with open("schedule.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        time = int(row["hour"]) + (int(row["minute"]) / 60)
        lenght = round(time * speed)
        print(f"{row["station"]}\t{lenght}")