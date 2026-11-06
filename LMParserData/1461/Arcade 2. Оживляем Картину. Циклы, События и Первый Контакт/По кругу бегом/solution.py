import math
import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Rounding circle"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.angle = 0
        self.speed = 0
        self.orbit_radius = 100
        self.circle_radius = 20
        self.circle_color = arcade.color.YELLOW

    def on_draw(self):
        self.clear()

        center_x = self.width // 2
        center_y = self.height // 2
        
        x = center_x + self.orbit_radius * math.cos(self.angle)
        y = center_y + self.orbit_radius * math.sin(self.angle)
        
        arcade.draw_circle_filled(x, y, self.circle_radius, self.circle_color)

    def on_update(self, delta_time):
        self.angle += self.speed

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.speed += 0.01
        elif key == arcade.key.LEFT:
            self.speed -= 0.01


def setup_game(width=800, height=600, title="Rounding circle"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
