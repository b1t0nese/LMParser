import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Moving Square"
VELOCITY = 20


class MyGame(arcade.Window):
    def __init__(self, width, height, title, velocity):
        super().__init__(width, height, title)
        self.velocity = velocity

    def setup(self):
        self.square_size = 100
        self.square_x = self.width // 2
        self.square_y = self.height // 2

    def on_draw(self):
        self.clear()
        
        left = self.square_x - self.square_size / 2
        bottom = self.square_y - self.square_size / 2
        arcade.draw_lbwh_rectangle_filled(
            left, 
            bottom, 
            self.square_size, 
            self.square_size, 
            arcade.color.WHITE
        )

    def on_key_press(self, key, modifiers):    
        if key == arcade.key.UP:
            self.square_y += self.velocity
        elif key == arcade.key.DOWN:
            self.square_y -= self.velocity
        elif key == arcade.key.LEFT:
            self.square_x -= self.velocity
        elif key == arcade.key.RIGHT:
            self.square_x += self.velocity
        
        if self.square_x - self.square_size / 2 < 0:
            self.square_x = self.square_size / 2
        
        if self.square_x + self.square_size / 2 > self.width:
            self.square_x = self.width - self.square_size / 2
        
        if self.square_y - self.square_size / 2 < 0:
            self.square_y = self.square_size / 2
        
        if self.square_y + self.square_size / 2 > self.height:
            self.square_y = self.height - self.square_size / 2


def setup_game(width=800, height=600, title="Moving Square", velocity=20):
    game = MyGame(width, height, title, velocity)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()
