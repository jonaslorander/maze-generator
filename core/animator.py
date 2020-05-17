import pygame

class Animator():
    def __init__(self, window, maze, size):
        self.window = window
        self.cell_order = maze.cell_order
        self.size = size
        self.wall = 2 # int(self.size / 10)

    def animate(self):
        black = (0, 0, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)

        # Draw a regtangle for each cell
        for cell in self.cell_order:
            rect = (cell.x * self.size, cell.y * self.size, self.size, self.size)
            pygame.draw.rect(self.window.screen, white, rect)

            # Check if we should draw the cells left wall
            if cell.lw:
                x0 = cell.x * self.size
                y0 = cell.y * self.size
                x1 = self.wall
                y1 = self.size
                pygame.draw.rect(self.window.screen, black, (x0, y0, x1, y1))

            # Check if we should draw the cells right wall
            if cell.rw:
                x0 = cell.x * self.size + self.size - self.wall
                y0 = cell.y * self.size
                x1 = self.wall
                y1 = self.size
                pygame.draw.rect(self.window.screen, black, (x0, y0, x1, y1))

            # Check if we should draw the cells top wall
            if cell.tw:
                x0 = cell.x * self.size
                y0 = cell.y * self.size
                x1 = self.size
                y1 = self.wall
                pygame.draw.rect(self.window.screen, black, (x0, y0, x1, y1))

            # Check if we should draw the cells bottom wall
            if cell.bw:
                x0 = cell.x * self.size
                y0 = cell.y * self.size + self.size - self.wall
                x1 = self.size
                y1 = self.wall
                pygame.draw.rect(self.window.screen, black, (x0, y0, x1, y1))

            self.window.update()