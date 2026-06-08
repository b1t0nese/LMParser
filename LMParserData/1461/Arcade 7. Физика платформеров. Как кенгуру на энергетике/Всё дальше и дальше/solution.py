import arcade
from arcade import Camera2D
from pyglet.graphics import Batch

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
        arcade.set_background_color(arcade.color.SPANISH_SKY_BLUE)
        
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        
        self.left_pressed = False
        self.right_pressed = False
        self.down_pressed = False
        self.up_pressed = False
        
        self.jump_buffer_timer = 0
        self.coyote_time_timer = 0
        self.jumps_remaining = MAX_JUMPS
        self.was_on_ground = False

        self.batch = Batch()
        self.score = 0

    def setup(self):
        self.camera = Camera2D()
        self.camera_ui = Camera2D()
        
        tile_map = arcade.load_tilemap("further_and_further.tmx", scaling=TILE_SCALING)

        self.platforms = tile_map.sprite_lists["platforms"]
        self.ground = tile_map.sprite_lists["ground"]
        self.lava_water = tile_map.sprite_lists["lava_water"]
        self.ladders = tile_map.sprite_lists["ladders"]

        self.keys = arcade.SpriteList()
        for i in range(410, 660, 50):
            key = arcade.Sprite(
                ":resources:images/items/keyYellow.png",
                scale=0.4
            )
            key.center_x = i
            key.center_y = 370
            self.keys.append(key)
        
        self.player_sprite = arcade.Sprite(
            ":resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5
        )
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self.player_sprite)

        self.objects = []
        self.objects.append(self.platforms)
        self.objects.append(self.ground)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            platforms=self.objects,
            gravity_constant=GRAVITY,
            ladders=self.ladders
        )

    def on_draw(self):
        self.clear()
        
        self.camera.use()

        self.platforms.draw()
        self.ground.draw()
        self.lava_water.draw()
        self.ladders.draw()
        self.keys.draw()
        self.player_spritelist.draw()

        self.camera_ui.use()
        self.batch.draw()

    def on_update(self, delta_time):
        self.text = arcade.Text(f'Score: {self.score}', 10, self.height - 30, arcade.color.WHITE,
                        24, batch=self.batch)
        
        c = arcade.check_for_collision_with_list(self.player_sprite, self.lava_water)
        for obj in c:
            self.player_sprite.center_x = 100
            self.player_sprite.center_y = 100

        c = arcade.check_for_collision_with_list(self.player_sprite, self.keys)
        for obj in c:
            self.keys.remove(obj)
            self.score += 1
        
        on_ladder = self.physics_engine.is_on_ladder()
        if on_ladder:
            if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = 6
            elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -6
            else:
                self.player_sprite.change_y = 0
        
        on_ground = self.physics_engine.can_jump()
        
        if self.jump_buffer_timer > 0 and on_ground:
            self.player_sprite.change_y = JUMP_SPEED
            self.jump_buffer_timer = 0
        
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_SPEED
        else:
            self.player_sprite.change_x = 0
        
        self.physics_engine.update()
        
        target_x = self.player_sprite.center_x - SCREEN_WIDTH / 2
        target_y = self.player_sprite.center_y - SCREEN_HEIGHT / 2
        
        target_x = max(0, min(target_x, 1920 - SCREEN_WIDTH))
        target_y = max(0, min(target_y, 960 - SCREEN_HEIGHT))
        
        target = (self.player_sprite.center_x, self.player_sprite.center_y)
        cx, cy = self.camera.position
        smooth = (cx + (target[0] - cx) * CAMERA_LERP,
                  cy + (target[1] - cy) * CAMERA_LERP)

        half_w = self.camera.viewport_width / 2
        half_h = self.camera.viewport_height / 2
        world_w = 1920
        world_h = 1920

        cam_x = max(half_w, min(world_w - half_w, smooth[0]))
        cam_y = max(half_h, min(world_h - half_h, smooth[1]))

        self.camera.position = (cam_x, cam_y)
        
        self.was_on_ground = on_ground

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.jump_buffer_timer = JUMP_BUFFER

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False
        elif key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.jump_buffer_timer = 0

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False


def setup_game(width=768, height=450, title="Moving Platforms Runner"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
