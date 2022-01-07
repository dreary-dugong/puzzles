from collections import deque
from colorama import Back

def print_grid(grid):
    """print the grid with highlights on who flashed in the last step"""
    out = ""
    for line in grid:
        for n in line:
            if n == 0:
                out = out + Back.BLUE
            out = out + str(n) + Back.RESET
        out += "\n"
    print(out)

def get_grid(infile):
    """load 2d array from textfile"""
    grid = []
    with open(infile) as f:
        for line in f:
            grid.append(list(map(int, line.strip(" \n"))))
    return grid

def get_adjacent(grid, pos):
    """get immediate positions around one given in a given 2d list"""
    i, j = pos
    adjacent = []
    incs = [0, 1, -1]
    for xinc in incs:
        for yinc in incs:
            if 0 <= i+xinc <= len(grid) - 1 and 0 <= j+yinc <= len(grid[0])-1:
                adj = (i+xinc, j+yinc)
                if adj != pos:
                    adjacent.append(adj)
    return adjacent

def step(grid):
    #part 1 increment all by 1
    #keep track of 10s for step 2
    flashers = deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
            if grid[i][j] == 10:
                flashers.append((i,j))

    #part 2: flashing with queue-based bfs
    flashed = deque() 
    while flashers:
        curr = flashers.pop()
        for pos in get_adjacent(grid, curr):
            i, j = pos
            if grid[i][j]+1 == 10:
                flashers.appendleft(pos)
            grid[i][j] = min(grid[i][j]+1, 10) 
        flashed.append(curr)

    #part 3: reset flashed to 0
    for pos in flashed:
        i, j = pos
        grid[i][j] = 0

    return grid, len(flashed)



def main():
    infile = "input.txt"
    grid = get_grid(infile)
    synced = False
    steps = 0

    while not synced:
        grid, stepFlashes = step(grid)
        steps += 1
        if stepFlashes == len(grid)*len(grid[0]):
            synced = True

    print(steps)

if __name__ == "__main__":
    main()

