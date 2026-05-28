# Перспектива

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 256 Мб

С помощью библиотеки `arcade` создайте изображение в окне приложения, имитирующее перспективу. Фон окна чёрный, заголовок **«Perspective»**.

Конструктор окна при инициализации принимает дополнительно цвет, ширину и высоту начального (самого нижнего) прямоугольника. Он располагается по центру окна по ширине и не доходит 20 пикселей до нижнего края.

Ещё 3 прямоугольника располагаются за первым и меньше него: размеры уменьшаются на 20 пикселей с каждой стороны (всего на 40), каждый следующий прямоугольник на 20 пикселей выше предыдущего и компоненты цвета — красная и зелёная — на 20 меньше.

Для рисования прямоугольников используйте метод `arcade.draw_lbwh_rectangle_filled()`.

Используйте шаблон кода ниже (вместо `...` впишите свой код), атрибуты класса должны иметь такие же имена, как аргументы в шаблоне.

 **Шаблон кода решения**

```
import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Perspective"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, width_rect, height_rect, color_rect: tuple[int, int, int]):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.width_rect = width_rect
        self.height_rect = height_rect
        self.color_rect = color_rect

    def on_draw(self):
        self.clear()
        ...

def setup_game(width=900, height=600, title="Perspective", width_rect=500, height_rect=300, color_rect=(192, 255, 0)):
    game = MyGame(width, height, title, width_rect, height_rect, color_rect)
    return game

def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

Результат (900x600)

## Примечания
Для успешного выполнения ваше решение должно содержать функцию `setup_game` и другие методы и функции, предоставленные в шаблоне.

---
## Информация о решении

**Урок:** Arcade 1. Основы Arcade. Немного примитивно  
**Максимальный балл:** 17  
**Полученный балл:** 17  
**Статус:** accepted  
**Дата:** 2025-12-03T11:08:22.756195+03:00  
**Контест:** 79908  
**Вердикт:** ok  