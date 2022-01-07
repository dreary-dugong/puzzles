#!/bin/python3

from dataclasses import dataclass
from sys import argv 

@dataclass
class Point:
    x: int
    y: int

    #would it be better to use unsafe_hash=True?
    def __hash__(self):
        return (self.x,self.y).__hash__()
    
@dataclass
class Line:
    start: Point
    end: Point

def parse_lines(file):
    lines = []
    with open(file) as f:
        for line in f:
            start_str, _, end_str = line.split(" ")
            start = Point(*map(int, start_str.split(",")))
            end = Point(*map(int, end_str.split(",")))
            lines.append(Line(start, end))
    return lines


def main():
    inputfile = argv[1] 
    lines = parse_lines(inputfile)
    visited = set()
    visitedTwice = set()

    for line in lines:

        #horizontal line
        if line.start.x == line.end.x:
            x = line.start.x
            ystart, yend = sorted([line.start.y, line.end.y])
            coverage = [Point(x, y) for y in range(ystart, yend+1)]

        #veritcal line
        elif line.start.y == line.end.y:
            y = line.start.y
            xstart, xend = sorted([line.start.x, line.end.x])
            coverage = [Point(x, y) for x in range(xstart, xend+1)]

        #diagonal line
        else:
            xchange = 1 if line.start.x < line.end.x else -1
            ychange = 1 if line.start.y < line.end.y else -1
            xstart, xend = sorted([line.start.x, line.end.x]) #how many points
            coverage = []
            for i in range(0, xend-xstart+1):
                currx = line.start.x + i*xchange
                curry = line.start.y + i*ychange
                coverage.append(Point(currx, curry))

        for point in coverage:
            if point in visited:
                visitedTwice.add(point)
            else:
                visited.add(point)

    print(len(visitedTwice))
    
if __name__ == "__main__":
    main()


    

    
