# LiceyLMParser
парсер задач и заданий из курсов Яндекс Лицея, а также база уже готовых задач на определённые курсы от автора

# Доступные решения

1) [Основы промышленного программирования | Д25 (1461)](https://github.com/b1t0nese/LiceyLMParser/blob/main/LiceyLMParserData/1461)

---
# Как использовать

1) Устанавливаем зависимости:
```bash
pip install -r requirements.txt
```
Также установите [Chrome последней версии](https://www.google.com/chrome/)

2) Получаем cookies аккаунта студента для будущего парсинга:
```bash
python get_cookie.py https://lms.yandex.ru/
```
Авторизируемся на сайте открытого Chrome, и жмём Enter в командной строке.

3) Запускаем процесс парсинга:
```bash
python liceylmparser.py <course_id> <group_id>
```
И ждём.

# Как получить <course_id> <group_id>:
1) Открываем сайт Яндекс LMS и выбираем курс.
2) С ссылки типа "https://lms.yandex.ru/courses/<course_id>/groups/<group_id>" берём наши значения.