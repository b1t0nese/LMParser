# Собеседование-2

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64Mb

Последовательное выполнение заданий занимает слишком много времени. Вы решили выдать очередным претендентам сразу оба задания, но выполнять они их должны последовательно.

Собеседование включает 2 этапа: всем претендентам выдается первое задание, затем в том же порядке выдается второе задание, затем они идут их выполнять, представляют результат первого задания; затем такие же действия проводятся для второго задания.

Напишите асинхронную функцию **interviews_2()**, которая принимает произвольное число претендентов – кортежей вида:
 *(имя, время на подготовку 1 задания, время на защиту 1 задания, время подготовки 2 задания, время на защиту второго задания)*

Функция должна для каждого задания каждого претендента вывести строки:
 при начале выполнения задания – *<имя> started the <N> task.*
 при переходе к защите – *<имя> moved on to the defense of the <N> task.*
 при окончании выполнения задания – *<имя> completed the <N> task.*

## Примеры
### Пример 1
**Ввод:**
```
data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews_2(*data))
print(time.time() - t0)
```
**Вывод:**
```
Ivan started the 1 task.
John started the 1 task.
Sophia started the 1 task.
Ivan started the 2 task.
John started the 2 task.
Sophia started the 2 task.
John moved on to the defense of the 1 task.
John completed the 1 task.
Sophia moved on to the defense of the 1 task.
Sophia completed the 1 task.
Sophia moved on to the defense of the 2 task.
Sophia completed the 2 task.
John moved on to the defense of the 2 task.
John completed the 2 task.
Ivan moved on to the defense of the 1 task.
Ivan completed the 1 task.
Ivan moved on to the defense of the 2 task.
Ivan completed the 2 task.
0.2332758903503418
```

## Примечания
Для более быстрой работы программы поделите все времена ожидания на 100.

---
## Информация о решении

**Урок:** WEB 10. Введение в асинхронное программирование  
**Максимальный балл:** 20  
**Полученный балл:** 20  
**Статус:** accepted  
**Дата:** 2026-04-09T16:19:09.865885+03:00  
**Контест:** 37235  
**Вердикт:** ok  