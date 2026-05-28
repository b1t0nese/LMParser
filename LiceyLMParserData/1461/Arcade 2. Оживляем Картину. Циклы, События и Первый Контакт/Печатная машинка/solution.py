import arcade
from pyglet.graphics import Batch

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Writing Machine"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.batch = Batch()
        self.text = ""
        self.arcade_text = arcade.Text(
            self.text, self.width // 2, self.height // 2,
            arcade.color.BANANA_YELLOW,
            font_size=100, font_name="Calibri",
            anchor_x="center", anchor_y="center",
            batch=self.batch)

    def on_key_press(self, key, modifiers):
        if key == 65505:
            return
        self.text += chr(key).upper() if modifiers & arcade.key.MOD_SHIFT\
            else chr(key).lower()

    def on_draw(self):
        self.clear()
        self.arcade_text.text = self.text
        self.batch.draw()


def setup_game(width=800, height=600, title="Writing Machine"):
    game = MyGame(width, height, title)
    game.setup()
    return game