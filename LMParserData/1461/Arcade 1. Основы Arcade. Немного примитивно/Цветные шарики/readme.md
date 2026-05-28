# Цветные шарики

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 512 Мб

Добавьте случайности, пусть шарики появляются не в центре окна, а в случайном месте, но полностью попадают в окно, и имеют случайную скорость от -3 до 3. Шариков должно быть 12.

Цвета шариков должны быть следующими: SAE, AMBER, AMETHYST, APPLE_GREEN, AZURE, BALL_BLUE, BRIGHT_LILAC, BITTERSWEET, BLUE_VIOLET, BRIGHT_PINK, CITRINE, FRENCH_LIME.

При ударе о стенку шарик должен менять одну составляющую скорости на противоположную. Для рисования шариков используйте метод `arcade.draw_circle_filled()`.

Цвет окна DARK_BLUE_GRAY.

Используйте шаблон кода ниже (вместо ... впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные или объявленные аргументы в шаблоне.

 **Шаблон кода решения**

```
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Balls"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        ...

    def setup(self):
        self.balls = ...  # Список списков координат шариков
        self.change = ...  # Список списков скоростей шариков
        self.colors = ...  # Список цветов шариков

    def on_draw(self):
        self.clear()
        ...

    def on_update(self, delta_time):
        ...

def setup_game(width=800, height=600, title="Balls", radius=10):
    game = MyGame(width, height, title, radius)
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

Для корректного прохождения анимационных тестов важно соблюдать определенный порядок генерации случайных чисел. В методе `setup()` сначала сгенерируйте все координаты для всех 12 шаров, и только после этого — все их скорости. Для генерации чисел используйте функцию `randint`.

---
## Информация о решении

**Урок:** Arcade 1. Основы Arcade. Немного примитивно  
**Максимальный балл:** 25  
**Полученный балл:** 0  
**Статус:** new  
**Дата:** 2025-12-03T11:08:44.382561+03:00  