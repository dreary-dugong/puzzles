from colorama import Back #print boards for debugging 

def main():

    #read input
    with open("input.txt") as f:
        calls = f.readline()[:-1].split(",")
        f.readline()
        boards = []
        for rawboard in f.read().replace("\n ", "\n").split("\n\n"):
            board = []
            for rawline in rawboard.split("\n"):
                #too early in the month for regex yet
                rawline = rawline.replace("  ", " ")
                row = rawline.split(" ")
                board.append(row)
            boards.append(board)

    boards[-1] = boards[-1][:-1]

    #markers keep track of calls
    markers = []
    for board in range(len(boards)):
        marker = []
        for row in range(5):
            markrow = []
            for num in range(5):
                markrow.append(False)
            marker.append(markrow)
        markers.append(marker)
  
    #loop until we find a bingo
    call_index = 0
    lastscore = None
    winners = set()
    while call_index < len(calls):
        call = calls[call_index]

        #loop through boards and mark the call
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, num in enumerate(row):
                    if num == call:
                        markers[i][j][k] = True

                        #check for bingo aka sudoku
                        if sum(markers[i][j]) == 5 or sum([row[k] for row in markers[i]]) == 5:
                            if i not in winners:
                                latestscore = calcscore(boards[i], markers[i], call) 
                                winners.add(i)
        call_index += 1

    print(latestscore)

def calcscore(board, marker, latestcall):
    unmarked_sum = 0
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if not marker[i][j]:
                unmarked_sum += int(num)
    return unmarked_sum * int(latestcall)



def printboard(board, marker):
    out = ""
    for boardline, markline in zip(board, marker):
        for num, mark in zip(boardline, markline):
            if len(num) == 1:
                out += " "
            if mark:
                out += Back.GREEN
            else:
                out += Back.RESET
            out += num + Back.RESET + " "
        out += Back.RESET + "\n"
    print(out)

if __name__ == "__main__":
    main()
