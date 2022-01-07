from sys import maxsize
import heapq

def get_grid(infile):
    grid = []
    for vert in range(5):
        with open(infile) as f:
            for line in f:
                gridLine = []
                for horz in range(5):
                    for val in line.strip():
                        currVal = int(val)
                        currVal += vert
                        currVal += horz
                        #this does not work in the general case
                        # this only works while val < 19
                        if currVal >= 10:
                            currVal = currVal % 10 + (currVal // 10)
                        gridLine.append(currVal)
                grid.append(gridLine)

                    
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

def get_min_position(prio, dist, visited):
    foundMin = False
    #we can't update an item already in the queue
    #so we check if the current distance is the most
    #up to date based on our dict of shortest distances
    while not foundMin:
        possMin = heapq.heappop(prio)
        d, pos = possMin
        if dist[pos] == d: 
            foundMin = True
            return possMin[1]

def main():
    infile = "input.txt"
    grid = get_grid(infile)

    print("Graph loaded.")
    print(f"Size: {len(grid)*len(grid[0])}")

    #dijkstra's algorithm but without unconventional prio queue 

    start = (0, 0) #distance from here 
    end = (len(grid)-1, len(grid[0])-1) #break once we get here

    visited = set() #nodes whose minimum distance is totally known
    dist = dict() #current minimum distances for each node

    #initialize distances
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dist[(i,j)] = maxsize
    dist[start] = 0
    prio = [(0, start)]

    #repeat dijkstra until nothing unvisted is reachable
    numReachableFinite = 1
    while numReachableFinite:
        curr = get_min_position(prio, dist, visited)
        if curr == end:
            break
        for adj in get_adjacent(grid, curr):
            adjDist = dist[adj]
            currPathToAdj = dist[curr] + grid[adj[0]][adj[1]]
            if dist[adj] == maxsize:
                numReachableFinite += 1
            if currPathToAdj < adjDist:
                dist[adj] = currPathToAdj
                heapq.heappush(prio, (currPathToAdj, adj))

        visited.add(curr)
        numReachableFinite -= 1

    print(dist[end])




if __name__ == "__main__":
    main()
