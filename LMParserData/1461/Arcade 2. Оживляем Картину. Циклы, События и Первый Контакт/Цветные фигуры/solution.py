import arcade
from arcade.types import Color

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Color points"
COLORS = ['#ffc000', '#dc00a9', '#0065ac', '#22ad00']


class MyGame(arcade.Window):
    def __init__(self, width, height, title, colors):
        super().__init__(width, height, title)
        self.colors = colors

    def setup(self):
        self.keys_pressed = set()
        self.points = []
        self.radius = 10
        for i in range(len(self.colors)):
            if isinstance(self.colors[i], str) and self.colors[i].startswith("#"):
                hex_color = self.colors[i].lstrip("#")
                if len(hex_color) == 6:
                    self.colors[i] = Color(
                        int(hex_color[0:2], 16),
                        int(hex_color[2:4], 16),
                        int(hex_color[4:6], 16)
                    )
        self.color_id = 0

    def on_draw(self):
        self.clear()
        for point in self.points:
            x, y, color, figure = point
            if figure == "circle":
                arcade.draw_circle_filled(x, y, self.radius, color)
            elif figure == "rect":
                arcade.draw_lbwh_rectangle_filled(x, y, self.radius * 2, self.radius * 2, color)

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        
    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            figure = "circle"
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            figure = "rect"
        self.color_id += 1
        if self.color_id>=len(self.colors):
            self.color_id = 0
        if arcade.key.LCTRL in self.keys_pressed or arcade.key.RCTRL in self.keys_pressed:
            color = Color(255, 255, 255)
            print(color, "privet")
        else:
            color = self.colors[self.color_id]
        self.points.append((x, y, color, figure))


def setup_game(width=800, height=600, title="Color points", colors=None):
    game = MyGame(width, height, title, COLORS[:] if colors is None else colors)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()