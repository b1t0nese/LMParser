import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Texture"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, filename):
        super().__init__(width, height, title)
        self.filename = filename

    def setup(self):
        self.texture = arcade.load_texture(f"images/backgrounds/{self.filename}")

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, arcade.rect.XYWH(
            self.width // 2, self.height // 2, self.width, self.height))


def setup_game(width=800, height=600, title="Texture", filename='fon1.png'):
    game = MyGame(width, height, title, filename)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()