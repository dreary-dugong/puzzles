
#move the ferry by a given amount in a given direction
def advanceWaypoint(direction, distance):
    global relativeWayPos
    
    if direction == "N":
        relativeWayPos[1] -= distance
    elif direction == "S":
        relativeWayPos[1] += distance
    elif direction == "E":
        relativeWayPos[0] += distance
    elif direction ==  "W":
        relativeWayPos[0] -= distance

    return


#read input

shipPos = [0, 0] #0 East, 0 South
relativeWayPos = [10, -1] #waypoint starts 10 east, 1 north of the ship

with open("input1.txt") as f:

    for line in f:
        lineDir = line[0]
        lineDist = int(line[1:])

        if lineDir == "F": #advance the ship to the waypoint n times
            shipPos[0] += relativeWayPos[0] * lineDist
            shipPos[1] += relativeWayPos[1] * lineDist
            
        elif lineDir == "R": #rotate waypont right

            #our rotations are pretty obscure but they're elegant^(TM)
            for __ in range(lineDist // 90):

                #swap x and y
                relativeWayPos[0], relativeWayPos[1] = relativeWayPos[1], relativeWayPos[0]
                relativeWayPos[0] *= -1 #reflect across x axis
                    
        elif lineDir == "L": #rotate waypoint left

            #opposite rotations to go left
            for __ in range(lineDist % 90):

                #swap y and x
                relativeWayPos[1], relativeWayPos[0] = relativeWayPos[0], relativeWayPos[1]
                relativeWayPos[-1] *= -1 #reflect across x axis
            
        else:
            advanceWaypoint(lineDir, lineDist)


print(shipPos)
print(abs(shipPos[0]) + abs(shipPos[1]))



