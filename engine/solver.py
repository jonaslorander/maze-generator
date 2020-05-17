

class Solver:
    def __init__(self, maze, start, finish):
        # Maze to solve
        self.maze = maze

        # Start cell
        self.start_x = start[0] - 1
        self.start_y = start[1] - 1

        # Finish cell
        self.finish_x = finish[0] - 1
        self.finish_y = finish[1] - 1

        # List to hold search cell order
        self.search = []

        # List to hold solved path
        self.solution = []

    # Return start cell
    def get_start_cell(self):
        return (self.start_x, self.start_y)

    # Return finish cell
    def get_finish_cell(self):
        return (self.finish_x, self.finish_y)

    # The function to call for starting the solve
    def solve(self):
        pass