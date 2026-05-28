import arcade

SCREEN_WIDTH = 820
SCREEN_HEIGHT = 620
SCREEN_TITLE = "Balls"
CELL_SIZE = 40
INDENT = 10

COLORS = [
    arcade.color.RED,
    arcade.color.GREEN,
    arcade.color.BLUE,
    arcade.color.YELLOW,
    arcade.color.VIOLET
]


class GridGame(arcade.Window):
    def __init__(self, screen_width, screen_height, screen_title, indent, cell_size):
        super().__init__(screen_width, screen_height, screen_title)

        self.indent = indent
        self.cell_size = cell_size
        self.rows = screen_height // cell_size
        self.cols = screen_width // cell_size

    def setup(self):
        self.grid = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]

    def on_draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size + self.cell_size // 2 + self.indent
                y = row * self.cell_size + self.cell_size // 2 + self.indent
                if self.grid[row][col] >- 1:
                    color = COLORS[self.grid[row][col]]
                    arcade.draw_circle_filled(x, y, self.cell_size // 2 - 2, color)
                arcade.draw_rect_outline(arcade.rect.XYWH(
                    x, y, self.cell_size, self.cell_size), arcade.color.GRAY, 1)

    def on_mouse_press(self, x, y, button, modifiers):
        col, row = int((x - self.indent) // self.cell_size), int((y - self.indent) // self.cell_size)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.grid[row][col] = (self.grid[row][col] + 1) % len(COLORS)
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                self.grid[row][col] = (self.grid[row][col] - 1) % len(COLORS)


def main():
    game = GridGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, INDENT, CELL_SIZE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()