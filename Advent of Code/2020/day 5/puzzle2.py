maxSID = 0;


seats = [] #list of all seats on the plane


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


        seats.append((row[0], column[0]))

#look for all possible seats
for i in range(128):
    for j in range(8):

        #if a seat is missing, check if there's one in front and behind
        if (i, j) not in seats:
            if (i-1, j) in seats and (i + 1, j) in seats:
                print("Seat: " + str(i) + ", " + str(j))
                print("SID: " + str(8 * i + j))
