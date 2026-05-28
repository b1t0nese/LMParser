import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tennis for two"
SCREEN_COLOR = arcade.color.DARK_GREEN

PADDLE_WIDTH = 10
PADDLE_COLOR = arcade.color.WHITE
PADDLE_SPEED = 80

BALL_SCALE = 0.2
BALL_SPEED = 200


class Ball(arcade.Sprite):
    def __init__(self, scale, speed, window):
        super().__init__("images/ball.png", scale)
        self.my_window = window
        self.change_x = 0
        self.change_y = 0
        self.speed = speed
        self.reset()

    def reset(self):
        self.center_x = self.my_window.width // 2
        self.center_y = self.my_window.height // 2
        angle = math.radians(random.randint(30, 60))
        direction = random.choice([-1, 1])
        self.change_x = direction * self.speed * math.cos(angle)
        self.change_y = self.speed * math.sin(angle)

    def update(self, delta_time):
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time


class Paddle(arcade.Sprite):
    def __init__(self, x, y, speed, window):
        super().__init__("images/paddle.png")
        self.my_window = window
        self.scale = 0.3
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def move_up(self):
        if self.center_y + self.speed < self.my_window.height:
            self.center_y += self.speed

    def move_down(self):
        if self.center_y - self.speed > 0:
            self.center_y -= self.speed


class TennisGame(arcade.Window):
    def __init__(self, width, height, title, screen_color):
        super().__init__(width, height, title)
        self.game_started = False
        self.screen_color = screen_color
        self.paddle_speed = PADDLE_SPEED
        self.ball_scale = BALL_SCALE
        self.ball_speed = BALL_SPEED

    def setup(self):
        arcade.set_background_color(self.screen_color)
        self.paddles = arcade.SpriteList()
        self.paddles.append(Paddle(20, self.height // 2, self.paddle_speed, self))
        self.paddles[0].score = 0
        self.paddles.append(Paddle(self.width - 20, self.height // 2, self.paddle_speed, self))
        self.paddles[1].score = 0
        self.ball_list = arcade.SpriteList()
        self.ball = Ball(self.ball_scale, self.ball_speed, self)
        self.ball_list.append(self.ball)

    def on_draw(self):
        self.clear()
        self.paddles.draw()
        self.ball_list.draw()
        arcade.draw_text(f"{self.paddles[0].score} : {self.paddles[1].score}",
                         self.width // 2, self.height - 50, 
                         arcade.color.WHITE, 36, anchor_x="center")

    def on_update(self, delta_time):
        if not self.game_started:
            return
        self.ball.update(delta_time)
        if self.ball.top >= self.height or self.ball.bottom <= 0:
            self.ball.change_y *= -1
        if arcade.check_for_collision_with_list(self.ball, self.paddles):
            self.ball.change_x *= -1
        if self.ball.right <= 0:
            self.paddles[1].score += 1
            self.ball.reset()
            self.game_started = False
        elif self.ball.left >= self.width:
            self.paddles[0].score += 1
            self.ball.reset()
            self.game_started = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if not self.game_started:
                self.ball.reset()
                self.game_started = True
        elif key == arcade.key.W:
            self.paddles[0].move_up()
        elif key == arcade.key.S:
            self.paddles[0].move_down()
        elif key == arcade.key.UP:
            self.paddles[1].move_up()
        elif key == arcade.key.DOWN:
            self.paddles[1].move_down()


def setup_game(width=800, height=600, title="Tennis for two",
               screen_color=arcade.color.DARK_GREEN):
    game = TennisGame(width, height, title, screen_color)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_COLOR)
    arcade.run()


if __name__ == "__main__":
    main()