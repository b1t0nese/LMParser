import arcade
import random
import math
from pyglet.graphics import Batch

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Побежали!"
TILE_SIZE = 64
GRAVITY = 1.2
JUMP_SPEED = 25
MOVEMENT_SPEED = 10
CAMERA_LERP = 0.12


class GreenSparkParticle(arcade.SpriteCircle):
    def __init__(self, x, y):
        # Случайный оттенок зеленого
        color = random.choice([
            (100, 255, 100, 255),
            (50, 255, 50, 255),
            (150, 255, 150, 255),
            (200, 255, 200, 255),
            (100, 200, 100, 255)
        ])
        size = random.randint(3, 6)
        super().__init__(size, color)
        self.center_x = x
        self.center_y = y
        # Начальная скорость в случайном направлении
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 5)
        self.change_x = math.cos(angle) * speed
        self.change_y = math.sin(angle) * speed
        self.alpha = 255
        self.lifetime = random.uniform(0.3, 0.8)
        self.time_alive = 0
        self.scale = 1.0

    def update(self, delta_time):
        # Движение с учетом гравитации
        self.change_y -= 0.1
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Уменьшение прозрачности и размера
        self.alpha -= 4
        self.scale_x *= 0.97
        self.scale_y *= 0.97

        # Увеличение времени жизни
        self.time_alive += delta_time


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.walk_textures = [arcade.load_texture(':resources:images/alien/alienBlue_walk1.png'),
                              arcade.load_texture(':resources:images/alien/alienBlue_walk2.png')]
        self.texture = self.walk_textures[0]
        self.center_y = TILE_SIZE + self.height / 2
        self.change_x = 0
        self.change_y = 0
        self.animation_timer = 0
        self.current_texture = 0
        self.jump_timer = 0
        self.is_jumping = False
        self.center_y = 300

        self.texture = arcade.load_texture(':resources:images/alien/alienBlue_walk1.png')
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self)
        self.x_speed = MOVEMENT_SPEED

    def update(self, delta_time):
        self.center_x += self.x_speed

        self.animation_timer += 1
        self.jump_timer += 1
        if self.animation_timer >= 10:
            self.animation_timer = 0
            if self.current_texture != self.walk_textures[0]:
                self.current_texture = self.walk_textures[0]
            else:
                self.current_texture = self.walk_textures[1]
            self.texture = self.current_texture

    def jump(self):
        ...


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background_color = arcade.color.SKY_BLUE

        # Спрайты
        self.player = None
        self.tile_list = None
        self.cactus_list = None
        self.spark_particles = None
        self.physics_engine = None

        # Камера
        self.world_camera = arcade.camera.Camera2D()
        self.gui_camera = ...

    def setup(self):
        # Инициализация игрока
        self.player = Player()
        self.player.center_x = self.width // 2

        # Создание списков спрайтов
        self.tile_list = arcade.SpriteList()
        self.cactus_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.spark_particles = arcade.SpriteList()

        # Создание земли из тайлов
        for x in range(-TILE_SIZE, 25000, TILE_SIZE):
            self.texture = arcade.load_texture(':resources:images/tiles/brickTextureWhite.png')
            self.sprite = arcade.Sprite(self.texture, center_y=180, center_x=x, scale=0.5)
            self.tile_list.append(self.sprite)

        # Размещение кактусов
        for x in range(300, 25000, 300):
            if random.randint(0, 10) > 3:
                self.texture = arcade.load_texture(':resources:images/tiles/cactus.png')
                self.sprite = arcade.Sprite(self.texture, center_y=243, center_x=x + random.randint(-100, 100), scale=0.5)
                self.cactus_list.append(self.sprite)

        # Физический движок
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player,
            gravity_constant=GRAVITY,
            platforms=self.tile_list
        )

    def on_draw(self):
        self.clear()
        self.world_camera.use()
        self.player.player_spritelist.draw()
        self.tile_list.draw()
        self.cactus_list.draw()
        self.spark_particles.draw()

    def create_green_sparks(self, x, y):
        for i in range(0, 10):
            self.spark_particles.append(GreenSparkParticle(x, y))

    def on_update(self, delta_time):
        self.player.update(delta_time)

        collided = arcade.check_for_collision_with_list(self.player, self.cactus_list)
        for cactus in collided:
            self.create_green_sparks(cactus.center_x, cactus.center_y)

        for obj in self.spark_particles:
            obj.update(delta_time)
            if obj.time_alive > obj.lifetime:
                self.spark_particles.remove(obj)

        camera_x = self.player.center_x
        camera_y = self.player.center_y

        self.world_camera.position = arcade.math.lerp_2d(self.world_camera.position, (camera_x, camera_y), CAMERA_LERP)

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if self.player.jump_timer > 60:
            self.player.jump_timer = 0
            self.physics_engine.jump(JUMP_SPEED)


def setup_game(width=1000, height=600, title="Побежали!"):
    game = GameWindow(width, height, title)
    game.setup()
    return game


def main():
    window = setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
