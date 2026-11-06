import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blinking stars"
BLINK_INTERVAL = 0.5

vp = arcade.load_texture("images/star.png")
nvp = arcade.load_texture("images/star0.png")


class BlinkingStar(arcade.Sprite):
    def __init__(self, filename, center_x, center_y, scale=1.0):
        super().__init__(filename, scale, center_x, center_y)
        
        self.is_blinking = False
        self.blink_timer = 0
        
        self.angle = random.uniform(0, 360)
        
        self.visible_texture = vp
        self.gone_texture = nvp
        
        self.texture = self.visible_texture 

    def update(self, delta_time: float = 1 / 60):
        if self.is_blinking:
            self.blink_timer += delta_time
            if self.blink_timer >= BLINK_INTERVAL:
                self.blink_timer = 0
                if self.texture == self.visible_texture:
                    self.texture = self.gone_texture
                else:
                    self.texture = self.visible_texture

    def toggle_blinking(self):
        self.is_blinking = not self.is_blinking
        
        if not self.is_blinking:
            self.texture = self.visible_texture
            self.blink_timer = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

    def setup(self):
        self.star_list = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        self.star_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if arcade.get_sprites_at_point((x, y), self.star_list):
            star = arcade.get_sprites_at_point((x, y), self.star_list)[0]
            star.toggle_blinking()
        else:
            star = BlinkingStar(filename="images/star.png", center_x=x, center_y=y, scale=0.1)
            self.star_list.append(star)

    def on_update(self, delta_time: float):
        self.star_list.update(delta_time)

def setup_game(width=800, height=600, title="Blinking stars"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
