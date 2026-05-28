import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flying squares"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, side, color):
        super().__init__(width, height, title)
        self.side = side
        self.color = color
        self.speed = 2

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        if isinstance(self.color, str) and self.color.startswith("#"):
            hexcol = self.color.lstrip("#")
            if len(hexcol) == 6:
                self.color = (int(hexcol[0:2], 16), int(hexcol[2:4], 16), int(hexcol[4:6], 16))
            else:
                self.color = arcade.color.PINK
        self.points = [[450, 0], [450, 0]]

    def on_draw(self):
        self.clear()
        for point in self.points:
            arcade.draw_lbwh_rectangle_filled(
                point[0] - self.side / 2, point[1], self.side, self.side, self.color)

    def on_update(self, delta_time):
        self.points[0][0] -= self.speed
        self.points[0][1] += self.speed
        self.points[1][0] += self.speed
        self.points[1][1] += self.speed


def setup_game(width=900, height=600, title="Flying squares", side=100, color="#ff40ff"):
    game = MyGame(width, height, title, side, color)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()