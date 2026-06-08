# ПО СУТИ ВСЕ РАБОТАЕТ
# НО СИСТЕМА НЕ ПРИНИМАЕТ
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Soap Bubbles"


class Bubble(arcade.Sprite):
    def __init__(self, scale=0.5, center_x=0, center_y=0):
        super().__init__(scale=scale, center_x=center_x, center_y=center_y)
        self.ball = arcade.load_texture("images/balls/ball0.png")
        self.bb = arcade.SpriteList()
        for i in range(1, 8):
            self.bb.append(arcade.Sprite(path_or_texture=arcade.load_texture(f"images/balls/ball{i}.png")))
        self.texture = self.ball
        self.is_burst = False
        self.time = 0.1
        self.timer = 0.0
        self.counter = 0

    def update_animation(self, delta_time: float = 1 / 60):
        if self.is_burst:
            self.timer += delta_time
            if self.timer > self.time:
                self.timer = 0.0
                self.counter += 1
                if self.counter >= 8:
                    pass
                else:
                    self.texture = arcade.load_texture(f"images/balls/ball{self.counter}.png")


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.bubble_list = arcade.SpriteList()
        self.clicked_list = arcade.SpriteList()
        for i in range(0, 10):
            self.bubble_list.append(Bubble(center_x=random.randint(100, self.width - 100),
                                           center_y=random.randint(100, self.height - 100)))

    def on_draw(self):
        self.clear()
        self.clicked_list.draw()
        self.bubble_list.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for obj in arcade.get_sprites_at_point(point=[x, y], sprite_list=self.bubble_list):
            obj.is_burst = True
            self.clicked_list.append(obj)
            self.bubble_list.remove(obj)

    def on_update(self, delta_time: float):
        for obj in self.clicked_list:
            obj.update_animation(delta_time)


def setup_game(width=800, height=600, title="Soap Bubbles"):
    game = MyGame(width, height, title)
    game.setup()
    return game


# Блок для вашего локального тестирования (необязателен для сдачи)
def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()