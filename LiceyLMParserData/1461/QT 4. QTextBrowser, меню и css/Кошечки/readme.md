# Кошечки

**Ограничение времени:** 1 секунда
**Ограничение памяти:** 64 Мб

В файле `cat_breeds.csv` (для отладки можно скачать [пример](https://assets.contest.yandex.net/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..HkG93vRbQBIbkIFP.w_EA9T9VmygunKBPO35lmX2UaEsdKm-PjCSORVPh1GpXgB5e9XlpU1mnalhGvVmAxGf-Hw876_q0ASIOAcNml0PmZzS-nsh-jsziznUI.OSQoHGMkg68BTdw2qdFf-g)) записана информация о породах кошек и некоторые дополнительные сведения о каждой из них с заголовками (разделители — ;):

```
Breed; Location of origin; Type; Body type; Coat type and length; Coat pattern
```

Напишите приложение на PyQT6, которое помогает найти породу по вводимой в поле `QLineEdit` подстроке. Все строки, в породе которых есть подстрока в любом регистре, выводятся в поле QTextBrowser со значениями полей через запятую и пробел. Порода (breed) выделена полужирным начертанием (bold), остальное — обычным. Заливка под текстом чередуется из цветов по порядку в цикле:

```
Cornsilk
BlanchedAlmond
Bisque
NavajoWhite
Wheat
BurlyWood
Tan
```

Цвет под строкой можно изменить так: `<тег style="background:имя цвета">...</тег>`

Класс, реализующий окно приложения, называется `CatBreeds` и наследуется от `QMainWindow`, должен быть метод `write`.

Окно содержит строку для ввода породы `QLineEdit` с именем `lineEdit` (вывод появляется сразу после ввода символа) и поле вывода `QTextBrowser` с именем `textBrowser`.

---
## Информация о решении

**Урок:** QT 4. QTextBrowser, меню и css.  
**Максимальный балл:** 34  
**Полученный балл:** 34  
**Статус:** accepted  
**Дата:** 2026-01-11T15:04:44.058777+03:00  
**Контест:** 80824  
**Вердикт:** ok  