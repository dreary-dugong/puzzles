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

def main():
    infile = "input.txt"
    points = set(get_points(infile))
    folds = get_folds(infile)
    points = do_fold(points, folds[0])
    print(len(points))




if __name__ == "__main__":
    main()
