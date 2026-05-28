from math import *

func = input()

with open("function.txt", "w") as f:
    for x in range(0, 201):
        x = x / 100
        f.write(f"{x}\t{round(eval(func), 3)}\n")