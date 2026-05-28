import arcade

PART = 35
SCREEN_WIDTH = PART * 20
SCREEN_HEIGHT = PART * 20
SCREEN_TITLE = "Storks"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        self.part = part
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

    def on_draw(self):
        self.clear()
        p = self.part

        def draw_eye(cx, cy, p):
            arcade.draw_circle_filled(cx, cy, p, arcade.color.WHITE)
            arcade.draw_circle_outline(cx, cy, p, arcade.color.BLACK, p / 10)
            arcade.draw_circle_filled(cx, cy, p / 3, arcade.color.BLACK)

        arcade.draw_triangle_filled(0, p * 16, p * 2, p * 16.33, p * 2, p * 15.66, arcade.color.RED)
        draw_eye(p * 3, p * 16, p)
        arcade.draw_arc_filled(p * 10, p * 16, p * 4, p * 4, arcade.color.WHITE, 180, 360)
        arcade.draw_arc_outline(p * 10, p * 16, p * 4, p * 4, arcade.color.BLACK, 180, 360, p / 5)
        arcade.draw_line(p * 4, p * 16, p * 16, p * 16, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 4, p * 15.66, p * 8, p * 15.66, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 12, p * 16, p * 16, p * 15, arcade.color.BLACK, p / 10)
        arcade.draw_arc_filled(p * 11.5, p * 16.5, p * 3, p * 3, arcade.color.BLACK, 45, 225)
        for x, y in [(p * 14, p * 16), (p * 14, p * 15.5)]:
            arcade.draw_circle_filled(x, y, p * 0.2, arcade.color.RED)
        for x1, y1, x2, y2, x3, y3 in [
            (p * 16, p * 16, p * 16.5, p * 16.33, p * 16.5, p * 15.66),
            (p * 16, p * 15, p * 16.5, p * 15.33, p * 16.5, p * 14.66)]:
            arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.RED)

        arcade.draw_triangle_filled(0, p * 11, p * 2, p * 12, p * 2, p * 11.5, arcade.color.RED)
        draw_eye(p * 3, p * 12, p)
        arcade.draw_line(p * 3, p * 11, p * 3, p * 8, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 3.291, p * 11, p * 3.291, p * 8, arcade.color.BLACK, p / 10)
        arcade.draw_arc_filled(p * 5, p * 8, p * 4, p * 4, arcade.color.WHITE, 180, 360)
        arcade.draw_arc_outline(p * 5, p * 8, p * 4, p * 4, arcade.color.BLACK, 180, 360, p / 5)
        arcade.draw_line(p * 3, p * 8, p * 7, p * 8, arcade.color.BLACK, p / 10)
        arcade.draw_arc_filled(p * 5.5, p * 8.5, p * 3, p * 3, arcade.color.BLACK, 45, 225)
        arcade.draw_line(p * 4.5, p * 6.1875, p * 4.5, p * 2, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 5.5, p * 6.1875, p * 5.5, p * 2, arcade.color.BLACK, p / 10)
        for x, y in [(p * 4.5, p * 4), (p * 5.5, p * 4)]:
            arcade.draw_circle_filled(x, y, p * 0.2, arcade.color.RED)
        for x1, y1, x2, y2, x3, y3 in [
            (p * 4.5, p * 2.5, p * 4.2, p * 2, p * 4.8, p * 2),
            (p * 5.5, p * 2.5, p * 5.2, p * 2, p * 5.8, p * 2)]:
            arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.RED)

        draw_eye(p * 17, p * 7, p)
        arcade.draw_triangle_filled(p * 19, p * 5, p * 17.5, p * 6.25, p * 17.875, p * 6.5, arcade.color.RED)
        arcade.draw_arc_filled(p * 12.5, p * 8.5, p * 3, p * 3, arcade.color.BLACK, 45, 225)
        arcade.draw_arc_filled(p * 12, p * 6, p * 4, p * 4, arcade.color.WHITE, 0, 180)
        arcade.draw_arc_outline(p * 12, p * 6, p * 4, p * 4, arcade.color.BLACK, 0, 180, p / 5)
        arcade.draw_arc_filled(p * 10.5, p * 8.5, p * 3, p * 3, arcade.color.BLACK, 135, 315)
        arcade.draw_line(p * 10, p * 6, p * 17, p * 6, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 14, p * 6.291, p * 16.25, p * 6.291, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 12, p * 6, p * 11, p * 2, arcade.color.BLACK, p / 10)
        arcade.draw_line(p * 12, p * 6, p * 13, p * 2, arcade.color.BLACK, p / 10)
        for x, y in [(p * 11.5, p * 4), (p * 12.5, p * 4)]:
            arcade.draw_circle_filled(x, y, p * 0.2, arcade.color.RED)
        for x1, y1, x2, y2, x3, y3 in [
            (p * 11, p * 2.5, p * 10.75, p * 2, p * 11.25, p * 2),
            (p * 13, p * 2.5, p * 12.75, p * 2, p * 13.25, p * 2),]:
            arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.RED)


def setup_game(width=400, height=400, title="Storks", part=20):
    game = MyGame(width, height, title, part)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()


if __name__ == "__main__":
    main()