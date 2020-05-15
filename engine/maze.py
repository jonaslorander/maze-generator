import random

class Cell():
    def __init__(self, x, y):
        # Cell coordinates
        self.x = x
        self.y = y

        # Cell walls
        self.ew = True
        self.nw = True
        self.ww = True
        self.sw = True

        # Is cel visited?
        self.visited = False

    def __repr__(self):
        return f'{self.x};{self.y}:{1 if self.visited else 0}'

class Maze():
    def __init__(self, size = (10, 10), start = (0, 0)):
        self.width = size[0]
        self.height = size[1]

        # Check that start cell is inside of maze
        self.start_x = start[0]
        self.start_y = start[1]

        self.cells = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    # Get all unvisited neighbours of a cell
    def __getNeighbours(self, cell):
        n = []

        # Check left neighbour
        #  Make sure we are on the map
        if cell.x - 1 > 0:
            if not self.cells[cell.x - 1][cell.y].visited:
                n.append(self.cells[cell.x - 1][cell.y])

        # Check right neighbour
        #  Make sure we are on the map
        if cell.x + 1 < self.width:
            if not self.cells[cell.x + 1][cell.y].visited:
                n.append(self.cells[cell.x + 1][cell.y])

        # Check upper neighbour
        #  Make sure we are on the map
        if cell.y - 1 > 0:
            if not self.cells[cell.x][cell.y - 1].visited:
                n.append(self.cells[cell.x][cell.y - 1])

        # Check lower neightbour
        #  Make sure we are on the map
        if cell.y + 1 < self.height:
            if not self.cells[cell.x][cell.y + 1].visited:
                n.append(self.cells[cell.x][cell.y + 1])

        return n

    # Check if two cells are neighbours 
    def __isNeighbours(self, cc, nc):
        pass

    # Remove wall between current cell (cc) and next cell (nc)
    def removeWall(self, cc, nc):
        # Check if cells are neighbours
        if self.__isNeighbours(cc, nc):
            # Remove wall between cells
            pass

    def generate(self):
        # Get the start cell and set it as visited
        curr_cell = self.cells[self.start_x][self.start_y]
        curr_cell.visited = True

        # Add it to the stack
        cellstack = [curr_cell]

        # Loop through the stack until it is empty
        while cellstack:
            # Get last cell in stack and remove it from the stack
            curr_cell = cellstack.pop()

            # Get list of unvisited neighbours
            nb = self.__getNeighbours(curr_cell)

            # If there are neighbours ad the cell back to the stack to handle other neightbours later
            if nb:
                cellstack.append(curr_cell)

                # Pick a random neighbour and set it as visited
                next_cell = random.choice(nb)
                next_cell.visited = True

                # Remove wall between cells
                self.removeWall(curr_cell, next_cell)

                # Add next cell to the stack to begin there next iteration
                cellstack.append(next_cell)

