import arcade
from pyglet.graphics import Batch

DEFAULT_FONT_SIZE = 40
SCREEN_TITLE = "Rosetta Stone"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, lines, colors, font_size):
        super().__init__(width, height, title)

        self.batch = Batch()
        self.lines = lines
        self.colors = colors
        self.font_size = font_size
        self.texts = []

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        positions = [(300, 100), (300, 200), (300, 300)]
        for i in range(len(self.lines)):
            text = {
                'text': self.lines[i], 'x': positions[i][0], 'y': positions[i][1],
                'color': self.colors[i], 'font_size': self.font_size,
                'font_name': 'Arial', 'anchor_x': 'center', 'anchor_y': 'center'
            }
            self.texts.append(text)

    def on_draw(self):
        self.clear()
        arcade.Text(**self.texts[0]).draw()
        arcade.Text(**self.texts[1]).draw()
        arcade.Text(**self.texts[2]).draw()


def setup_game(width=600, height=400, title="Rosetta", lines=None, colors=None, font_size=40):
    lines = lines or ["Ροζέτα Στόουν", "Rosetta stone", "حجر رشيد"]
    colors = colors or [[255, 3, 62], [153, 102, 204], [164, 198, 57]]
    game = MyGame(width, height, title, lines, colors, font_size)
    game.setup()
    return game