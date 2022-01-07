from collections import deque

def get_adjacent(grid, i,j):
    """return list of coordinate adjacent to a given coordinate"""
    adjacent = []
    if i < len(grid)-1:
        adjacent.append((i+1, j))
    if i > 0:
        adjacent.append((i-1, j))
    if j < len(grid[0])-1:
        adjacent.append((i, j+1))
    if j > 0:
        adjacent.append((i, j-1))
    return adjacent

def get_lows(grid):
    """return coordinates of low points"""
    lows = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            adjacentNums = [grid[x][y] for x, y in get_adjacent(grid,i,j)]
            if grid[i][j] < min(adjacentNums):
                lows.append((i,j))
    return lows

def load_grid(infile):
    """read 2d array from file"""
    grid = []
    with open(infile) as f:
        for line in f:
            grid.append(list(map(int,list(line.replace("\n","")))))
        return grid

def product(li):
    """return product of all values in an iterable"""
    prod = 1
    for item in li:
        prod *= item
    return prod

def get_basin_size(grid, low):
    """return the size of a basin around a given low point"""
    basinSize = 0 
    basinStack = deque()
    basinStack.append(low)
    checked = {low} 

    while basinStack:
        curr = basinStack.popleft()
        basinSize += 1
        currNum = grid[curr[0]][curr[1]]
    
        for adj in get_adjacent(grid, curr[0], curr[1]):

            adjNum = grid[adj[0]][adj[1]]

            if currNum < adjNum and adjNum != 9 and adj not in checked:
                basinStack.append(adj)
                checked.add(adj)

    return basinSize

def main():
    infile = "input.txt"
    grid = load_grid(infile)
    basins = []
    for low in get_lows(grid):
        basins.append(get_basin_size(grid, low))

    print(product(sorted(basins)[-1:-4:-1])) #product of top 3 basins

if __name__ == "__main__":
    main()






