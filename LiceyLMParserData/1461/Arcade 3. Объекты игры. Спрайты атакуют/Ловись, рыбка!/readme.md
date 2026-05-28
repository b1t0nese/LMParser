# Ловись, рыбка!

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 896 Мб

Создайте приложение для рыбалки в окне **1000х600** с фоном [shore.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/H_%D0%9B%D0%BE%D0%B2%D0%B8%D1%81%D1%8C%2C%20%D1%80%D1%8B%D0%B1%D0%BA%D0%B0%21/shore.png).

В нижней половине окна плавают рыбки ([fish.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/H_%D0%9B%D0%BE%D0%B2%D0%B8%D1%81%D1%8C%2C%20%D1%80%D1%8B%D0%B1%D0%BA%D0%B0%21/fish.png)) со случайными скоростями. Их движение "зациклено": уплывая за левый край, они появляются справа. Сверху свисает леска с крючком ([hook.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/H_%D0%9B%D0%BE%D0%B2%D0%B8%D1%81%D1%8C%2C%20%D1%80%D1%8B%D0%B1%D0%BA%D0%B0%21/hook.png)), верхний конец которой следует за мышью. Как только крючок подходит близко к носу рыбки, она считается пойманной и перемещается в бадью ([pot.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/H_%D0%9B%D0%BE%D0%B2%D0%B8%D1%81%D1%8C%2C%20%D1%80%D1%8B%D0%B1%D0%BA%D0%B0%21/pot.png)) на берегу.

Для решения вам потребуется создать класс рыбки `Fish` и основной класс игры.

Шаблон кода для решения

Используйте предоставленный шаблон. Он содержит необходимую структуру для успешного прохождения тестов. Ваш код нужно написать вместо `...`

```
import arcade
import random
import math

# Константы
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Catching fish"
FISH_COUNT = 10
FISH_SPEED = 50
LINE_LENGTH = SCREEN_HEIGHT // 2 - 50
CATCH_DISTANCE = 20  # Дистанция для "пойманной" рыбки


class Fish(arcade.Sprite):
    def __init__(self, filename, scale=1.0):
        super().__init__(filename, scale)
        # Задайте случайную позицию в нижней половине окна, случайную скорость
        # и флаг состояния self.caught = False.
        ...

    def update(self, delta_time):
        # Если рыба не поймана (проверьте флаг):
        #   - Обновите её позицию.
        #   - Реализуйте "зацикливание" по горизонтали и отскок от границ воды.
        # Если поймана:
        #   - Плавно перемещайте её в точку над бадьёй.
        ...


class FishingGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Загрузите фоновую текстуру.
        ...

    def setup(self):
        # Инициализируйте списки спрайтов: self.fish_list, self.hook_list, self.pot_list.
        # Создайте и добавьте в них FISH_COUNT рыбок, 1 крючок и 1 бадью.
        ...

    def on_draw(self):
        self.clear()
        # Отрисуйте фон, бадью, рыбок.
        # Отдельно нарисуйте леску (arcade.draw_line) от верха окна до крючка.
        # Затем отрисуйте крючок.
        ...

    def on_update(self, delta_time):
        # Вызовите .update() у списка рыбок.
        # В цикле проверьте дистанцию от крючка до каждой непойманной рыбки.
        # Если дистанция меньше CATCH_DISTANCE, установите рыбке флаг caught = True.
        ...

    def on_mouse_motion(self, x, y, dx, dy):
        # Реализуйте движение крючка: вычислите его новую позицию так, чтобы
        # он следовал за мышью, но длина лески оставалась постоянной (LINE_LENGTH).
        ...


def setup_game(width=1000, height=600, title="Catching fish"):
    game = FishingGame(width, height, title)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
```

Результат

При задании констант, как в шаблоне, должен получиться результат:

## Примечания
Для успешной сдачи задачи ваше решение должно содержать функцию `setup_game` и другую сигнатуру, объявленную в предоставленном шаблоне.

Все изображения находятся в папке `images/`. Указывайте пути к файлам относительно неё (например, `images/shore.png`).

---
## Информация о решении

**Урок:** Arcade 3. Объекты игры. Спрайты атакуют  
**Максимальный балл:** 34  
**Полученный балл:** 0  
**Статус:** new  
**Дата:** 2025-12-10T16:45:51.547912+03:00  