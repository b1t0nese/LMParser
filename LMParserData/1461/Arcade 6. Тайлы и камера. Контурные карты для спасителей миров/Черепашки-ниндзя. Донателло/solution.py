import random
import arcade

SPEED = 4
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Donatello Game"
CELL_SIZE = 64


class GridGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.cell_size = CELL_SIZE
        self.all_sprites = arcade.SpriteList()
        self.wall_sprites = arcade.SpriteList()
        self.enemy_sprites = arcade.SpriteList()
        self.stone_texture = arcade.load_texture(":resources:images/tiles/stoneCenter.png")
        self.sand_texture = arcade.load_texture(":resources:images/tiles/sandCenter.png")
        self.player_texture = arcade.load_texture(":resources:images/enemies/slimeBlue.png")
        self.player1_texture = arcade.load_texture(":resources:images/enemies/slimePurple.png")
        self.enemy_texture = arcade.load_texture(":resources:images/enemies/fly.png")
        
        self.grid_width = SCREEN_WIDTH // (self.cell_size // 2)
        self.grid_height = SCREEN_HEIGHT // (self.cell_size // 2)

    def setup(self):
        self.all_sprites.clear()
        self.wall_sprites.clear()
        self.enemy_sprites.clear()
        
        self.grid = []
        scale = 0.5
        
        for y in range(0, self.grid_height, 2):
            row = []
            for x in range(0, self.grid_width, 2):
                if (x == 0 or y == 0 or 
                    x == self.grid_width - 2 or 
                    y == self.grid_height - 2):
                    sprite = arcade.Sprite()
                    sprite.texture = self.stone_texture
                    sprite.center_x = x * (self.cell_size // 2) + self.cell_size // 2
                    sprite.center_y = y * (self.cell_size // 2) + self.cell_size // 2
                    sprite.scale = scale
                    self.all_sprites.append(sprite)
                    self.wall_sprites.append(sprite)
                    row.append('stone')
                else:
                    sprite = arcade.Sprite()
                    sprite.texture = self.sand_texture
                    sprite.center_x = x * (self.cell_size // 2) + self.cell_size // 2
                    sprite.center_y = y * (self.cell_size // 2) + self.cell_size // 2
                    sprite.scale = scale
                    self.all_sprites.append(sprite)
                    row.append('sand')
            self.grid.append(row)
        
        self.player_sprite = arcade.Sprite()
        self.player_sprite.texture = self.player_texture
        self.player_sprite.center_x = 13 * self.cell_size
        self.player_sprite.center_y = 5 * self.cell_size
        self.player_sprite.scale = 0.5
        self.all_sprites.append(self.player_sprite)
        
        self.player1_sprite = arcade.Sprite()
        self.player1_sprite.texture = self.player1_texture
        self.player1_sprite.center_x = 2 * self.cell_size
        self.player1_sprite.center_y = 5 * self.cell_size
        self.player1_sprite.scale = 0.5
        self.all_sprites.append(self.player1_sprite)
        
        for i in range(5):
            enemy = arcade.Sprite()
            enemy.texture = self.enemy_texture
            enemy.scale = 0.3
            enemy.change_x = random.uniform(-4, 4)
            enemy.change_y = random.uniform(-4, 4)
            enemy.center_x = random.randint(self.cell_size * 2, SCREEN_WIDTH - self.cell_size * 2)
            enemy.center_y = random.randint(self.cell_size * 2, SCREEN_HEIGHT - self.cell_size * 2)
            self.all_sprites.append(enemy)
            self.enemy_sprites.append(enemy)
        
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, 
            self.wall_sprites
        )
        self.physics_engine1 = arcade.PhysicsEngineSimple(
            self.player1_sprite, 
            self.wall_sprites
        )
        
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player1_sprite.change_x = 0
        self.player1_sprite.change_y = 0

    def on_draw(self):
        self.clear()
        self.all_sprites.draw()

    def on_update(self, delta_time: float):
        self.player_sprite.center_x += self.player_sprite.change_x * SPEED
        self.player_sprite.center_y += self.player_sprite.change_y * SPEED
        self.player1_sprite.center_x += self.player1_sprite.change_x * SPEED
        self.player1_sprite.center_y += self.player1_sprite.change_y * SPEED
        
        for enemy in self.enemy_sprites:
            if enemy.left < 0 + self.grid_width * 2 or enemy.right > SCREEN_WIDTH - self.grid_width * 2:
                enemy.change_x *= -1
            if enemy.bottom < 0 + self.grid_height * 3 or enemy.top > SCREEN_HEIGHT - self.grid_height * 3.2:
                enemy.change_y *= -1
            
            enemy.center_x += enemy.change_x
            enemy.center_y += enemy.change_y
        
        self.physics_engine.update()
        self.physics_engine1.update()
        
        enemies_to_remove = []
        for enemy in self.enemy_sprites:
            if (arcade.check_for_collision(self.player_sprite, enemy) or 
                arcade.check_for_collision(self.player1_sprite, enemy)):
                enemies_to_remove.append(enemy)
        
        for enemy in enemies_to_remove:
            enemy.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -1
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 1
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 1
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -1
            
        if key == arcade.key.A:
            self.player1_sprite.change_x = -1
        elif key == arcade.key.D:
            self.player1_sprite.change_x = 1
        elif key == arcade.key.W:
            self.player1_sprite.change_y = 1
        elif key == arcade.key.S:
            self.player1_sprite.change_y = -1

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player_sprite.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0
            
        if key in (arcade.key.A, arcade.key.D):
            self.player1_sprite.change_x = 0
        elif key in (arcade.key.W, arcade.key.S):
            self.player1_sprite.change_y = 0


def setup_game(width=960, height=640, title="Donatello Game"):
    game = GridGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
