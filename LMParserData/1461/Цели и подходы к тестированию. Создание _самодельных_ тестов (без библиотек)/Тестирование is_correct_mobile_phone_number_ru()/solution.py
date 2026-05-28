from yandex_testing_lesson import is_correct_mobile_phone_number_ru

test_data = [
    ('+79001234567', True), ('89001234567', True), ('+7(900)1234567', True),
    ('8(900)1234567', True), ('+7 900 123-45-67', True), ('8 900 123 45 67', True),
    ('+7(900) 123-45-67', True), ('8-900-123-45-67', True), ('+7-900-123-45-67', True),
    ('8 (900) 123 45 67', True), ('890012345678', False), ('+7900123456', False),
    ('79001234567', False), ('+89001234567', False), ('+8(90)(01234567', False),
    ('+7 (900) 12(34567', False), ('+7900123456a', False), ('', False),
    ('+7900.123.45.67', False), ('+7900/123/45/67', False)
]

for test in test_data:
    if is_correct_mobile_phone_number_ru(test[0]) != test[1]:
        print('NO')
        break
else:
    print("YES")