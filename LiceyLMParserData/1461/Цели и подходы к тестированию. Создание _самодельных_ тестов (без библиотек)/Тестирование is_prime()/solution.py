from yandex_testing_lesson import is_prime


test_cases = [
    (3, True), (4, False), (5, True),
    (6, False), (7, True), (8, False),
    (11, True), (12, False), (25, False),
    (29, True), (97, True), (121, False)]
test_cases_errors = [-5, 0, -1, 1, -10]

try:
    for n, output in test_cases:
        result = is_prime(n)
        assert result == output
    for n in test_cases_errors:
        try:
            is_prime(n)
            raise
        except Exception:
            pass
    print("YES")
except Exception:
    print("NO")