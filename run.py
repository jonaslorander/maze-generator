import engine.maze as maze
from core.window import Window
from core.animator import Animator

MAZE_SIZE_X = 25
MAZE_SIZE_Y = 25
CELL_SIZE = 20

def main():
    # Generate maze
    m = maze.Maze(size = (MAZE_SIZE_X, MAZE_SIZE_Y), start = (1, 1))
    m.generate()

    # Create new window and paint it black
    win_size = (MAZE_SIZE_X * CELL_SIZE, MAZE_SIZE_Y * CELL_SIZE)
    w = Window(win_size)
    w.fill((0, 0, 0))

    a = Animator(w, m, CELL_SIZE)
    a.animate()

    # Save maze
    m.create_image('maze.png') #, start = (1, 1), end = (25, 25))

    while not w.closed:
        w.update()

if __name__ == "__main__":
    main()
