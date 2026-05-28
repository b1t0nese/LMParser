import arcade
from arcade import Camera2D
import os

MAIN_DIR = os.path.dirname(__file__)
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Higher and higher Runner"
TILE_SCALING = 0.5
GRAVITY = 0.5
PLAYER_SPEED = 6
CAMERA_LERP = 0.12
MAX_JUMPS = 1
JUMP_BUFFER = 0.12
JUMP_SPEED = 20
COYOTE_TIME = 0.08


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        arcade.set_background_color(arcade.color.SPANISH_SKY_BLUE)

        self.left, self.right = False, False
        self.jump_buffer, self.coyote_time = 0, 0
        self.on_ground = False

        self.camera = Camera2D()
        self.tile_map = arcade.load_tilemap(os.path.join(MAIN_DIR, "higher.tmx"), TILE_SCALING)
        self.player_sprite = arcade.Sprite(
            ":resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 0.5, 100, 100)
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self.player_sprite)
        self.objects = [self.tile_map.sprite_lists["platforms"], self.tile_map.sprite_lists["ground"]]
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.objects, GRAVITY)

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.tile_map.sprite_lists["platforms"].draw()
        self.tile_map.sprite_lists["ground"].draw()
        self.tile_map.sprite_lists["entry_exit"].draw()
        self.tile_map.sprite_lists["cool"].draw()
        self.player_spritelist.draw()

    def on_update(self, delta_time):
        if self.jump_buffer > 0:
            self.jump_buffer -= delta_time
        if self.coyote_time > 0:
            self.coyote_time -= delta_time

        on_ground = self.physics_engine.can_jump()
        if on_ground:
            self.coyote_time = COYOTE_TIME
        elif self.on_ground and not on_ground:
            if self.coyote_time <= 0:
                self.coyote_time = COYOTE_TIME
        if self.jump_buffer > 0 and on_ground:
            self.player_sprite.change_y = JUMP_SPEED
            self.jump_buffer, self.coyote_time = 0, 0
        self.on_ground = on_ground

        if self.left and not self.right:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif self.right and not self.left:
            self.player_sprite.change_x = PLAYER_SPEED
        else:
            self.player_sprite.change_x = 0

        if self.player_sprite.right > self.width:
            self.player_sprite.right = self.width
        elif self.player_sprite.left < 0:
            self.player_sprite.left = 0
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        if self.player_sprite.right > self.width:
            self.player_sprite.right = self.width
        self.physics_engine.update()

        cpx, cpy = self.camera.position
        view_w, view_h = self.camera.viewport_width / 2, self.camera.viewport_height / 2
        self.camera.position = (
            max(view_w, min(960 - view_w, cpx + (self.player_sprite.center_x - cpx) * CAMERA_LERP)),
            max(view_h, min(1920 - view_h, cpy + (self.player_sprite.center_y - cpy) * CAMERA_LERP)))

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left = True
        elif key == arcade.key.RIGHT:
            self.right = True
        elif key == arcade.key.UP:
            self.jump_buffer = JUMP_BUFFER

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left = False
        elif key == arcade.key.RIGHT:
            self.right = False
        elif key == arcade.key.UP:
            self.jump_buffer = 0


def setup_game(width=768, height=450, title="Moving Platforms Runner"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()