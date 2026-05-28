chislo, chislo2 = int(input()), 1
for i in str(chislo):
    chislo2 *= int(i)
try:
    print(chislo / chislo2)
except ZeroDivisionError:
    print(0)