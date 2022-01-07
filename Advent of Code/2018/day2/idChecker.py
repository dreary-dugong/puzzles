#load data from file
fileName = "input.txt"
with open(fileName, 'r') as f:
    ids = [line.replace("\n", "") for line in f]

#cartesian product of ids to compare each combo
#should import itertools for efficiency but I'm here for fun, not efficiency
combos = []
for id1 in ids:
    for id2 in ids:
        combos.append((id1, id2));

#compare each combo
for combo in combos:
    numDiff = 0
    latestDiffIndex = 0;
    for i in range(len(combo[0])):
        if combo[0][i] != combo[1][i]:
            numDiff += 1;
            lastestDiffIndex = i;
            if numDiff > 1:
                break;
            
    if numDiff == 1:
        print("IDs: " + str(combo))
        print("Index of difference: " + str(latestDiffIndex))
        print("Solution: " + combo[0][0:i] + combo[0][i+1:])
        break;
    
