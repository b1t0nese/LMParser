import arcade
from pyglet.graphics import Batch

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Real Jump"
# Физика и движение
GRAVITY = 2  # Пикс/с^2
MOVE_SPEED = 6  # Пикс/с
JUMP_SPEED = 40  # Начальный импульс прыжка, пикс/с
# Качество жизни прыжка
COYOTE_TIME = 0.08  # Сколько после схода с платформы можно ещё прыгнуть
JUMP_BUFFER = 0.12  # Если нажали прыжок чуть раньше приземления, мы его «запомним» (тоже лайфхак для улучшения качества жизни игрока)
MAX_JUMPS = 1  # С двойным прыжком всё лучше, но не сегодня
CAMERA_LERP = 0.12
WORLD_WIDTH = 2500
WORLD_HEIGHT = 1100

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.world_camera = arcade.Camera2D()
        self.gui_camera = arcade.Camera2D()

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
        self.left = self.right = self.jump_pressed = False
        self.time_since_ground = 999.0
        self.jumps_left = MAX_JUMPS

        self.score = 0
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.world_camera.use()
        self.player_spritelist.draw()
        self.scene.draw()
        self.gui_camera.use()
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
        if self.jump_pressed:
            if self.engine.can_jump(y_distance=6) or self.time_since_ground <= COYOTE_TIME:
                self.engine.jump(JUMP_SPEED)
                self.jump_pressed = False
        if self.player.center_x < self.player.width // 2 or self.player.center_x > WORLD_WIDTH - self.player.width:
            self.player.center_y -= JUMP_SPEED * dt
        # if self.player.center_y < self.player.height // 2:
        #     self.setup()
        #     return
        self.engine.update()

        target = (self.player.center_x, self.player.center_y)
        cx, cy = self.world_camera.position
        half_w = self.world_camera.viewport_width / 2
        half_h = self.world_camera.viewport_height / 2
        cam_x = max(half_w, min(WORLD_WIDTH - half_w, cx + (target[0] - cx) * CAMERA_LERP))
        cam_y = max(half_h, min(WORLD_HEIGHT - half_h, cy + (target[1] - cy) * CAMERA_LERP))
        self.world_camera.position = (cam_x, cam_y)
        self.gui_camera.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def on_key_press(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.left = True
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right = True
        elif key == arcade.key.UP:
            self.jump_pressed = True

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.left = False
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.right = False
        elif key == arcade.key.UP:
            self.jump_pressed = False


def setup_game(width=1220, height=850, title="Аркадный Бегун"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()