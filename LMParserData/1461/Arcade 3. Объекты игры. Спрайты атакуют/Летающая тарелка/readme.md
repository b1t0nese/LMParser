# Летающая тарелка

**Ограничение времени:** 200 секунд
**Ограничение памяти:** 896 Мб

Реализуйте приложение в окне **800х600** с фоном `DARK_IMPERIAL_BLUE`.

В центре окна находится летающая тарелка ([plate.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/K_%D0%9B%D0%B5%D1%82%D0%B0%D1%8E%D1%89%D0%B0%D1%8F%20%D1%82%D0%B0%D1%80%D0%B5%D0%BB%D0%BA%D0%B0/plate.png)) с полупрозрачным лучом света ([beam.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/K_%D0%9B%D0%B5%D1%82%D0%B0%D1%8E%D1%89%D0%B0%D1%8F%20%D1%82%D0%B0%D1%80%D0%B5%D0%BB%D0%BA%D0%B0/beam.png)). Клик по тарелке позволяет её перемещать — она "прилипает" к мышке, повторный клик — останавливает и отпускает тарелку. В окне движутся со случайными скоростями от -10 до 10 невидимые инопланетяне ([alien.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/K_%D0%9B%D0%B5%D1%82%D0%B0%D1%8E%D1%89%D0%B0%D1%8F%20%D1%82%D0%B0%D1%80%D0%B5%D0%BB%D0%BA%D0%B0/alien.png)), которые отталкиваются от краёв окна. Они становятся видимыми, только когда попадают в световой луч тарелки (радиус **150** пикселей).

Для решения вам потребуется создать класс `Alien` и основной класс игры `FlyingPlateGame`.

Класс `Alien`, наследник arcade.Sprite; содержит кроме инициализации методы `update()` и `update_visibility()` (см. шаблон).

 Шаблон кода для решения

Используйте предоставленный шаблон. Он содержит необходимую структуру для успешного прохождения тестов. Ваш код нужно написать вместо `...`

```
import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flying Plate"
BEAM_RADIUS = 150

class Alien(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        # 1. Загрузите текстуру ('images/alien.png').
        # 2. Установите alpha = 0 или visible = False, чтобы сделать пришельца невидимым.
        # 3. scale = 0.2
        # 4. Задайте случайную скорость движения. (random.randint)
        # 5. Случайным образом определите ориентацию текстуры по горизонтали (random.randint)
        ...

    def update_visibility(self, plate_x, plate_y):
        # Вычислите дистанцию от пришельца до центра тарелки.
        # Если дистанция меньше BEAM_RADIUS, установите self.alpha = 255, иначе — 0.
        ...

    def update(self, delta_time: float = 1 / 60):
        # Реализуйте движение пришельца и его отскок от всех четырех краёв окна.
        ...

class FlyingPlateGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Установите цвет фона.
        ...

    def setup(self):
        # 1. Создайте спрайты тарелки(scale=0.3) и луча(scale=0.5), поместите их в один SpriteList.
        # 2. Создайте инопланетян с помощью create_aliens().
        # 3. Инициализируйте атрибуты для координат тарелки (по центру экрана) и флага self.moving.
        # 4. Создайте 20 инопланетян.
        ...

    def create_aliens(self, count):
        # В цикле создайте 'count' экземпляров класса Alien в случайных позициях
        # и добавьте их в список спрайтов для пришельцев.
        ...

    def update_sprites_position(self):
        # Этот метод синхронизирует позиции спрайтов тарелки и луча
        # с логическими координатами self.plate_x и self.plate_y.
        self.plate_sprite.center_x = self.plate_x
        self.plate_sprite.center_y = self.plate_y
        self.beam_sprite.center_x = self.plate_x
        self.beam_sprite.center_y = self.plate_y

    def on_draw(self):
        self.clear()
        # Отрисуйте список с тарелкой и список с инопланетянами.
        # Невидимые пришельцы (с alpha=0) не будут отрисованы автоматически.
        ...

    def on_mouse_press(self, x, y, button, modifiers):
        # Проверьте, был ли клик по тарелке. Если да, инвертируйте флаг self.moving.
        ...

    def on_mouse_motion(self, x, y, dx, dy):
        # Если self.moving активно, обновляйте self.plate_x и self.plate_y,
        # ограничивая их пределами окна. Затем вызовите update_sprites_position().
        ...

    def on_update(self, delta_time):
        # В цикле для каждого инопланетянина вызовите его метод update_visibility().
        # После этого вызовите .update() у всего списка пришельцев для их перемещения.
        ...

def setup_game(width=800, height=600, title="Flying Plate"):
    game = FlyingPlateGame(width, height, title)
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

Все изображения находятся в папке `images/`. Указывайте пути к файлам относительно неё (например, `images/alien.png`).

---
## Информация о решении

**Урок:** Arcade 3. Объекты игры. Спрайты атакуют  
**Максимальный балл:** 34  
**Полученный балл:** 0  
**Статус:** new  
**Дата:** 2025-12-13T10:16:23.447791+03:00  