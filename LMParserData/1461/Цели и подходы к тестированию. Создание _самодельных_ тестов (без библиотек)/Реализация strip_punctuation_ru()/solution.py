def strip_punctuation_ru(s):
    s2 = ""
    for char in s:
        s2 += ' ' if char in '''!()—[]{};:'"\,<>./?@#$%^&*_~''' else char
    return " ".join(s2.replace(" - ", " ").split())


print(strip_punctuation_ru(input()))