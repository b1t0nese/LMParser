from collections import Counter

input_counter = Counter(input())

valid_words = []
while True:
    try:
        current_word = input()
        is_valid = True
        for char, count in Counter(current_word).items():
            if char not in input_counter or count > input_counter[char]:
                is_valid = False
                break
        if is_valid:
            valid_words.append(current_word)
    except EOFError:
        break

print(len(valid_words))
print("\n".join(valid_words))