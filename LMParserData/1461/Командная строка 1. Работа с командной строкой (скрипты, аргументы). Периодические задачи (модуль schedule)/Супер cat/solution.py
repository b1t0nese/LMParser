import sys
try:
    file = list(filter(lambda x: not x.startswith("-"), sys.argv[::-1]))[0]
    with open(file, "r", encoding="utf-8") as f:
        data = f.read().splitlines()
        output = data.copy()
    if "--count" in sys.argv:
        output.append((f'rows count: {len(data)}',))
    if "--sort" in sys.argv:
        output[:len(data)] = sorted(output[:len(data)])
    if "--num" in sys.argv:
        output[:len(data)] = enumerate(output[:len(data)])
    for line in output:
        if isinstance(line, tuple):
            print(*line)
        else:
            print(line)
except Exception:
    print('ERROR')