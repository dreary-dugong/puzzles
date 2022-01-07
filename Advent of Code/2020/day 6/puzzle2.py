ans = 0
with open("input1.txt") as f:

    groups = f.read().split("\n\n")

    for group in groups:

        possQ = []
        accQ = []

        people = group.split("\n")
        
        for person in people:
            for q in person:
                if q not in possQ:
                    possQ.append(q)
                    
        accQ = possQ
        if "\n" in accQ:
            accQ.remove("\n")
        
        for person in people:
            toRemove = []
            for q in accQ:
                if q not in person:
                    toRemove.append(q)
            for q in toRemove:
                accQ.remove(q)

        ans += len(accQ)

print(ans)
