import arcade
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
TITLE = "Apple Tree"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg_texture = arcade.load_texture("images/tree.png")
        self.apple_list = arcade.SpriteList()
        self.apple_hit_list = arcade.SpriteList()

    def setup(self):
        for i in range(0, 10):
            apple = arcade.Sprite("images/apple.png")
            apple.center_x = random.randint(150, self.width - 150)
            apple.center_y = random.randint(150, self.height - 150)
            self.apple_list.append(apple)
        

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.bg_texture, arcade.rect.XYWH(self.width // 2, self.height // 2,
                                                                   self.width, self.height))
        self.apple_list.draw()
        self.apple_hit_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        for sprite in arcade.get_sprites_at_point((x, y), self.apple_list):
            apple = arcade.Sprite("images/apple.png")
            apple.center_x = sprite.center_x
            apple.center_y = sprite.center_y
            apple.stop_y = random.randint(0, 150)
            apple.speed = 0
            self.apple_hit_list.append(apple)
            sprite.kill()
        

    def on_update(self, delta_time: float):
        for sprite in  self.apple_hit_list:
            sprite.speed += 10
            if sprite.center_y - sprite.height / 2 > sprite.stop_y:
                sprite.center_y -= sprite.speed * delta_time
            

def setup_game(width=1000, height=800, title="Apple Tree"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
