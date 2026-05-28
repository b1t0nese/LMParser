import arcade
from pyglet.graphics import Batch

SCREEN_TITLE = "Игра супер круто"
SCREEN_WIDTH = 1220
SCREEN_HEIGHT = 850
PLAYER_SPEED = 5
GRAVITY = 0.5

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

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.scene["Platforms"])

        self.score = 0
        self.batch = Batch()

    def on_draw(self):
        self.clear()
        self.player_spritelist.draw()
        self.scene.draw()
        self.text = arcade.Text(f'Score: {self.score}', 10, self.height - 30, arcade.color.WHITE, 24)
        self.text.draw()

    def on_update(self, delta_time):
        coins_collizion = arcade.check_for_collision_with_list(self.player, self.tile_map.sprite_lists["Coins"])
        for coin in coins_collizion:
            self.tile_map.sprite_lists["Coins"].remove(coin)
            self.score += 1
        self.player.change_y -= GRAVITY
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED * 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0


def setup_game(width=1220, height=850, title="Аркадный Бегун"):
    game = MyGame(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()