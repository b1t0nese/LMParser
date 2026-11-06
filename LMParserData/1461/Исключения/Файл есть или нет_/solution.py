import json

try:
    with open(input(), "r", encoding="utf-8") as f:
        key = input()
        print(" ".join([dat[key] for dat in json.load(f)]))
except FileNotFoundError:
    print("There is no such file in the directory.")
except KeyError:
    print("The key is missing.")
except TypeError:
    print("It is impossible to add non-line with line.")