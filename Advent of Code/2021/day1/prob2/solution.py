measures = []
with open("input.txt") as f:
    for line in f:
        measures.append(int(line))

curr = sum(measures[0:3])
times_increased = 0 
for i in range(1, len(measures)):
    new = sum(measures[i:i+3])
    if new > curr:
        times_increased += 1
    curr = new

print(times_increased)

