import math
inputFile = open("input.txt","r");

inputs = []
for line in inputFile:
    inputs.append(int(line.strip()));

def getFuel(n):
    return math.floor(n/3)-2

total = 0;
for n in inputs:
    while True:
        n = getFuel(n);
        if n <= 0:
            break;
        total += n;
        

print(total);
