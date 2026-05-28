import arcade
import random

from pyglet.graphics import Batch

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Red Hat collects berries"

GIRL_SCALE = 0.5
GIRL_SPEED = 50

BUSH_COUNT = 15
BUSH_SCALE = 0.4
BERRY_SCALE = 0.2


class Girl(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__("images/girl.png", GIRL_SCALE, x, y)

    def update(self, delta_time):
        if self.speed:
            self.center_x += self.speed[0] * delta_time
            self.center_y += self.speed[1] * delta_time

    def set_speed(self, speed):
        self.speed = speed


class Bush(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__("images/bush.png", BUSH_SCALE, x, y)


class Berry(arcade.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__("images/berry.png", BERRY_SCALE, x, y)


class BerryGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("images/meadow.png")

    def setup(self):
        self.girl_list = arcade.SpriteList()
        girl = Girl()
        girl.center_x = girl.width // 2
        girl.center_y = self.height // 2
        self.girl_list.append(girl)
        self.girl_speed = (0, 0)

        self.bushes = arcade.SpriteList()
        for i in range(BUSH_COUNT):
            bush = Bush()
            bush.center_x = random.randint(int(bush.width // 2), int(self.width - bush.width // 2))
            bush.center_y = random.randint(int(bush.height // 2), int(self.height - bush.height // 2))
            self.bushes.append(bush)
        self.berries = arcade.SpriteList()
        for bush in self.bushes:
            self.berries.append(Berry(bush.center_x, bush.center_y))

        self.batch = Batch()
        self.score = 0
        self.score_text = arcade.Text(
            f"Ягод: {self.score}", self.width - self.width // 5, 20,
            arcade.color.BLACK, 20, batch=self.batch)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.rect.XYWH(
            self.width // 2, self.height // 2, self.width, self.height))
        self.bushes.draw()
        self.berries.draw()
        self.girl_list.draw()
        self.batch.draw()

    def on_update(self, delta_time):
        if self.girl_speed:
            self.girl_list[0].set_speed(self.girl_speed)
            self.girl_list[0].update(delta_time)
        girl_colision_with_berries = arcade.check_for_collision_with_list(
            self.girl_list[0], self.berries)
        for berry in girl_colision_with_berries:
            self.berries.remove(berry)
            self.score += 1
        self.score_text = arcade.Text(
            f"Ягод: {self.score}", self.width - self.width // 5, 20,
            arcade.color.BLACK, 20, batch=self.batch)

    def on_key_press(self, key, modifiers):
        x_speed, y_speed = 0, 0
        if key == arcade.key.W:
            y_speed = GIRL_SPEED
        elif key == arcade.key.S:
            y_speed = -GIRL_SPEED
        else:
            y_speed = self.girl_speed[1]
        if key == arcade.key.D:
            x_speed = GIRL_SPEED
        elif key == arcade.key.A:
            x_speed = -GIRL_SPEED
        else:
            x_speed = self.girl_speed[0]
        self.girl_speed = (x_speed, y_speed)

    def on_key_release(self, key, modifiers):
        x_speed, y_speed = 0, 0
        if not key == arcade.key.W:
            y_speed = None if y_speed > 0 else y_speed
        elif not key == arcade.key.S:
            y_speed = None if y_speed < 0 else y_speed
        else:
            y_speed = self.girl_speed[1]
        if not key == arcade.key.D:
            x_speed = None if x_speed > 0 else x_speed
        elif not key == arcade.key.A:
            x_speed = None if x_speed < 0 else x_speed
        else:
            x_speed = self.girl_speed[0]
        self.girl_speed = (x_speed, y_speed)


def setup_game(width=800, height=600, title="Red Hat collects berries"):
    game = BerryGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()