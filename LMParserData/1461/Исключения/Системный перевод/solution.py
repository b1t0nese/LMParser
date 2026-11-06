digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_valid_number(n, base):
    for digit in n:
        digit_value = digits.index(digit)
        assert digit_value < base


def to_decimal(n, base):
    result = 0
    for i, digit in enumerate(reversed(n)):
        result += digits.index(digit) * (base**i)
    return result


nums = []
while True:
    try:
        n, base = input().split()
        base = int(base)
        try:
            is_valid_number(n, base)
            nums.append((n, base))
        except Exception:
            pass
    except Exception:
        break

for num in nums:
    print(f"{num[0]}({num[1]}) = {to_decimal(*num)}")