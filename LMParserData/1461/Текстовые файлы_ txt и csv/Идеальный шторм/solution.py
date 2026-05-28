from collections import Counter
import csv

clear_storm, yes_waves = [], []
with open("storm.csv", "r") as f:
    storm = csv.reader(f)
    for line in storm:
        numbers = list(map(int, line))
        clear_storm.append(numbers)

max_gorb = max([max(numbers) for numbers in clear_storm])
for i, numbers in enumerate(clear_storm):
    counts = Counter(numbers)
    clear_counts = list(map(lambda x: x[1], dict(counts).items()))
    if clear_counts.count(2) == 1 and clear_counts.count(1) == len(clear_counts) - 1:
        if len([num for num in numbers if str(num)[-1] == str(max_gorb)[-1]]) >= 1:
            if len([num for num in numbers if num % 2 == 0]) >= 3:
                yes_waves.append(numbers)

print(len(yes_waves), min([min(numbers) for numbers in yes_waves]))