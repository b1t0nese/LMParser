# Мыш (кродёться)

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 512 Мб

Напишите приложение на `arcade`, которое имитирует бегущую мышку: все её части перемещаются поступательно на 5 пикселей, а тело (треугольник) попеременно покачивается между двумя положениями, показанными на схеме. Характерный размер клетки передаётся в конструктор класса параметром `part`.

Вначале мышь рисуется, касаясь хвостом левой границы окна, тело — наклонный треугольник.

Глаза и нос — круги радиуса 0.2p (p — `part`), толщина усов и прямых линий хвоста 0.1p, дуг хвоста 0.2p. Все остальные размеры кратны 0.25p. Цвет заливки окна ANDROID_GREEN. Цвет мыши GRAY, розовые части ушей — PINK.

Когда даже кончик хвоста достигает правого края окна, мышь появляется слева и продолжает движение.

Для отрисовки используйте методы `arcade.draw_circle_filled()`, `arcade.draw_triangle_filled()`, `arcade.draw_line()`, `arcade.draw_arc_outline()`.

Используйте шаблон кода ниже (вместо ... впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные или объявленные аргументы в шаблоне.

 **Шаблон кода решения**

```
import arcade

PART = 20
SCREEN_WIDTH = PART * 30
SCREEN_HEIGHT = PART * 15
SCREEN_TITLE = "Running mouse"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        ...

    def setup(self):
        self.point = 3  # Начальная точка в клетках
        self.i = 0  # Положение тела

    def on_draw(self):
        self.clear()
        self.draw_head(self.point)
        self.draw_body(self.point, self.i)
        self.draw_tail(self.point)

    def draw_head(self, x):
        ...

    def draw_body(self, x, i):
        ...

    def draw_tail(self, x):
        ...

    def on_update(self, delta_time):
        self.point += 0.05
        ...

def setup_game(width=600, height=300, title="Running mouse", part=20):
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
**Дата:** 2025-12-03T11:08:43.294433+03:00  