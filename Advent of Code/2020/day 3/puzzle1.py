
#read file in
forest = []

with open("input1.txt") as file:
    for line in file:
        currLine = []
        for char in line.strip():
            currLine.append(char)
        forest.append(currLine)


#position class so indexes don't drive me crazy
class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


def getTrees(slope):
    
    X_INC = slope[0]
    Y_INC = slope[1]

    treeCount = 0

    #start at 0,0
    currPos = Position(0, 0)

    #increment once because we don't look for trees at the starting position
    currPos.x += X_INC
    currPos.y += Y_INC


    while currPos.y < len(forest): #repeat until we've gone down all the rows

        currRow = forest[currPos.y]
        if currRow[currPos.x % len(currRow)] == "#": #use mod to wrap around
            treeCount += 1
            
        currPos.x += X_INC
        currPos.y += Y_INC

        
    return treeCount


def main():
    ans = 1;
    for slope in ((1,1),(3,1),(5,1),(7,1),(1,2)):
        ans *= getTrees(slope)

    print(ans)

if __name__=="__main__":
    main()
    
