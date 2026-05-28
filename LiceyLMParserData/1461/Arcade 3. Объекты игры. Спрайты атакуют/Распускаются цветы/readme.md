# Распускаются цветы

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 896 Мб

Создайте анимированную сцену в окне `arcade`. На фоне луга [meadow.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/C_%D0%A0%D0%B0%D1%81%D0%BF%D1%83%D1%81%D0%BA%D0%B0%D1%8E%D1%82%D1%81%D1%8F%20%D1%86%D0%B2%D0%B5%D1%82%D1%8B/meadow.png) в случайном порядке размещаются **10** бутонов лилий. Клик по бутону запускает его анимацию распускания.

Для этого вам потребуется написать собственный класс цветка `Flower`, унаследованный от `arcade.Sprite`. Рисунки для анимации (`flower0.png` - `flower8.png`) находятся в папке `images/flowers`. Их можно получить из архива [flowers.zip](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/C_%D0%A0%D0%B0%D1%81%D0%BF%D1%83%D1%81%D0%BA%D0%B0%D1%8E%D1%82%D1%81%D1%8F%20%D1%86%D0%B2%D0%B5%D1%82%D1%8B/flowers.zip).

Размещать цветки нужно с примененным масштабированием в 30% в рамках окна с отступом в 50 пикселей от границ.

Шаблон кода для решения

Используйте предоставленный шаблон. Он содержит необходимую структуру для успешного прохождения тестов. Ваш код нужно написать вместо `...`

```
import arcade
import random

# Константы
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Цветущие лилии"
FLOWER_COUNT = 10
ANIMATION_SPEED = 0.2  # скорость анимации в секундах между кадрами


class Flower(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 1. Загрузите все 9 текстур анимации в список self.textures.
        # 2. Установите начальную текстуру (бутон).
        # 3. Задайте позицию и масштаб спрайта.
        ...

        self.animation_frame = 0
        self.is_blooming = False
        self.animation_timer = 0

    def update(self, delta_time: float = 1 / 60):
        # Если is_blooming равно True, увеличивайте animation_timer.
        # Когда таймер превысит ANIMATION_SPEED:
        # - Сбросьте таймер, увеличьте кадр анимации (animation_frame).
        # - Смените текущую текстуру спрайта на новую из списка.
        # - Если анимация дошла до конца, установите is_blooming в False.
        ...

    def start_blooming(self):  # Изменение параметра цветения
        # Установите флаг is_blooming в True, чтобы запустить анимацию.
        ...


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Загрузите фоновую текстуру 'images/meadow.png'.
        ...

    def setup(self):
        self.flower_list = arcade.SpriteList()
        # Создайте FLOWER_COUNT экземпляров класса Flower в случайных
        # позициях и добавьте их в self.flower_list.
        ...

    def on_draw(self):
        self.clear()
        # Отрисуйте фон и список цветов self.flower_list.
        ...

    def on_update(self, delta_time):
        # Вызовите метод .update() у всего списка спрайтов, передав delta_time.
        # Это автоматически вызовет метод update() у каждого цветка.
        ...

    def on_mouse_press(self, x, y, button, modifiers):
        # Используйте arcade.get_sprites_at_point, чтобы найти нажатые цветки.
        # Для каждого из них вызовите метод start_blooming().
        ...


def setup_game(width=1000, height=500, title="Цветущие лилии"):
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

Все изображения находятся в папке `images/`. Указывайте пути к файлам относительно неё (например, `images/flowers/flower1.png`).

---
## Информация о решении

**Урок:** Arcade 3. Объекты игры. Спрайты атакуют  
**Максимальный балл:** 20  
**Полученный балл:** 0  
**Статус:** rework  
**Дата:** 2025-12-08T16:36:20.248349+03:00  
**Контест:** 82060  
**Вердикт:** runtime-error  