from sys import maxsize

def get_grid(infile):
    grid = []
    with open(infile) as f:
        for line in f:
            grid.append(list(map(int, list(line.strip()))))
    return grid

def get_adjacent(grid, pos):
    i, j = pos
    adjacent = []
    if i > 0:
        adjacent.append((i-1, j))
    if i < len(grid)-1:
        adjacent.append((i+1, j))
    if j > 0:
        adjacent.append((i, j-1))
    if j < len(grid[0])-1:
        adjacent.append((i, j+1))
    return adjacent

def is_unvisited_finite(dist, visited):
    for pos, value in dist.items():
        if value < maxsize and pos not in visited:
            return True
    return False

def get_min_position(dist, visited):
    minPos = None
    minValue = maxsize
    for pos, value in dist.items():
        if value < minValue and pos not in visited:
            minValue = value
            minPos = pos
    return minPos 

def main():
    infile = "input.txt"
    grid = get_grid(infile)

    #dijkstra's algorithm but  without the prio queue

    start = (0, 0) #distance from here 
    end = (len(grid)-1, len(grid[0])-1) #break once we get here

    visited = set() #nodes whose minimum distance is totally known
    dist = dict() #current minimum distances for each node

    #initialize distances
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dist[(i,j)] = maxsize
    dist[start] = 0

    #repeat dijkstra until nothing unvisted is reachable
    while is_unvisited_finite(dist, visited):
        curr = get_min_position(dist, visited)
        if curr == end:
            break
        for adj in get_adjacent(grid, curr):
            adjDist = dist[adj]
            dist[adj] = min(adjDist, dist[curr] + grid[adj[0]][adj[1]])
        visited.add(curr)

    print(dist[end])




if __name__ == "__main__":
    main()
