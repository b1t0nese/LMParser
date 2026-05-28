import re


def is_correct_mobile_phone_number_ru(s):
    if s.startswith('+7'):
        r = s[2:]
    elif s.startswith('8'):
        r = s[1:]
    else:
        return False
    r = re.sub(r'[ -]', '', r)
    if re.match(r'^\(\d{3}\)', r):
        r = re.sub(r'\)', '', re.sub(r'\(', '', r, 1), 1)
    return bool(re.match(r'^\d{10}$', r))


print('YES' if is_correct_mobile_phone_number_ru(input()) else 'NO')