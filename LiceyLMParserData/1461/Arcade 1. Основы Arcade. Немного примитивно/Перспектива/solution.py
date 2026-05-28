import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Perspective"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, width_rect, height_rect, color_rect: tuple[int, int, int]):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.w_width, self.w_height = width, height
        self.width_rect = width_rect
        self.height_rect = height_rect
        self.color_rect = color_rect

    def on_draw(self):
        self.clear()
        current_width, current_height = self.width_rect, self.height_rect
        current_color = list(self.color_rect)
        rectangles = []
        for i in range(1, 5):
            x, y = (self.w_width - current_width) // 2, (i + i - 1) * 20
            rectangles.append((x, y, current_width, current_height, tuple(current_color)))
            current_width -= 40
            current_height -= 20
            current_color[0] = max(0, current_color[0] - 20)
            current_color[1] = max(0, current_color[1] - 20)
        for rect in rectangles[::-1]:
            arcade.draw_lbwh_rectangle_filled(*rect)


def setup_game(width=900, height=600, title="Perspective", width_rect=500, height_rect=300, color_rect=(192, 255, 0)):
    game = MyGame(width, height, title, width_rect, height_rect, color_rect)
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()