# Шишкомёт

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 896 Мб

Напишите приложение в окне **1000х800** с фоном цвета `WHEAT`.

В центре окна сидит медведь ([bear.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/J_%D0%A8%D0%B8%D1%88%D0%BA%D0%BE%D0%BC%D1%91%D1%82/bear.png)) с масштабом **0.7**. По клику мыши он поворачивается в сторону клика (отражается по горизонтали) и бросает туда шишку ([cone.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/J_%D0%A8%D0%B8%D1%88%D0%BA%D0%BE%D0%BC%D1%91%D1%82/cone.png)) с масштабом **0.4**. Шишку необходимо повернуть, чтобы она летела нужным концом вперёд. Когда шишка улетает за пределы экрана, она исчезает.

Для решения вам потребуется создать классы `Bear`, `Cone` и `FaceDirection` (см. шаблон).

Шаблон кода для решения

Используйте предоставленный шаблон. Он содержит необходимую структуру для успешного прохождения тестов. Ваш код нужно написать вместо `...`

```
import arcade
import math
import enum


class FaceDirection(enum.Enum):
    LEFT = 0
    RIGHT = 1


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Bear and cones"


class Bear(arcade.Sprite):
    def __init__(self):
        super().__init__()
        # 1. Загрузите текстуру ('images/bear.png').
        # 2. Установите начальные значения: масштаб, позицию в центре окна и направление взгляда.
        ...

    def update_animation(self, delta_time: float = 1 / 60):
        """ Обновление анимации """
        # В зависимости от направления взгляда (self.face_direction),
        # отражайте или не отражайте текстуру медведя по горизонтали.
        ...

    def update(self, delta_time, x):
        # Сравните координату x (цель клика) с центром экрана,
        # чтобы определить и установить новое направление взгляда (self.face_direction).
        ...


class Cone(arcade.Sprite):
    def __init__(self, start_x, start_y, target_x, target_y, speed=800, damage=10):
        super().__init__()
        # 1. Загрузите текстуру шишки ('images/cone.png') и отразите её.
        # 2. Установите начальные координаты и масштаб.
        # 3. Используя математику (math.atan2, cos, sin), рассчитайте вектор
        #    скорости (self.change_x, self.change_y) по направлению к цели.
        # 4. Установите угол поворота спрайта (self.angle).
        ...

    def update(self, delta_time):
        # Обновите позицию шишки на основе её скорости и delta_time.
        # Проверьте, не вышла ли шишка за пределы экрана, и если да —
        # удалите её (self.remove_from_sprite_lists()).
        ...


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Установите цвет фона
        ...

    def setup(self):
        self.bear_list = arcade.SpriteList()
        self.cones_list = arcade.SpriteList()
        # Инициализируйте списки спрайтов.
        # Создайте один экземпляр класса Bear и добавьте его в список.
        ...

    def on_draw(self):
        self.clear()
        # Отрисуйте оба списка спрайтов.
        ...

    def on_update(self, delta_time):
        # Вызовите методы обновления для спрайтов: .update() для обоих списков
        # и .update_animation() для медведя.
        ...

    def on_mouse_press(self, x, y, button, modifiers):
        # При клике создайте новый экземпляр Cone, передав ему координаты
        # медведя (старт) и мыши (цель). Добавьте новую шишку в список.
        ...


def setup_game(width=1000, height=800, title="Bear and cones"):
    game = MyGame(width, height, title)
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

Все изображения находятся в папке `images/`. Указывайте пути к файлам относительно неё (например, `images/bear.png`).

---
## Информация о решении

**Урок:** Arcade 3. Объекты игры. Спрайты атакуют  
**Максимальный балл:** 33  
**Полученный балл:** 0  
**Статус:** new  
**Дата:** 2025-12-13T10:15:40.626245+03:00  