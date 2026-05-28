import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Changing Circle"
VELOCITY = 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title, velocity):
        super().__init__(width, height, title)
        self.velocity = velocity

    def setup(self):
        self.radius = 20
        self.is_growing = False
        self.is_shrinking = False

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(
            self.width // 2, self.height // 2,
            self.radius, arcade.color.GREEN_YELLOW)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.is_growing = True
            self.is_shrinking = False

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.is_growing = False
            self.is_shrinking = True

    def on_update(self, delta_time):
        if self.is_growing:
            self.radius += self.velocity
        if self.is_shrinking:
            if self.radius > 20:
                self.radius -= self.velocity
            else:
                self.radius = 20
                self.is_shrinking = False


def setup_game(width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
               title=TITLE, velocity=VELOCITY):
    game = MyGame(width, height, title, velocity)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()