#4DConstellations.py
#Daniel Gysi
#Given a list of 4 dimensional points, determine how many constellations they form
#Two points are in the same constellation if there is some other point
#in that constellation in which the manhattan distance to the first point is <=3
import math

class point:
    """represent a point in 4D space"""
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
    def __str__(self):
        return  f"({self.x},{self.y},{self.z},{self.t})"

def manhattanDistance(p1, p2):
    """Return the manhattan distance between 2 points in 4d space"""
    d = math.abs(p1.x - p2.x) + math.abs(p1.y - p2.y) + math.abs(p1.x - p2.z) + math.abs(p1.t-p2.t)
    return d



#read points from file
inputFile = "samplePoints4.txt" #name of file
points = [] #list of every point in the file

with open(inputFile, 'r') as f:
    for line in f:
        p = point(*[int(n) for n in line.split(",")]); #convert line of numbers into coordinates and create point object
        points.append(p)


#put points into constellations
#create constellations by combining smaller constellations

#initial list with a constellation for every point
constellations = [ [p] for p in points]
numCon = 0; #total number of constellations completed

#iterate until all constellations are complete
while len(constellations) > 0:

    currentCon = constellations
    for c in constellations:

        for p1 in currentCon:
            for p2 in c:
                if manhattanDistance(p1, p2) <= 3:
                    
        

        
    
