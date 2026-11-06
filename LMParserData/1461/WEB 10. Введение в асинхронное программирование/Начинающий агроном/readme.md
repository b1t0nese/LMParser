# Начинающий агроном

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 92Mb

Когда что-то делаешь впервые, хорошо бы записать порядок действий, чтобы что-нибудь не забыть и не перепутать. Вот, например, памятка для начинающего агронома.

Семена перед посадкой нужно замочить в специальном растворе для повышения всхожести и защиты от болезней. Выдержать в нем строго указанное время.

Затем посадить в землю и накрыть нетканым материалом для сохранения влажности. Через заданное время снять укрытие.

Пикировка. Подросшие сеянцы нужно аккуратно рассадить по одному в горшочек. Подождать некоторое время, пока они приживутся. Все, рассада готова.

Эти этапы должны следовать именно в таком порядке. Однако подкормить растения минеральными удобрениями и обработать от вредителей можно в любой момент. И это надо сделать обязательно. Время на подкормку всегда 3, на обработку от вредителей – 5. При начале подкормки выводится сообщение:
 *7 Application of fertilizers for <растение>*
 при окончании:
 *7 Fertilizers for the <растение> have been introduced*
 При начале обработки:
 *8 Treatment of <растение> from pests*
 при окончании:
 *8 The <растение> is treated from pests*

Напишите асинхронную функцию sowing(), принимающую произвольное количество кортежей:
 *(растение, время замачивания, время прорастания, время приживания после пикировки)*
 и печатающую отчет в виде:

При начале процесса для каждого растения
 *0 Beginning of sowing the <растение> plant*

При начале замачивания
 *1 Soaking of the <растение> started*

После этапа замачивания
 *2 Soaking of the <растение> is finished*

При высадке семян и установке укрытия
 *3 Shelter of the <растение> is supplied*

При снятии укрытия
 *4 Shelter of the <растение> is removed*

При начале пикировки
 *5 The <растение> has been transplanted*

Растение прижилось
 *6 The <растение> has taken root*

После окончания выращивания рассады
 *9 The seedlings of the <растение> are ready*

Для увеличения скорости работы программы разделите все времена ожидания на 1000.

## Примеры
### Пример 1
**Ввод:**
```
data = [('carrot', 7, 18, 2), ('cabbage', 2, 6, 10), ('onion', 5, 12, 7)]
asyncio.run(sowing(*data))
```
**Вывод:**
```
0 Beginning of sowing the carrot plant
1 Soaking of the carrot started
7 Application of fertilizers for carrot
8 Treatment of carrot from pests
0 Beginning of sowing the cabbage plant
1 Soaking of the cabbage started
7 Application of fertilizers for cabbage
8 Treatment of cabbage from pests
0 Beginning of sowing the onion plant
1 Soaking of the onion started
7 Application of fertilizers for onion
8 Treatment of onion from pests
2 Soaking of the cabbage is finished
3 Shelter of the cabbage is supplied
7 Fertilizers for the carrot have been introduced
7 Fertilizers for the cabbage have been introduced
7 Fertilizers for the onion have been introduced
8 The carrot is treated from pests
8 The cabbage is treated from pests
2 Soaking of the onion is finished
3 Shelter of the onion is supplied
8 The onion is treated from pests
2 Soaking of the carrot is finished
3 Shelter of the carrot is supplied
4 Shelter of the cabbage is removed
5 The cabbage has been transplanted
4 Shelter of the onion is removed
5 The onion has been transplanted
6 The cabbage has taken root
9 The seedlings of the cabbage are ready
4 Shelter of the carrot is removed
5 The carrot has been transplanted
6 The onion has taken root
9 The seedlings of the onion are ready
6 The carrot has taken root
9 The seedlings of the carrot are ready
```

---
## Информация о решении

**Урок:** WEB 10. Введение в асинхронное программирование  
**Максимальный балл:** 20  
**Полученный балл:** 20  
**Статус:** accepted  
**Дата:** 2026-05-18T17:41:55.961066+03:00  
**Контест:** 37235  
**Вердикт:** ok  