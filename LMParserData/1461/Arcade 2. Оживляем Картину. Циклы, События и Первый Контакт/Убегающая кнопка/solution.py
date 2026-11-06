import random
import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Running button"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.rect_width = 100
        self.rect_height = 50
        self.random_rect()
        self.rect_color = arcade.color.BLUE
        self.is_active = True

    def random_rect(self):
        self.rect_left = random.randint(0, self.width - self.rect_width)
        self.rect_bottom = random.randint(0, self.height - self.rect_height)
        self.rect_center_x = self.rect_left + self.rect_width / 2
        self.rect_center_y = self.rect_bottom + self.rect_height / 2

    def on_draw(self):
        self.clear()
        arcade.draw_lbwh_rectangle_filled(
            self.rect_left, self.rect_bottom, 
            self.rect_width, self.rect_height, 
            self.rect_color)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.is_active:
            return
        if (self.rect_left <= x <= self.rect_left + self.rect_width and\
          self.rect_bottom <= y <= self.rect_bottom + self.rect_height):
            self.rect_color = arcade.color.RED
            self.is_active = False

    def on_mouse_motion(self, x, y, dx, dy):
        if not self.is_active:
            return

        distance_x = x - max(self.rect_left, min(x, self.rect_left + self.rect_width))
        distance_y = y - max(self.rect_bottom, min(y, self.rect_bottom + self.rect_height))
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        if distance < 10:
            self.random_rect()
            self.rect_color = arcade.color.BLUE
        elif distance < 20:
            self.rect_color = arcade.color.GREEN
        else:
            self.rect_color = arcade.color.BLUE


def setup_game(width=800, height=600, title="Running button"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()