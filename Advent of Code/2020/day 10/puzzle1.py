#this puzzle is simple
#to get them in order of joltages,
#just sort the list

#read input
adapters = []
with open("input1.txt") as f:
    for line in f:
        adapters.append(int(line))

#get the joltage order so that all are used
adapters.sort()

prev = 0
numThree = 1 #at least one due to internal adapter
numOne = 0
for adapter in adapters:
    currDiff = adapter - prev

    prev = adapter


    if currDiff == 3:
        numThree+=1
    elif currDiff == 1:
        numOne+=1

print(numOne * numThree)
