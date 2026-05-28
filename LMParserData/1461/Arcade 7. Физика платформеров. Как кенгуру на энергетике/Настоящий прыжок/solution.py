import arcade
from pyglet.graphics import Batch

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
# Физика и движение
GRAVITY = 2
MOVE_SPEED = 6
JUMP_SPEED = 40
# Качество жизни прыжка
COYOTE_TIME = 0.08
JUMP_BUFFER = 0.12
MAX_JUMPS = 1
SCREEN_TITLE = "Real Jump"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.player = arcade.Sprite(":resources:/images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        self.player.center_x = 100
        self.player.center_y = 100
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self.player)

        self.tile_map = arcade.load_tilemap(":resources:/tiled_maps/level_1.json", scaling=0.5)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player, gravity_constant=GRAVITY,
            walls=self.scene["Bombs"], platforms=self.scene["Platforms"]
        )
        self.left = self.right = self.up = self.down = self.jump_pressed = False
        self.jump_buffer_timer = 0.0
        self.time_since_ground = 999.0
        self.jumps_left = MAX_JUMPS

        self.score = 0
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.player_spritelist.draw()
        self.scene.draw()
        self.text = arcade.Text(f'Score: {self.score}', 10, self.height - 30, arcade.color.WHITE, 24)
        self.text.draw()

    def on_update(self, dt):
        coins_collizion = arcade.check_for_collision_with_list(self.player, self.scene["Coins"])
        for coin in coins_collizion:
            self.tile_map.sprite_lists["Coins"].remove(coin)
            self.score += 1

        move = 0
        if self.left and not self.right:
            move = -MOVE_SPEED
        elif self.right and not self.left:
            move = MOVE_SPEED
        self.player.change_x = move
        grounded = self.engine.can_jump(y_distance=6)
        if grounded:
            self.time_since_ground = 0
            self.jumps_left = MAX_JUMPS
        else:
            self.time_since_ground += dt
        if self.jump_buffer_timer > 0:
            self.jump_buffer_timer -= dt
        if self.jump_pressed or (self.jump_buffer_timer > 0):
            can_coyote = (self.time_since_ground <= COYOTE_TIME)
            if grounded or can_coyote:
                self.engine.jump(JUMP_SPEED)
                self.jump_buffer_timer = 0
        self.engine.update()

    def on_key_press(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.left = True
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right = True
        elif key in (arcade.key.UP, arcade.key.W):
            self.up = True
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.down = True
        elif key == arcade.key.SPACE:
            self.jump_pressed = True
            self.jump_buffer_timer = JUMP_BUFFER

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.left = False
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right = False
        elif key in (arcade.key.UP, arcade.key.W):
            self.up = False
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.down = False
        elif key == arcade.key.SPACE:
            self.jump_pressed = False
            if self.player.change_y > 0:
                self.player.change_y *= 0.45


def setup_game(width=1220, height=850, title="Аркадный Бегун"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()