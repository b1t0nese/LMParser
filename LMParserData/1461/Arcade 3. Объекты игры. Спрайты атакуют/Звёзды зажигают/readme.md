# Звёзды зажигают

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 1024 Мб

Реализуйте интерактивное приложение в окне **800х600** с фоном `DARK_IMPERIAL_BLUE`.

По клику на пустом месте появляется звезда (файл [star.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/E_%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D1%8B%20%D0%B7%D0%B0%D0%B6%D0%B8%D0%B3%D0%B0%D1%8E%D1%82/star.png)) с масштабом **0.1** и случайным углом поворота от 0 до 360 градусов. Повторный клик по уже существующей звезде заставляет её мигать (появляться и пропадать [star0.png](https://yastatic.net/s3/lyceum/content/images/d2_arcade3/E_%D0%97%D0%B2%D1%91%D0%B7%D0%B4%D1%8B%20%D0%B7%D0%B0%D0%B6%D0%B8%D0%B3%D0%B0%D1%8E%D1%82/star0.png)). Ещё один клик по мигающей звезде останавливает анимацию.

Для этого напишите класс `BlinkingStar`, унаследованный от `arcade.Sprite`, и основной класс игры.

 Шаблон кода для решения

Используйте предоставленный шаблон. Он содержит необходимую структуру для успешного прохождения тестов. Ваш код нужно написать вместо `...`

```
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blinking stars"
BLINK_INTERVAL = 0.5  # Интервал мигания в секундах

class BlinkingStar(arcade.Sprite):
    def __init__(self, filename, center_x, center_y, scale=1.0):
        super().__init__(filename, scale, center_x, center_y)
        self.is_blinking = False
        self.blink_timer = 0
        # Загрузите текстуру для видимого состояния звезды.
        # Также понадобится способ сделать звезду "невидимой" (например, вторая пустая текстура).
        # Задайте случайный угол поворота self.angle.
        ...

    def update(self, delta_time: float = 1 / 60):
        if self.is_blinking:
            # Увеличивайте self.blink_timer. Когда он превысит BLINK_INTERVAL:
            # - Сбросьте таймер.
            # - Переключите self.texture между видимой и "невидимой" текстурами.
            ...

    def toggle_blinking(self):
        self.is_blinking = not self.is_blinking
        if not self.is_blinking:
            # Если мигание выключилось, обязательно верните звезде видимую текстуру.
            ...

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Установите цвет фона
        ...

    def setup(self):
        """Настройка игры"""
        self.star_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        # Отрисуйте список звёзд
        ...

    def on_mouse_press(self, x, y, button, modifiers):
        """Обработка клика мышью"""
        # Используйте arcade.get_sprites_at_point, чтобы найти нажатые звёзды.
        # Если список нажатых звёзд не пуст, вызовите у них toggle_blinking().
        # Если список пуст, создайте новый экземпляр BlinkingStar в месте клика
        # и добавьте его в self.star_list.
        ...

    def on_update(self, delta_time: float):
        """Обновление состояния игры"""
        # Вызовите .update() у всего списка звёзд.
        ...

def setup_game(width=800, height=600, title="Blinking stars"):
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

Все изображения находятся в папке `images/`. Указывайте пути к файлам относительно неё (например, `images/star.png`).

---
## Информация о решении

**Урок:** Arcade 3. Объекты игры. Спрайты атакуют  
**Максимальный балл:** 20  
**Полученный балл:** 0  
**Статус:** rework  
**Дата:** 2026-03-16T15:07:36.463157+03:00  
**Контест:** 82060  
**Вердикт:** runtime-error  