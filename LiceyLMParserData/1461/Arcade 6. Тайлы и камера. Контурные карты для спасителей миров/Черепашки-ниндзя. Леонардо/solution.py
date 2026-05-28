import arcade

SPEED = 4
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Leonardo Game"


class GridGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.cell_size = 64
        self.all_sprites = arcade.SpriteList()
        self.wall_sprites = arcade.SpriteList()

        self.stone_texture = arcade.load_texture(":resources:images/tiles/stoneCenter.png")
        self.sand_texture = arcade.load_texture(":resources:images/tiles/sandCenter.png")
        self.player_texture = arcade.load_texture(":resources:images/enemies/slimeBlue.png")

        self.cellS2 = (self.cell_size // 2)
        self.grid_width = self.width // self.cellS2
        self.grid_height = self.height // self.cellS2

    def setup(self):
        self.all_sprites.clear()
        self.wall_sprites.clear()
        
        self.grid = []
        for y in range(0, self.grid_height, 2):
            row = []
            for x in range(0, self.grid_width, 2):
                if (x == 0 or y == 0 or x == self.grid_width - 2 or y == self.grid_height - 2):
                    sprite = arcade.Sprite(self.stone_texture, 0.5, (x + 1) * self.cellS2, (y + 1) * self.cellS2)
                    self.all_sprites.append(sprite)
                    self.wall_sprites.append(sprite)
                    row.append('stone')
                else:
                    self.all_sprites.append(arcade.Sprite(
                        self.sand_texture, 0.5, (x + 1) * self.cellS2, (y + 1) * self.cellS2))
                    row.append('sand')
            self.grid.append(row)

        self.player_sprite = arcade.Sprite(self.player_texture, 0.5, self.width // 2, self.height // 2)
        self.all_sprites.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_sprites)
        self.player_sprite.change_x, self.player_sprite.change_y = 0, 0

    def on_draw(self):
        self.clear()
        self.all_sprites.draw()

    def on_update(self, delta_time: float):
        self.player_sprite.center_x += self.player_sprite.change_x * SPEED
        self.player_sprite.center_y += self.player_sprite.change_y * SPEED
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -1
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 1
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 1
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -1

    def on_key_release(self, key, modifiers):
        if (key == arcade.key.LEFT and self.player_sprite.change_x < 0) or\
           (key == arcade.key.RIGHT and self.player_sprite.change_x > 0):
            self.player_sprite.change_x = 0
        elif (key == arcade.key.UP and self.player_sprite.change_y > 0) or\
             (key == arcade.key.DOWN and self.player_sprite.change_y < 0):
            self.player_sprite.change_y = 0


def setup_game(width=960, height=640, title="Leonardo Game"):
    game = GridGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()