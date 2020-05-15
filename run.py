import engine.maze as maze

def main():
    # Generate maze
    m = maze.Maze(size = (25, 25), start = (1, 1))
    m.generate()

    # Save maze
    #print(m.cells)
    m.create_image('maze.png', start = (1, 1), end = (25, 25))

if __name__ == "__main__":
    main()
