import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Snowfalls"
VELOCITY = 2


class MyGame(arcade.Window):
    def __init__(self, width, height, title, velocity):
        super().__init__(width, height, title)
        self.velocity = velocity

    def setup(self):
        self.points = []
        self.side = 20

    def on_draw(self):
        self.clear()
        for i in range(len(self.points)):
            x, y = self.points[i]
            arcade.draw_line(x - self.side // 2, y, x + self.side // 2, y, arcade.color.WHITE, 2)
            arcade.draw_line(x, y - self.side // 2, x, y + self.side // 2, arcade.color.WHITE, 2)
            arcade.draw_line(x - self.side // 2, y - self.side // 2, x + self.side // 2, y + self.side // 2, arcade.color.WHITE, 2)
            arcade.draw_line(x - self.side // 2, y + self.side // 2, x + self.side // 2, y - self.side // 2, arcade.color.WHITE, 2)
            self.points[i] = x, y - self.velocity if y > self.side//2 else y

    def on_mouse_press(self, x, y, button, modifiers):
        self.points.append([x, y])


def setup_game(width=800, height=600, title="Snowfalls", velocity=2):
    game = MyGame(width, height, title, velocity)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()