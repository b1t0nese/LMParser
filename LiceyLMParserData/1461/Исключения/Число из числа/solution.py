chislo = input()
try:
    assert len(chislo) > 4, "There are not enough discharges."
except AssertionError as e:
    print(e)
    exit()

chislo2 = int(chislo[len(chislo) - 4:] + chislo[:len(chislo) - 4])
try:
    assert len(str(chislo2)) == len(str(chislo)), "The number has decreased."
except AssertionError as e:
    print(e)
    exit()

chislo3 = 0
for i in str(chislo2):
    chislo3 += int(i)
chislo2 += chislo3
try:
    assert chislo2 % 2 == 0, "Odd result."
except AssertionError as e:
    print(e)
    exit()

print(chislo2)