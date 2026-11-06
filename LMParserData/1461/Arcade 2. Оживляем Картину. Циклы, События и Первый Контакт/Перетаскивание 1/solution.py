import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Moving Rect"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.rect_size = (0, 0)
        self.rect_pos = (0, 0)
        self._is_draw = None
        self.start_pos = (0, 0)
        self._is_moving = False
        self.deltas = (0, 0)

    def get_draw_rect(self):
        return (min(self.start_pos[0], self.start_pos[0] + self.rect_size[0]),
                min(self.start_pos[1], self.start_pos[1] + self.rect_size[1]),
                abs(self.rect_size[0]), abs(self.rect_size[1]))

    def on_draw(self):
        self.clear()
        if self._is_draw:
            arcade.draw_lbwh_rectangle_filled(*self.get_draw_rect(), arcade.color.WHITE)
        elif self.rect_size[0] > 0 and self.rect_size[1] > 0:
            arcade.draw_lbwh_rectangle_filled(*self.rect_pos, *self.rect_size, arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, modifiers):
        if self._is_draw is None:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self._is_draw = True
                self.start_pos = (x, y)
        elif not self._is_draw and button == arcade.MOUSE_BUTTON_LEFT:
            if (self.rect_pos[0] <= x <= self.rect_pos[0] + self.rect_size[0] and\
                self.rect_pos[1] <= y <= self.rect_pos[1] + self.rect_size[1]):
                self.deltas = (x - self.rect_pos[0], y - self.rect_pos[1])
                self._is_moving = True

    def on_mouse_motion(self, x, y, dx, dy):
        if self._is_draw:
            self.rect_size = (x - self.start_pos[0], y - self.start_pos[1])
            if abs(self.rect_size[0]) == 0 or abs(self.rect_size[1]) == 0:
                self.rect_size = (0, 0)
        if self._is_moving:
            self.rect_pos = (x - self.deltas[0], y - self.deltas[1])

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self._is_draw:
                rect = self.get_draw_rect()
                self.rect_pos, self.rect_size = (rect[0], rect[1]), (rect[2], rect[3])
                self._is_draw = False
            else:
                self._is_moving = False


def setup_game(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="Moving Rect"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()