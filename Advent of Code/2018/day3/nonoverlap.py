#read file
filename = "input.txt"

coordsDict = {}
claimsDict = {}
with open(filename, 'r') as f:
    for line in f:

        #parse data
        currLineData =  line.split(" ")
        currID = currLineData[0][1:]
        fromLeft, fromTop = currLineData[2].replace(":", "").split(",")
        width, height = currLineData[-1].split("x")

        fromLeft, fromTop, width, height = int(fromLeft), int(fromTop), int(width), int(height)


        #record squares
        claimsDict[currID] = []
        for x in range(width):
            for y in range(height):
                coords = (x+fromLeft, y+fromTop)
                if coords in coordsDict:
                    coordsDict[coords] += 1;
                else:
                    coordsDict[coords] = 1;

                claimsDict[currID].append(coords)

#compare claimsDict to coordsDict
for claim in claimsDict:
    hasOverlap = False;
    for coord in claimsDict[claim]:
        if coordsDict[coord] > 1:
            hasOverlap = True
            break
    if not hasOverlap:
        print("This claim id has no overlap: " + claim)
        
        
