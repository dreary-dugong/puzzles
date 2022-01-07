
#read file
with open("input1.txt") as f:
    earliestDeparture = int(f.readline())
    busIds = [int(x) if x.isnumeric() else 1 for x in f.readline().split(",")]
        #this is a disgusting line but it's why I love this language


found = False

#speed up the brute force with the biggest increment
inc = max(busIds)
base = inc - busIds.index(inc)

curr = base

while not found:

    curr += inc

    found = True #assume true so we can see if a condition fails
    for i, bus in enumerate(busIds):
        if (curr + i) % bus != 0:
            found = False


print(curr)
