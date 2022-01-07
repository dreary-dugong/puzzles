maxSID = 0;

with open("input1.txt") as f:
    for line in f:

        #reset ranges
        row, column = [0, 127], [0, 7]
        for char in line:

            #get distances
            rowDist = row[1] - row[0] + 1
            colDist = column[1] - column[0] + 1

            #row
            if char == "F":
                row[1] -= rowDist / 2
            elif char == "B":
                row[0] += rowDist / 2

            #column
            elif char == "L":
                column[1] -= colDist / 2
            elif char == "R":
                column[0] += colDist / 2


        SID = row[0] * 8 + column[0]

        maxSID = max(maxSID, SID)

print(maxSID)
