import arcade
import random
from arcade.types import Color

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Color points"
COLORS = ['#ffc000', '#dc00a9', '#0065ac', '#22ad00']


class MyGame(arcade.Window):
    def __init__(self, width, height, title, colors):
        super().__init__(width, height, title)
        self.colors = colors

    def setup(self):
        self.points = []
        self.radius = 20
        for i in range(len(self.colors)):
            if isinstance(self.colors[i], str) and self.colors[i].startswith("#"):
                hex_color = self.colors[i].lstrip("#")
                if len(hex_color) == 6:
                    self.colors[i] = (
                        int(hex_color[0:2], 16),
                        int(hex_color[2:4], 16),
                        int(hex_color[4:6], 16)
                    )

    def on_draw(self):
        self.clear()
        for point in self.points:
            x, y, color = point
            arcade.draw_circle_filled(x, y, self.radius, color)

    def on_mouse_press(self, x, y, button, modifiers):
        self.points.append((x, y, random.choice(self.colors)))


def setup_game(width=800, height=600, title="Color points", colors=None):
    # Если в функцию не передали список цветов, используйте COLORS по умолчанию
    game = MyGame(width, height, title, COLORS[:] if colors is None else colors)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()