# недоделано

import arcade
import random

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
        self._is_started = False

    def setup(self):
        self.grid = [[random.randint(0, len(COLORS) - 1) if r < self.rows // 2 else -1
                      for c in range(self.cols)] for r in range(self.rows)]
        self._is_started = True

    def on_draw(self):
        self.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size + self.cell_size // 2 + self.indent
                y = row * self.cell_size + self.cell_size // 2 + self.indent
                if self.grid[row][col] > -1:
                    color = COLORS[self.grid[row][col]]
                    arcade.draw_circle_filled(x, y, self.cell_size // 2 - 2, color)
                arcade.draw_rect_outline(arcade.rect.XYWH(
                    x, y, self.cell_size, self.cell_size), arcade.color.GRAY, 1)

    def on_update(self, delta_time):
        filled_cols = [0 for _ in range(self.cols)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] > -1:
                    if self.grid[row - 1][col] == -1 and row - 1 >= 0:
                        self.grid[row - 1][col] = self.grid[row][col]
                        self.grid[row][col] = -1
                    filled_cols[col] += 1
        if self.rows in filled_cols and self._is_started:
            print("GAME OVERRRRRR")
            self._is_started = False

    def on_mouse_press(self, x, y, button, modifiers):
        col, row = int((x - self.indent) // self.cell_size), int((y - self.indent) // self.cell_size)
        if 0 <= row < self.rows and 0 <= col < self.cols and self._is_started:
            shariki, color = [], self.grid[row][col]
            if color > -1:
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if r + 1 < self.rows and self.grid[r][c] == color:
                            shariki.append((r, c))
                        elif c + 1 < self.cols and self.grid[r][c] == color:
                            shariki.append((r, c))
                if len(shariki) >= 3:
                    for r, c in shariki:
                        self.grid[r][c] = -1
                    for c in range(self.cols):
                        if self.grid[self.rows-1][c] == -1:
                            self.grid[self.rows-1][c] = random.randint(0, len(COLORS) - 1)


def main():
    game = GridGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, INDENT, CELL_SIZE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()