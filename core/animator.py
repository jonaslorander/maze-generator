import pygame

class Animator():
    def __init__(self, window, maze, size, solver = None):
        self.window = window
        self.cell_order = maze.cell_order
        self.size = size
        self.wall = 2 # int(self.size / 10)
        self.solver = solver

    def animate(self):
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
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

        # If there is a solver with a result passed, animate that as well
        if self.solver:
            # Save current drawn maze

            # Draw start rect
            (start_x, start_y) = self.solver.get_start_cell()
            x0 = start_x * self.size + self.wall
            y0 = start_y * self.size + self.wall
            x1 = self.size - (2 * self.wall)
            y1 = self.size - (2 * self.wall)
            rect = (x0, y0, x1, y1)
            pygame.draw.rect(self.window.screen, red, rect)
            
            # Draw finish rect
            (finish_x, finish_y) = self.solver.get_finish_cell()
            x0 = finish_x * self.size + self.wall
            y0 = finish_y * self.size + self.wall
            x1 = self.size - (2 * self.wall)
            y1 = self.size - (2 * self.wall)
            rect = (x0, y0, x1, y1)
            pygame.draw.rect(self.window.screen, green, rect)

            if self.solver.search:
                # Draw search

                # Restore maze

                # Draw solution
                pass