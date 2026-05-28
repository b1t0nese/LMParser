from yandex_testing_lesson import is_palindrome

tests = [("", True), ("1", True), ("123", False), ("12321", True)]

ok = True
for test in tests:
    try:
        assert is_palindrome(test[0]) == test[1]
    except Exception:
        ok = False
        break
print("YES" if ok else "NO")
