import csv


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


start, end = int(input()), int(input())

with open("divisors.csv", "w", newline="") as f:
    divisors = csv.writer(f, delimiter=" ")
    divisors.writerow(["number"] + [f"div{i}" for i in range(1, 6)])

    for i in range(start, end + 1):
        row = []

        for j in range(2, i + 1):
            if i % j == 0 and is_prime(j):
                row.append(j)
                if len(row) == 5:
                    break

        divisors.writerow([i] + row)