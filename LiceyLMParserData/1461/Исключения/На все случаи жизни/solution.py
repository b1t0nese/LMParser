life, advices = [], []

input_t = None
while input_t != "":
    input_t = input()
    cur_life = input_t.split("\t")
    life.append(cur_life[0])
    try:
        life.append(cur_life[1])
    except IndexError:
        pass
life.pop()

input_t = None
while input_t != "":
    input_t = input()
    advices.append(input_t)
advices.pop()

for action in advices:
    try:
        print(life[life.index(action) + 1])
    except ValueError:
        print("Делай, что должен, и будь, что будет.")