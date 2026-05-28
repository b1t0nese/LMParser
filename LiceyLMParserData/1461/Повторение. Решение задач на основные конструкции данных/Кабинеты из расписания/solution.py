with open("input.txt", "r", encoding="utf-8") as f:
    output = {}
    for line in f:
        line = line.split()
        if len(line) > 1:
            cab, object = line[-1], " ".join(line[:-1])
            if cab not in output:
                output[cab] = []
            if object not in output[cab]:
                output[cab].append(object)

output = dict(sorted(output.items(), key=lambda x: int(x[0])))

with open("output.txt", "w", encoding="utf-8") as f:
    for i, item in enumerate(output.items()):
        f.write(f"{item[0]}: {', '.join(item[1])}" + 
                ("\n" if i + 1 < len(output) else ""))