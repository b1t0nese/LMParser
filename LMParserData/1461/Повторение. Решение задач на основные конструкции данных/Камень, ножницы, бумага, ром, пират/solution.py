wins = {
    "камень": ("ножницы", "ром"),
    "ножницы": ("бумага", "ром"),
    "бумага": ("пират", "камень"),
    "ром": ("бумага", "пират"),
    "пират": ("камень", "ножницы"),
}

pirot1, pirot2 = input(), input()

if pirot1 == pirot2:
    print("ничья")
else:
    for enemy in wins[pirot1]:
        if enemy == pirot2:
            print("первый")
            break
    for enemy in wins[pirot2]:
        if enemy == pirot1:
            print("второй")
            break
