
#move the ferry by a given amount in a given direction
def advance(direction, distance):
    global currPos
    global currDir
    
    if direction == "N":
        currPos[1] -= distance
    elif direction == "S":
        currPos[1] += distance
    elif direction == "E":
        currPos[0] += distance
    elif direction ==  "W":
        currPos[0] -= distance

    return


#read input

DIRECTIONS = ("N", "E", "S", "W")

currPos = [0, 0] #0 East, 0 South
currDir = "E"

with open("input1.txt") as f:

    for line in f:
        lineDir = line[0]
        lineDist = int(line[1:])

        if lineDir == "F":
            advance(currDir, lineDist)
        elif lineDir == "L":
            absDir = DIRECTIONS[(DIRECTIONS.index(currDir)-lineDist//90) % len(DIRECTIONS)] #perform rotation as a rotation
            currDir = absDir
        elif lineDir == "R":
            absDir = DIRECTIONS[(DIRECTIONS.index(currDir)+lineDist//90) % len(DIRECTIONS)]
            currDir = absDir
        else:
            advance(lineDir, lineDist)

print(currPos)
print(abs(currPos[0]) + abs(currPos[1]))



