with open("elements.txt", "r", encoding="utf-8") as f:
    try:
        elements = list(map(int, f.read().splitlines()))
        fivelem = abs(elements[0] - elements[3]) + abs(elements[1] - elements[2])
    except ValueError:
        fivelem = 0
    except IndexError:
        fivelem = 1000
    print(abs(fivelem))
    print("The fifth element has been found!")