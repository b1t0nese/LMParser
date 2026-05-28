import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 501, 501
TITLE = "Zoom"
K = 1.1

with open('points.txt') as file:
    data = [list(map(lambda x: float(x.replace(',', '.')), line.split(';')))
            for line in file.read().rstrip()[1:-1].split('), (')]


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.scal = 1.0

    def on_draw(self):
        self.clear()
        centr = [sum(map(lambda x: x[i], data)) / len(data) for i in range(2)]
        arcade.draw_polygon_outline([(
            x * self.scal + (self.width / 2 - self.scal * centr[0]),
            y * self.scal + (self.height / 2 - self.scal * centr[1]))
            for x, y in data], arcade.color.WHITE, 1)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.scal *= K
        elif key == arcade.key.DOWN:
            self.scal /= K


def setup_game(width=501, height=501, title="Zoom"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()