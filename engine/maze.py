import random

class Cell():
    def __init__(self, x, y):
        # Cell coordinates
        self.X = x
        self.y = y

        # Cell walls
        self.ew = True
        self.nw = True
        self.ww = True
        self.sw = True

        # Is cel visited?
        self.visited = False

class Maze():
    def __init__(self, size = (10, 10), start = (0, 0)):
        self.width = size[0]
        self.height = size[1]
        self.start_x = start[0]
        self.start.y = start[1]

        self.cells = [[Cell(x, y) for x in range(x)] for y in range(y)]
        