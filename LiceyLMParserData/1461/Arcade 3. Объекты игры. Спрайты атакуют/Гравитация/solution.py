import arcade
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
TITLE = "Apple Tree"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.apple_list = arcade.SpriteList()
        self.apple_hit_list = arcade.SpriteList()
        self.apple_spawn = (700, 500)

    def setup(self):
        self.backround = arcade.load_texture("images/tree.png")
        for _ in range(10):
            apple = arcade.Sprite("images/apple.png", scale=1)
            apple.speed = 50
            apple.down = random.randint(apple.height // 2, 150)
            apple.center_x = random.randint((self.width - self.apple_spawn[0]) // 2,
                                            (self.width + self.apple_spawn[0]) // 2)
            apple.center_y = random.randint((self.height - self.apple_spawn[1]) // 2,
                                            (self.height + self.apple_spawn[1]) // 2)
            self.apple_list.append(apple)

    def on_update(self, delta_time):
        for apple in self.apple_hit_list:
            apple.center_y -= delta_time * apple.speed
            apple.speed += 10
            if apple.center_y <= apple.down:
                apple.center_y = apple.down
                self.apple_hit_list.remove(apple)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.backround, arcade.rect.XYWH(
            self.width // 2, self.height // 2, self.width, self.height))
        self.apple_list.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        apple_hit_list = arcade.get_sprites_at_point((x, y), self.apple_list)
        apple = apple_hit_list[0] if apple_hit_list else None
        if apple and not apple in self.apple_hit_list:
            self.apple_hit_list.append(apple)


def setup_game(width=1000, height=800, title="Apple Tree"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()