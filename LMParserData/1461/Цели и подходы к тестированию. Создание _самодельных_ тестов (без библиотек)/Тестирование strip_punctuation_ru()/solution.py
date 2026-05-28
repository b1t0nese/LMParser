from yandex_testing_lesson import strip_punctuation_ru


test_data = [
    ['лал, аяя-ааа. ы', 'лал аяя-ааа ы'],
    ['.', ''], ['зов, ю... ь!', 'зов ю ь'],
    ['р, ы', 'р ы'], ['р, - ы', 'р ы']
]

for test in test_data:
    if strip_punctuation_ru(test[0]) != test[1]:
        print('NO')
        break
else:
    print("YES")