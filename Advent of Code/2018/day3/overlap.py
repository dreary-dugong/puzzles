#read file
filename = "input.txt"

coordsDict = {}

with open(filename, 'r') as f:
    for line in f:

        #parse data
        currLineData =  line.split(" ")
        currID = currLineData[0][1:]
        fromLeft, fromTop = currLineData[2].replace(":", "").split(",")
        width, height = currLineData[-1].split("x")

        fromLeft, fromTop, width, height = int(fromLeft), int(fromTop), int(width), int(height)


        #record squares
        for x in range(width):
            for y in range(height):
                coords = (x+fromLeft, y+fromTop)
                if coords in coordsDict:
                    coordsDict[coords] += 1;
                else:
                    coordsDict[coords] = 1;

#extract info from coords dict
numOverlap = 0
for coord in coordsDict:
    if coordsDict[coord] > 1:
        numOverlap += 1;

print("Number of squares with overlapping claims: " + str(numOverlap))
