import arcade


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smile Silence"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.radius = radius

    def on_draw(self):
        self.clear()
        smile_prms = (self.width//2, self.height//2, 200, (255, 192, 0))
        arcade.draw_circle_filled(*smile_prms)
        arcade.draw_circle_filled(smile_prms[0]-smile_prms[2]//2,
                                  smile_prms[1]+smile_prms[2]//2, 15, (0, 0, 0))
        arcade.draw_circle_filled(smile_prms[0]+smile_prms[2]//2,
                                  smile_prms[1]+smile_prms[2]//2, 15, (0, 0, 0))


def setup_game(width=900, height=600, title="Smile Silence", radius=200):
    game = MyGame(width, height, title, radius)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()