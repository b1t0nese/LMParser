from collections import Counter

answers = []

with open("numbers.txt", "r") as f:
    for i, line in enumerate(f):
        numbers = list(map(int, line.split()))
        counts = Counter(numbers)
        clear_counts = list(map(lambda x: x[1], dict(counts).items()))
        if clear_counts.count(3) == 1 and clear_counts.count(1) == 3:
            unique_nums = [num for num, count in counts.items() if count == 1]
            repeating_number = next((num for num, count in counts.items() if count == 3))
            if sum(unique_nums) / len(unique_nums) >= repeating_number:
                if max(numbers) % min(numbers) != 0:
                    answers.append((i + 1, sum(numbers)))

answers.sort(key=lambda x: x[1])
print(answers[0][0])