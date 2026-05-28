import csv

hole_structure = {
    "no": "",
    "kilometer": "",
    "stripe": "",
    "area": "",
    "depth": "",
    "priority": "",
}

control_int, n = int(input()), int(input())

with open("holes.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, delimiter=";", fieldnames=hole_structure.keys())
    writer.writeheader()

    for i in range(1, n + 1):
        yama = input().split()
        hole_data = hole_structure.copy()
        (
            hole_data["no"],
            hole_data["kilometer"],
            hole_data["stripe"],
            hole_data["area"],
            hole_data["depth"],
        ) = (i, *yama)
        hole_data["priority"] = 1 if int(yama[2]) * int(yama[3]) > control_int else 0
        writer.writerow(hole_data)