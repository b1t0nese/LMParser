import arcade

SCREEN_TITLE = "Origami Cat"
PART = 25


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        self.part = part
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.BEIGE)
        self.lines = [
            ((1, 1), (4, 4)),
            ((4, 4), (6, 4)),
            ((6, 4), (9, 1)),
            ((9, 1), (8, 7)),
            ((1, 1), (2, 7)),
            ((2, 7), (4, 4)),
            ((6, 4), (8, 7)),
            ((5, 4), (5, 16)),
            ((2, 7), (5, 10)),
            ((8, 7), (5, 10)),
            ((3, 8), (5, 16)),
            ((7, 8), (5, 16)),
            ((7, 8), (11, 12)),
            ((11, 12), (11, 16)),
            ((5, 16), (9, 16)),
            ((11, 12), (8, 18)),
            ((8, 18), (11, 16))
        ]

    def on_draw(self):
        self.clear()
        for a, b in self.lines:
            scr_w, scr_h = self.width // self.part, self.height // self.part
            arcade.draw_line(a[0] * self.part, (scr_h - a[1]) * self.part, 
                             b[0] * self.part, (scr_h - b[1]) * self.part,
                             arcade.color.COOL_BLACK, 4)


def setup_game(width=300, height=475, title="Origami Cat", part=25):
    game = MyGame(width, height, title, part)
    return game


def main():
    setup_game(PART * 12, PART * 19, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()