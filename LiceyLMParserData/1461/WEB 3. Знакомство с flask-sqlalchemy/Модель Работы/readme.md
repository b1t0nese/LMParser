# Модель Работы

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64Mb

Продолжаем создавать БД. Теперь нужно создать модель класса Jobs с полями следующего содержания:

- id
- team_leader (id) (id руководителя, целое число)
- job (description) (описание работы)
- work_size (hours) (объем работы в часах)
- collaborators (list of id of participants) (список id участников)
- start_date (дата начала)
- end_date (дата окончания)
- is_finished (bool) (признак завершения)

Установите связь между этой моделью и моделью users, team_leader задается по id из модели users. Файл jobs.py с моделью отправьте на проверку.

## Примеры
### Пример 1
**Ввод:**
```
job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False
session.add(job)
```
**Вывод:**
```
1 deployment of residential modules 1 and 2 15 2, 3 False
```

## Примечания
SqlAlchemyBase импортировать не нужно, он будет доступен вашему решению

---
## Информация о решении

**Урок:** WEB 3. Знакомство с flask-sqlalchemy  
**Максимальный балл:** 14  
**Полученный балл:** 0  
**Статус:** rework  
**Дата:** 2026-03-30T14:56:04.417164+03:00  
**Контест:** 17077  
**Вердикт:** runtime-error  