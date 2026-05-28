find_words = ["далек", "далеки", "далека", "далеков", "далеку",
              "далекам", "далеком", "далеками", "далеках", "далеке"]
with open("input.txt", "r", encoding="utf-8") as f:
    count = 0
    for line in f:
        for word in line.split():
            if word.lower() in find_words:
                count += 1
                break
    print(count)