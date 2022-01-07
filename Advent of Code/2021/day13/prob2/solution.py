def get_points(infile):
    points = []
    with open(infile) as f:
        data = f.read()
    pointData = data.split("\n\n")[0]
    for pointString in pointData.split("\n"):
        x, y = pointString.split(",")
        points.append((int(x), int(y)))
    return points

def get_folds(infile):
    folds = []
    with open(infile) as f:
        foldData = f.read().strip().split("\n\n")[1]

    for foldString in foldData.split("\n"):
        foldString = foldString.strip()
        foldSpec = foldString.split(" ")[2]
        foldType = foldSpec[0]
        foldNum = int(foldSpec[2:])
        folds.append((foldType, foldNum))
    return folds

def do_fold(points, fold):
    foldType, foldNum = fold
    foldedPoints = set() 
    for point in points:
        if foldType == "x" and point[0] > foldNum:
            foldedPoints.add((2*foldNum-point[0], point[1]))
        elif foldType == "y" and point[1] > foldNum:
            foldedPoints.add((point[0], 2*foldNum-point[1]))
        else:
            foldedPoints.add(point)
    return foldedPoints

def decode_points(points):
    xmax = 0
    ymax = 0
    for point in points:
        xmax = max(xmax, point[0])
        ymax = max(ymax, point[1])

    data = []
    for i in range(ymax+1):
        row = []
        for j in range(xmax+1):
            if (j, i) in points:
                row.append("#")
            else:
                row.append(".")
        data.append(row)
    return data

def write_data(data, outfile):
    with open(outfile, 'w') as f:
        for line in data:
            f.write("".join(line) + "\n")

def main():
    infile = "input.txt"
    outfile = "output.txt"
    points = set(get_points(infile))
    folds = get_folds(infile)
    for fold in folds:
        points = do_fold(points, fold)
    output = decode_points(points)
    write_data(output, outfile)




if __name__ == "__main__":
    main()
