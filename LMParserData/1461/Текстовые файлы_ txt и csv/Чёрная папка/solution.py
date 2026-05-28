with open("black/another_black/cats_black_and_other.txt", "r", encoding="utf-8") as f:
    words = []
    for line in f.read().splitlines():
        if "cat" in line.lower():
            for word in line.split():
                upper_symbols = 0
                for symbol in word:
                    if symbol.upper() == symbol and symbol.isalpha():
                        upper_symbols += 1
                if upper_symbols == 1 and word[0].upper() == word[0]:
                    words.append(word)
with open("cats.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(words)))