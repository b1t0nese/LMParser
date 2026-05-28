# Модель Марсиане

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64Mb

Прилетев на Марс, астронавты начинают его осваивать. Прежде всего нужно автоматизировать учет произведенных работ, чтобы заниматься работами, а не бюрократией. Главный программист миссии, Тедди Сандерс, создает базу данных mars_explorer.db с двумя таблицами users и jobs. По примеру, разобранному в уроке, создайте модель класса User со следующими полями:

- id (Integer, primary_key, autoincrement)
- surname (String) (фамилия)
- name (String) (имя)
- age (Integer) (возраст)
- position (String) (должность)
- speciality (String) (профессия)
- address (String) (адрес)
- email (String, unique) (электронная почта)
- hashed_password (String) (хэшированный пароль)
- modified_date (DateTime) (дата изменения)

На проверку сдайте файл users.py с данной моделью.

## Примеры
### Пример 1
**Ввод:**
```
user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)
```
**Вывод:**
```
Scott Ridley 21 captain research engineer
module_1 scott_chief@mars.org cap
```

## Примечания
SqlAlchemyBase - не надо импортировать, он будет доступен вашему решению. И другие необходимые модули также есть в системе, на проверку отправьте только файл с классом User.

---
## Информация о решении

**Урок:** WEB 3. Знакомство с flask-sqlalchemy  
**Максимальный балл:** 14  
**Полученный балл:** 14  
**Статус:** accepted  
**Дата:** 2026-03-16T15:43:22.417496+03:00  
**Контест:** 17077  
**Вердикт:** ok  