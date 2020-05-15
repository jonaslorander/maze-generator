import engine.maze as maze

def main():
    # Generate maze
    m = maze.Maze(start = (0,0))
    m.generate()

    # Save maze
    print(m.cells)

if __name__ == "__main__":
    main()
