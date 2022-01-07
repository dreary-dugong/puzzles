from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

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
    inputfile = "input.txt"
    lines = parse_lines(inputfile)
    visited = set()
    visitedTwice = set()

    for line in lines:
        coverage = []
        if line.start.x == line.end.x:
            x = line.start.x
            ystart, yend = sorted([line.start.y, line.end.y])
            coverage = [Point(x, y) for y in range(ystart, yend+1)]
        elif line.start.y == line.end.y:
            y = line.start.y
            xstart, xend = sorted([line.start.x, line.end.x])
            coverage = [Point(x, y) for x in range(xstart, xend+1)]

        for point in coverage:
            if point in visited:
                visitedTwice.add(point)
            else:
                visited.add(point)

    print(len(visitedTwice))
    
if __name__ == "__main__":
    main()


    

    
