from cartLib import *

#read textfile into char matrix
inputFile = "test1.txt"
matrix = []
with open(inputFile, 'r') as f:
    for line in f:
        matrix.append([])
        for c in line:
            if c != "\n":
                matrix[len(matrix)-1].append(c)

trackObjs = (Horizontal, Vertical, Intersection, Corner, LeftDown, RightUp, LeftUp, RightDown)

tracks = []
carts = []
for y, row in enumerate(matrix):
    for character in row:
        for trackObj in trackObjs:
            if character == trackObj.symbol:
                tracks.append(trackObj(
