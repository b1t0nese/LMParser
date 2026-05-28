with open("input.txt", "r", encoding="utf-8") as f:
    count = 0
    for line in f:
        for word in line.split():
            if word.lower().startswith("далек"):
                count += 1
                break
    print(count)