with open("input.txt", "r", encoding="utf-8") as f:
    count = 0
    for line in f:
        if "далек" in line.lower():
            count += 1
    print(count)