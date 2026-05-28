# Человечек

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 512 Мб

Нарисуйте анимированного человечка в окне `arcade`, залитом цветом BRILLIANT_LAVENDER.

Характерный размер клеточки передаётся в конструктор класса. Человечек рисуется по схеме (красными штриховыми линиями показаны промежуточные положения рук и ног при анимации).

Положения меняются каждое десятое обновление экрана.

Толщина линии земли — 1/10 характерного размера, толщина линий человечка — 1/4.

Сохраните значение `part` в атрибут `self.part`. А для отрисовки используйте методы `arcade.draw_circle_filled()`, `arcade.draw_line()`.

Используйте шаблон кода ниже (вместо ... впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные или объявленные аргументы в шаблоне.

 **Шаблон кода решения**

```
import arcade

PART = 30
SCREEN_WIDTH = PART * 12
SCREEN_HEIGHT = PART * 11
SCREEN_TITLE = "Walking man"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        ...

    def setup(self):
        self.hands = ...  # Список координат нижней точки левой руки
        self.foots = ...  # Список координат пятки левой ноги
        self.i = 0  # Изменение координат за один кадр

    def on_draw(self):
        self.clear()
        ...

    def on_update(self, delta_time):
        ...

def setup_game(width=360, height=330, title="Walking man", part=30):
    game = MyGame(width, height, title, part)
    game.setup()
    return game

def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
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
**Полученный балл:** 0  
**Статус:** new  
**Дата:** 2025-12-03T18:34:55.165616+03:00  