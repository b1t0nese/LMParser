wins = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}

pirot1, pirot2 = input(), input()

if pirot1 == pirot2:
    print("ничья")
elif wins[pirot1] == pirot2:
    print("первый")
elif wins[pirot2] == pirot1:
    print("второй")