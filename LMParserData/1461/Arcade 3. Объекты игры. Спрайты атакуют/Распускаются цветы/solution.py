import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Цветущие лилии"
FLOWER_COUNT = 10
ANIMATION_SPEED = 0.2


class Flower(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(center_x=x, center_y=y, scale=0.3)

        self.animation_frame = 0
        self.is_blooming = False
        self.animation_timer = 0

        for i in range(9):
            self.append_texture(arcade.load_texture(f"images/flowers/flower{i}.png"))
        self.set_texture(self.animation_frame)

    def update(self, delta_time: float = 1 / 60):
        if self.is_blooming:
            self.animation_timer += delta_time
            if self.animation_timer >= ANIMATION_SPEED:
                self.animation_timer = 0
                self.animation_frame += 1
                self.set_texture(self.animation_frame)
                if self.animation_frame >= 8:
                    self.is_blooming = False

    def start_blooming(self):
        self.is_blooming = True
        # self.animation_frame = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        self.background = arcade.load_texture("images/meadow.png")
        self.flower_list = arcade.SpriteList()
        for i in range(FLOWER_COUNT):
            flower = Flower(random.randint(50, self.width - 50), random.randint(50, self.height - 50))
            self.flower_list.append(flower)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background, arcade.rect.XYWH(
            self.width // 2, self.height // 2, self.width, self.height))
        self.flower_list.draw()

    def on_update(self, delta_time):
        for flower in self.flower_list:
            flower.update(delta_time)

    def on_mouse_press(self, x, y, button, modifiers):
        flower_hit_list = arcade.get_sprites_at_point((x, y), self.flower_list)
        for flower in flower_hit_list:
            flower.start_blooming()


def setup_game(width=1000, height=500, title="Цветущие лилии"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()