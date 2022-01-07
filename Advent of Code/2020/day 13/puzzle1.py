
#read file
with open("input1.txt") as f:
    earliestDeparture = int(f.readline())
    busIds = [int(x) for x in f.readline().split(",") if x.isnumeric()]
        #this is a disgusting line but it's why I love this language

bestTime = earliestDeparture + max(busIds) #upper bound on best departure time
bestBus = 0

for bus in busIds:

    #if a bus departs at the perfect time
    if earliestDeparture % bus == 0:
        bestTime = earliestDeparture
        bestBus = bus
        break

    #otherwise, look for the best one
    currDepart = (earliestDeparture // bus + 1) * bus
    if currDepart < bestTime:
        bestTime = currDepart
        bestBus = bus


print(bestBus * (bestTime - earliestDeparture))
