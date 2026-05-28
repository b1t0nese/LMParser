# Origami cat

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 512 Мб

В окне `12p x 19p` (где `p` — константа), залитым цветом BEIGE, нарисуйте кота линиями цвета COOL_BLACK, толщиной 4 пикселя по схеме:

В качестве `p` будет выступать глобальная переменная `PART` и `self.part` — атрибут класса. Для отрисовки линий используйте метод `arcade.draw_polygon_outline()`.

Используйте шаблон кода ниже (вместо `...` впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные аргументы.

 **Шаблон кода решения**

```
import arcade

SCREEN_TITLE = "Origami Cat"
PART = 25

class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        self.part = part

    def on_draw(self):
        self.clear()
        ...

def setup_game(width=300, height=475, title="Origami Cat", part=25):
    game = MyGame(width, height, title, part)
    return game

def main():
    setup_game(PART * 12, PART * 19, SCREEN_TITLE, PART)
    arcade.run()

if __name__ == "__main__":
    main()
```

Результат

## Примечания
Для успешного выполнения ваше решение должно содержать функцию `setup_game` и другие методы и функции, предоставленные в шаблоне.

---
## Информация о решении

**Урок:** Arcade 1. Основы Arcade. Немного примитивно  
**Максимальный балл:** 25  
**Полученный балл:** 25  
**Статус:** accepted  
**Дата:** 2025-12-08T06:18:18.915238+03:00  
**Контест:** 79908  
**Вердикт:** ok  