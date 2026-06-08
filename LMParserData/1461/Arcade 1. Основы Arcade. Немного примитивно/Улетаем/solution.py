import arcade

PART = 20
SCREEN_WIDTH = PART * 36
SCREEN_HEIGHT = PART * 15
SCREEN_TITLE = "Flying storks"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        self.part = part
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.storks = [0, self.width // 2, self.width]

    def on_draw(self):
        self.clear()
        p = self.part

        for i in range(0, len(self.storks)):
            arcade.draw_triangle_filled(0+self.storks[i], p*16-p*5, p*2+self.storks[i], p*16.33-p*5, p*2+self.storks[i], p*15.66-p*5, arcade.color.RED)
            arcade.draw_circle_filled(p*3+self.storks[i], p*16-p*5, p, arcade.color.WHITE)
            arcade.draw_circle_outline(p*3+self.storks[i], p*16-p*5, p, arcade.color.BLACK, p/10)
            arcade.draw_circle_filled(p*3+self.storks[i], p*16-p*5, p/3, arcade.color.BLACK)
            arcade.draw_arc_filled(p*10+self.storks[i], p*16-p*5, p*4, p*4, arcade.color.WHITE, 180, 360)
            arcade.draw_arc_outline(p*10+self.storks[i], p*16-p*5, p*4, p*4, arcade.color.BLACK, 180, 360, p/5)
            arcade.draw_line(p*4+self.storks[i], p*16-p*5, p*16+self.storks[i], p*16-p*5, arcade.color.BLACK, p/10)
            arcade.draw_line(p*4+self.storks[i], p*15.66-p*5, p*8+self.storks[i], p*15.66-p*5, arcade.color.BLACK, p/10)
            arcade.draw_line(p*12+self.storks[i], p*16-p*5, p*16+self.storks[i], p*15-p*5, arcade.color.BLACK, p/10)
            arcade.draw_arc_filled(p*11.5+self.storks[i], p*16.5-p*5, p*3, p*3, arcade.color.BLACK, 45, 225)
            arcade.draw_circle_filled(p*14+self.storks[i], p*16-p*5, p*0.2, arcade.color.RED)
            arcade.draw_circle_filled(p*14+self.storks[i], p*15.5-p*5, p*0.2, arcade.color.RED)
            arcade.draw_triangle_filled(p*16+self.storks[i], p*16-p*5, p*16.5+self.storks[i], p*16.33-p*5, p*16.5+self.storks[i], p*15.66-p*5, arcade.color.RED)
            arcade.draw_triangle_filled(p*16+self.storks[i], p*15-p*5, p*16.5+self.storks[i], p*15.33-p*5, p*16.5+self.storks[i], p*14.66-p*5, arcade.color.RED)

    def on_update(self, delta_time):
        for i in range(0, len(self.storks)):
            self.storks[i] -= self.width * 0.05 * delta_time * 1.6

        for i in range(0, len(self.storks)):
            if self.storks[i] <= self.width * -1 // 2:
                self.storks.remove(self.storks[i])
                self.storks.append(self.width)


def setup_game(width=720, height=300, title="Flying storks", part=20):
    game = MyGame(width, height, title, part)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()