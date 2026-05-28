import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Drop balls"
VELOCITY = 2


class MyGame(arcade.Window):
    def __init__(self, width, height, title, velocity):
        super().__init__(width, height, title)
        self.circles_speed = velocity

    def setup(self):
        self.points = []
        self.speed = []
        self.radius = 20

    def process_circle(self, id):
        x, y = self.points[id]
        xs, ys = self.speed[id]
        x += xs
        y += ys
        if x - self.radius < 0 or x + self.radius > self.width:
            xs = -xs
        if y - self.radius < 0 or y + self.radius > self.height:
            ys = -ys
        self.points[id] = [x, y]
        self.speed[id] = [xs, ys]
        return x, y

    def on_draw(self):
        self.clear()
        for id in range(len(self.points)):
            x, y = self.process_circle(id)
            arcade.draw_circle_filled(x, y, self.radius, (255, 255, 255))

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.points.append([x, y])
            self.speed.append([-self.circles_speed, self.circles_speed])


def setup_game(width=800, height=600, title="Drop balls", velocity=2):
    game = MyGame(width, height, title, velocity)
    game.setup()
    return game


def main():
    game = setup_game()
    arcade.run()


if __name__ == "__main__":
    main()