# Собеседование

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64Mb

Прием на работу IT-специалиста – дело ответственное, нужно проверить навыки претендента как в программировании, так и в знании алгоритмов. Нужно провести собеседование так, чтобы затратить как можно меньше времени, но не потерять в качестве.

Собеседование включает 2 этапа: претенденту выдается задание, затем он идет его выполнять, представляет результат и защищает его; потом претенденту дается 5 единиц времени отдохнуть; затем такие же действия проводятся для второго задания, кроме отдыха, разумеется.

Напишите асинхронную функцию **interviews()**, которая принимает произвольное число претендентов – кортежей вида:
 *(имя, время на подготовку 1 задания, время на защиту 1 задания, время подготовки 2 задания, время на защиту второго задания)*

Функция должна для каждого задания каждого претендента вывести строки:
 при начале выполнения задания – *<имя> started the <N> task.*
 при переходе к защите – *<имя> moved on to the defense of the <N> task.*
 при окончании выполнения задания – *<имя> completed the <N> task.*
 при начале отдыха перед вторым заданием – *<имя> is resting.*

Второе задание каждый претендент может получить только после выполнения первого.

## Примеры
### Пример 1
**Ввод:**
```
data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)
```
**Вывод:**
```
Ivan started the 1 task.
John started the 1 task.
Sophia started the 1 task.
John moved on to the defense of the 1 task.
Sophia moved on to the defense of the 1 task.
Ivan moved on to the defense of the 1 task.
Sophia completed the 1 task.
Sophia is resting.
Ivan completed the 1 task.
Ivan is resting.
John completed the 1 task.
John is resting.
Sophia started the 2 task.
Ivan started the 2 task.
John started the 2 task.
Sophia moved on to the defense of the 2 task.
Ivan moved on to the defense of the 2 task.
Sophia completed the 2 task.
John moved on to the defense of the 2 task.
Ivan completed the 2 task.
John completed the 2 task.
0.21059226989746094
```

## Примечания
Для более быстрой работы программы поделите все времена ожидания на 100.

---
## Информация о решении

**Урок:** WEB 10. Введение в асинхронное программирование  
**Максимальный балл:** 20  
**Полученный балл:** 20  
**Статус:** accepted  
**Дата:** 2026-04-09T16:02:17.114912+03:00  
**Контест:** 37235  
**Вердикт:** ok  