# Летающие квадраты

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 256 Мб

Напишите приложение на `arcade`, рисующее два квадрата, разлетающихся снизу вверх вправо и влево под углом в 45 градусов.

Сначала квадраты находятся посередине окна чёрного цвета внизу один поверх другого. Затем начинают разлетаться, в каждом цикле смещаясь на 2 пикселя по х и по у.

Для рисования квадратов используйте метод `arcade.draw_lbwh_rectangle_filled()`.

Используйте шаблон кода ниже (вместо `...` впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные аргументы. Цвет передаётся в 16-ричном формате.

 **Шаблон кода решения**

```
import arcade
from arcade.types import Color

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flying squares"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, side, color):
        super().__init__(width, height, title)
        self.side = side
        self.color = color

    def setup(self):
        self.points = ...  # Список списков координат квадратов для рисования

    def on_draw(self):
        """Этот метод отвечает за отрисовку содержимого окна"""
        self.clear()
        ...

    def on_update(self, delta_time):
        """Этот метод отвечает за обновление логики игры (анимации, взаимодействия и т. д.)"""
        ...

def setup_game(width=900, height=600, title="Flying squares", side=100, color="#ff40ff"):
    game = MyGame(width, height, title, side, color)
    game.setup()
    return game

def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
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
**Максимальный балл:** 17  
**Полученный балл:** 17  
**Статус:** accepted  
**Дата:** 2026-03-01T18:05:36.039021+03:00  
**Контест:** 79908  
**Вердикт:** ok  