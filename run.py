from engine.maze import Maze
from engine.solver import Solver
from core.animator import Animator
from core.window import Window

MAZE_SIZE_X = 10
MAZE_SIZE_Y = 10
CELL_SIZE = 30

def main():
    # Generate maze
    m = Maze(size = (MAZE_SIZE_X, MAZE_SIZE_Y), start = (1, 1))
    m.generate()
    
    # Save maze as PNG
    m.create_image('maze.png') #, start = (1, 1), end = (25, 25))

    # Create new window and paint it black
    win_size = (MAZE_SIZE_X * CELL_SIZE, MAZE_SIZE_Y * CELL_SIZE)
    w = Window(win_size)
    w.fill((0, 0, 0))

    # Create solver
    s = Solver(m, (1, 1), (MAZE_SIZE_X, MAZE_SIZE_Y))
    s.solve()

    # Instantiate an animator
    a = Animator(w, m, CELL_SIZE, s)
    a.animate()

    while not w.closed:
        w.update()

if __name__ == "__main__":
    main()
