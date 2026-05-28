# Улетаем

**Ограничение времени:** 20 секунд
**Ограничение памяти:** 768 Мб

Напишите приложение на `arcade`, в белом окне которого аисты летят друг за другом бесконечно. На схеме показан один аист, справа от него вплотную к этому изображению летит следующий.

Размер окна по горизонтали — дважды повторённый размер схемы. Характерный размер клетки передаётся в конструктор класса как атрибут `self.part`.

При рисовании аиста используются цвета: белый, чёрный, красный. Толщина контура — 1/10 характерного размера.

[ссылка на детальное изображение](https://assets.contest.yandex.net/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..GygAuEaB0px9d5Tw.EMuJsPDeXIGiiaR45n5xGkj3kJo-kcwWFLMTjtzpGbAIC4-94S2BfeuPpyl6ZnDCvxg5xC7Iz87kbz1j7HxCczqB4F4fYXq91EcjiiMVhCWpYYK_aE89YeY2t3olmHG0m0Mh6PHO.-3vV-Thg2ecx73qGDk3Uvg)

Используйте такие методы отрисовки: `arcade.draw_circle_outline()`, `arcade.draw_circle_filled()`, `arcade.draw_triangle_filled()`, `arcade.draw_arc_outline()`, `arcade.draw_arc_filled()`, `arcade.draw_line()`.

Шаг изменения координаты за кадр равен 0.05.

Используйте шаблон кода ниже (вместо ... впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные или объявленные аргументы в шаблоне.

 **Шаблон кода решения**

```
import arcade

PART = 20
SCREEN_WIDTH = PART * 36
SCREEN_HEIGHT = PART * 15
SCREEN_TITLE = "Flying storks"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        ...

    def setup(self):
        self.storks = ...  # Список координат кончика клюва трёх аистов
        # Первый — 0, второй — посередине окна, третий — правый край окна

    def on_draw(self):
        self.clear()
        ...

    def on_update(self, delta_time):
        ...

def setup_game(width=720, height=300, title="Flying storks", part=20):
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
**Дата:** 2025-12-03T18:10:33.505929+03:00  