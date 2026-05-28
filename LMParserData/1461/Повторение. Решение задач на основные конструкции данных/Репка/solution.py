s = input()
persons = [input() for i in range(int(input()))]

s = s.split(" -> ")
for obj in persons:
    if s.index(obj) == 0:
        print(f"{s[0]} -> {s[1]}")
    elif s.index(obj) == len(s) - 1:
        print(f"{s[len(s) - 2]} -> {s[len(s) - 1]}")
    else:
        print(f"{s[s.index(obj) - 1]} -> {s[s.index(obj)]} -> {s[s.index(obj) + 1]}")
