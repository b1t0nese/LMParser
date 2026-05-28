import arcade


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Rects With Cancel"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.rects = []
        self._is_draw = False
        self.start_pos = (0, 0)
        self.rect_size = (0, 0)

    def get_draw_rect(self):
        return (
            min(self.start_pos[0], self.start_pos[0] + self.rect_size[0]),
            min(self.start_pos[1], self.start_pos[1] + self.rect_size[1]),
            abs(self.rect_size[0]), abs(self.rect_size[1]))

    def on_draw(self):
        self.clear()
        for rect in self.rects + ([self.get_draw_rect()] if self._is_draw else []):
            arcade.draw_lbwh_rectangle_outline(*rect, arcade.color.WHITE, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self._is_draw = True
            self.start_pos = (x, y)
            self.rect_size = (0, 0)

    def on_mouse_release(self, x, y, button, modifiers):
        if self._is_draw and button == arcade.MOUSE_BUTTON_LEFT:
            if self.rect_size[0] != 0 or self.rect_size[1] != 0:
                self.rects.append(self.get_draw_rect())
            self._is_draw, self.rect_size = False, (0, 0)

    def on_mouse_motion(self, x, y, button, modifiers):
        if self._is_draw:
            self.rect_size = (x - self.start_pos[0], y - self.start_pos[1])

    def on_key_press(self, key, modifiers):
        if (modifiers & arcade.key.MOD_CTRL) and key == arcade.key.Z:
            if self.rects:
                self.rects.pop()


def setup_game(width=800, height=600, title="Rects With Cancel"):
    game = MyGame(width, height, title)
    game.setup()
    return game