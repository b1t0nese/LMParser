import arcade
from arcade.gui import UIManager, UITextureButton
from arcade.gui.widgets.layout import UIAnchorLayout, UIBoxLayout

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pink Worm And Others"
SPEED = 2


class Player(arcade.Sprite):
    def __init__(self, n):
        super().__init__()
        self.hero = n

        self.heros = [[arcade.load_texture(":resources:images/enemies/wormPink.png"),
                       arcade.load_texture(":resources:images/enemies/slimePurple.png")],
                      [arcade.load_texture(":resources:images/enemies/wormGreen.png"),
                       arcade.load_texture(":resources:images/enemies/wormGreen_move.png")],
                      [arcade.load_texture(":resources:images/enemies/frog.png"),
                       arcade.load_texture(":resources:images/enemies/frog_move.png")]
        ]

        self.is_up = False
        self.is_down = False
        self.is_left = False
        self.is_right = False

        self.texture = arcade.load_texture(":resources:images/enemies/wormPink.png")
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self)

        self.animation_timer = 0
        self.current_texture = 0

    def update(self, delta_time):
        if self.is_up is True:
            self.center_y += SPEED
        if self.is_down is True:
            self.center_y -= SPEED
        if self.is_left is True:
            self.center_x -= SPEED
        if self.is_right is True:
            self.center_x += SPEED

        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.animation_timer = 0
            if self.current_texture != self.heros[self.hero][0]:
                self.current_texture = self.heros[self.hero][0]
            else:
                self.current_texture = self.heros[self.hero][1]
            self.texture = self.current_texture


class MyGUIWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)

        self.manager = UIManager()
        self.manager.enable()

        self.anchor_layout = UIAnchorLayout()
        self.main_box = UIBoxLayout(vertical=True, space_between=400)
        self.box_layout = UIBoxLayout(vertical=False, space_between=10)
        self.player_box_layout = UIBoxLayout(vertical=False, space_between=10)

        self.setup_widgets()

        self.main_box.add(self.box_layout)
        self.main_box.add(self.player_box_layout)
        self.anchor_layout.add(self.main_box)
        self.manager.add(self.anchor_layout)

    def setup_widgets(self):
        texture_normal = arcade.load_texture(":resources:/gui_basic_assets/button/red_normal.png")
        texture_hovered = arcade.load_texture(":resources:/gui_basic_assets/button/red_hover.png")
        texture_pressed = arcade.load_texture(":resources:/gui_basic_assets/button/red_press.png")
        hero_1_button = UITextureButton(texture=texture_normal,
                                         texture_hovered=texture_hovered,
                                         texture_pressed=texture_pressed,
                                         scale=1.0,
                                         text="Pink Worm")
        hero_1_button.on_click = self.change_hero
        hero_2_button = UITextureButton(texture=texture_normal,
                                        texture_hovered=texture_hovered,
                                        texture_pressed=texture_pressed,
                                        scale=1.0,
                                        text="Green Worm")
        hero_2_button.on_click = self.change_hero1
        hero_3_button = UITextureButton(texture=texture_normal,
                                        texture_hovered=texture_hovered,
                                        texture_pressed=texture_pressed,
                                        scale=1.0,
                                        text="Frog")
        hero_3_button.on_click = self.change_hero2
        self.box_layout.add(hero_1_button)
        self.box_layout.add(hero_2_button)
        self.box_layout.add(hero_3_button)

    def setup(self):
        self.player = Player(0)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2

    def change_hero(self, event):
        self.player.hero = 0

    def change_hero1(self, event):
        self.player.hero = 1

    def change_hero2(self, event):
        self.player.hero = 2

    def on_draw(self):
        self.clear()
        self.player.player_spritelist.draw()
        self.manager.draw()

    def on_update(self, delta_time: float) -> bool | None:
        self.player.update(delta_time)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.is_up = True
        elif key == arcade.key.DOWN:
            self.player.is_down = True

        if key == arcade.key.LEFT:
            self.player.is_left = True
        elif key == arcade.key.RIGHT:
            self.player.is_right = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.is_up = False
        elif key == arcade.key.DOWN:
            self.player.is_down = False

        if key == arcade.key.LEFT:
            self.player.is_left = False
        elif key == arcade.key.RIGHT:
            self.player.is_right = False


def setup_game(width=800, height=600, title="Pink Worm And Others"):
    game = MyGUIWindow(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()