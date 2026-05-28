import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Moving Rect"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.rect_size = (400, 300)
        self.rect_pos = (self.width // 2 - self.rect_size[0] // 2,
                         self.height // 2 - self.rect_size[1] // 2)
        self._is_moving = False
        self.deltas = (0, 0)

    def on_draw(self):
        self.clear()
        arcade.draw_lbwh_rectangle_filled(
            self.rect_pos[0], self.rect_pos[1], 
            self.rect_size[0], self.rect_size[1], 
            arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.rect_pos[0] <= x <= self.rect_pos[0] + self.rect_size[0] and\
          self.rect_pos[1] <= y <= self.rect_pos[1] + self.rect_size[1]):
            self.deltas = (x - self.rect_pos[0], y - self.rect_pos[1])
            self._is_moving = True

    def on_mouse_motion(self, x, y, dx, dy):
        if self._is_moving:
            self.rect_pos = (x - self.deltas[0], y - self.deltas[1])

    def on_mouse_release(self, x, y, button, modifiers):
        self._is_moving = False


def setup_game(width=800, height=600, title="Moving Rect"):
    game = MyGame(width, height, title)
    game.setup()
    return game