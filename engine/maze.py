import random
from PIL import Image, ImageDraw

class Cell():
    x = None
    y = None

    def __init__(self, x, y):
        # Cell coordinates
        self.x = x
        self.y = y

        # Cell walls
        self.rw = True
        self.tw = True
        self.lw = True
        self.bw = True

        # Is cel visited?
        self.visited = False

    def __repr__(self):
        return f'{self.x};{self.y}:{1 if self.visited else 0}'

class Maze():
    def __init__(self, size = (10, 10), start = (1, 1)):
        self.width = size[0]
        self.height = size[1]

        # Check that start cell is inside of maze
        self.start_x = start[0] - 1
        self.start_y = start[1] - 1

        # Create a list of the order of the cisited cells, can be used for animating the drawing
        self.cell_order = []

        # Generate 3D list of all cells
        self.cells = [[Cell(x, y) for y in range(self.height)] for x in range(self.width)]

    # Get all unvisited neighbours of a cell
    def __get_neighbours(self, cell):
        n = []

        # Check left neighbour
        #  Make sure we are on the map
        if cell.x - 1 >= 0:
            if not self.cells[cell.x - 1][cell.y].visited:
                n.append(self.cells[cell.x - 1][cell.y])

        # Check right neighbour
        #  Make sure we are on the map
        if cell.x + 1 < self.width:
            if not self.cells[cell.x + 1][cell.y].visited:
                n.append(self.cells[cell.x + 1][cell.y])

        # Check upper neighbour
        #  Make sure we are on the map
        if cell.y - 1 >= 0:
            if not self.cells[cell.x][cell.y - 1].visited:
                n.append(self.cells[cell.x][cell.y - 1])

        # Check lower neightbour
        #  Make sure we are on the map
        if cell.y + 1 < self.height:
            if not self.cells[cell.x][cell.y + 1].visited:
                n.append(self.cells[cell.x][cell.y + 1])

        return n

    # Check if two cells are neighbours 
    def __is_neighbours(self, cc, nc):
        xdiff = abs(cc.x - nc.x)
        ydiff = abs(cc.y - nc.y)

        if (xdiff == 1 and ydiff == 0) or (xdiff == 0 and ydiff == 1) or (xdiff == 0 and ydiff == 0):
            return True
        else:
            return False

    # Remove wall between current cell (cc) and next cell (nc)
    def remove_wall(self, cc, nc):
        # Check if cells are neighbours
        if self.__is_neighbours(cc, nc):
            # Remove wall between cells
            xdiff = cc.x - nc.x
            ydiff = cc.y - nc.y

            # nc | cc
            if xdiff == 1:
                cc.lw = False
                nc.rw = False
            
            # cc | nc
            elif xdiff == -1:
                cc.rw = False
                nc.lw = False

            # nc
            # --
            # cc
            elif ydiff == 1:
                cc.tw = False
                nc.bw = False

            # cc
            # --
            # nc
            elif ydiff == -1:
                cc.bw = False
                nc.tw = False

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
            nb = self.__get_neighbours(curr_cell)

            # Add the newly visited cell to the list
            self.cell_order.append(curr_cell)

            # If there are neighbours ad the cell back to the stack to handle other neightbours later
            if nb:
                cellstack.append(curr_cell)

                # Pick a random neighbour and set it as visited
                next_cell = random.choice(nb)
                next_cell.visited = True

                # Remove wall between cells
                self.remove_wall(curr_cell, next_cell)

                # Add next cell to the stack to begin there next iteration
                cellstack.append(next_cell)

    def create_image(self, filename = 'maze.png', start = None, end = None):
        img = Image.new('RGB', (self.width * 10, self.height * 10), 'black')
        d = ImageDraw.Draw(img)

        cell_size = 10
        line_width = int(cell_size / 10)

        for cellx in self.cells:
            for cell in cellx:
                x = cell.x * cell_size
                y = cell.y * cell_size

                # Draw cell with all walls
                d.rectangle([(x, y), (x + cell_size - line_width, y + cell_size - line_width)], fill = 'white', outline = 'black', width = line_width)

                # Remove walls
                if not cell.rw:
                    x0 = x + cell_size - line_width
                    y0 = y + line_width
                    x1 = x + cell_size
                    y1 = y + cell_size - line_width * 2
                    d.rectangle([(x0, y0), (x1, y1)], fill = 'white')
                
                if not cell.lw:
                    x0 = x
                    y0 = y + line_width
                    x1 = x
                    y1 = y + cell_size - line_width * 2
                    d.rectangle([(x0, y0), (x1, y1)], fill = 'white')

                if not cell.tw:
                    x0 = x + line_width
                    y0 = y
                    x1 = x + cell_size - line_width * 2
                    y1 = y
                    d.rectangle([(x0, y0), (x1, y1)], fill = 'white')
                
                if not cell.bw:
                    x0 = x + line_width
                    y0 = y + cell_size
                    x1 = x + cell_size - line_width * 2
                    y1 = y + cell_size - line_width
                    d.rectangle([(x0, y0), (x1, y1)], fill = 'white')
        
        # Print start end end tiles
        if not start == None and not end == None:
            start_x = start[0] - 1
            start_y = start[1] - 1
            end_x = end[0] - 1
            end_y = end[1] - 1

            # Draw start rectangle
            x0 = start_x * cell_size + line_width
            y0 = start_y * cell_size + line_width
            x1 = start_x * cell_size + cell_size - line_width * 2
            y1 = start_y * cell_size + cell_size - line_width * 2
            d.rectangle([(x0, y0), (x1, y1)], fill = 'red')

            # Draw end rectangle
            x0 = end_x * cell_size + line_width
            y0 = end_y * cell_size + line_width
            x1 = end_x * cell_size + cell_size - line_width * 2
            y1 = end_y * cell_size + cell_size - line_width * 2
            d.rectangle([(x0, y0), (x1, y1)], fill = 'green')

        img.save(filename)
