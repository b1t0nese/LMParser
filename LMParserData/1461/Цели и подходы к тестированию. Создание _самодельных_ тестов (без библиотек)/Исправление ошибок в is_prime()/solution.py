def is_prime(n):
    try:
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return n >= 2
    except Exception:
        return False


print("YES" if is_prime(int(input())) else "NO")