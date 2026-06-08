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
MOVEMENT_SPEED = 8
CAMERA_LERP = 0.12


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


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.SKY_BLUE

        # Спрайты
        self.player = None
        self.tile_list = None
        self.cactus_list = None
        self.physics_engine = None

        # Камера
        self.world_camera = arcade.camera.Camera2D()
        self.gui_camera = ...
        self.setup()

    def setup(self):
        # Инициализация игрока
        self.player = Player()
        self.player.center_x = self.width // 2

        # Создание списков спрайтов
        self.tile_list = arcade.SpriteList()
        self.cactus_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Создание земли из тайлов
        for x in range(-TILE_SIZE, 25000, TILE_SIZE):
            self.texture = arcade.load_texture(':resources:images/tiles/brickTextureWhite.png')
            self.sprite = arcade.Sprite(self.texture, center_y=180, center_x=x, scale=0.5)
            self.tile_list.append(self.sprite)

        # Размещение кактусов
        for x in range(1200, 25000, 500):
            if random.randint(0, 10) > 4:
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

    def on_update(self, delta_time):
        self.player.update(delta_time)

        collided = arcade.check_for_collision_with_list(self.player, self.cactus_list)
        for cactus in collided:
            self.window.show_view(GameOverView())
            break

        camera_x = self.player.center_x
        camera_y = self.player.center_y

        self.world_camera.position = arcade.math.lerp_2d(self.world_camera.position, (camera_x, camera_y), CAMERA_LERP)

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.P:
            self.window.show_view(PauseView(self))
        elif key == arcade.key.SPACE:
            if self.player.jump_timer > 40:
                self.player.jump_timer = 0
                self.physics_engine.jump(JUMP_SPEED)
                

class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.camera = arcade.camera.Camera2D()

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.batch = Batch()
        self.text = [arcade.Text(
            "Pause",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2 + 50,
            arcade.color.WHITE,
            54,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch
        ),
            arcade.Text(
                "Press Esc",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 50,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                anchor_y="center",
                batch=self.batch
            )]
        self.batch.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)  # Возвращаемся в игру


class StartView(arcade.View):
    def on_draw(self):
        self.clear()
        self.batch = Batch()
        self.text = [arcade.Text(
            "Game",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2 + 50,
            arcade.color.WHITE,
            54,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch
        ),
            arcade.Text(
                "Press Any Key",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 50,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                anchor_y="center",
                batch=self.batch
            )]
        self.batch.draw()

    def on_key_press(self, key, modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.camera = arcade.camera.Camera2D()
        
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.batch = Batch()
        text = [arcade.Text(
            "Game Over",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2 + 50,
            arcade.color.WHITE,
            54,
            anchor_x="center",
            anchor_y="center",
            batch=self.batch
        ),
            arcade.Text(
                "Press Any Key",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 50,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                anchor_y="center",
                batch=self.batch
            )]
        self.batch.draw()

    def on_key_press(self, key, modifiers):
        game_view = GameView()
        self.window.show_view(game_view)
        

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
