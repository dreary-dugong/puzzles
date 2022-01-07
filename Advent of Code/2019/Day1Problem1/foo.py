import math
inputFile = open("input.txt","r");

inputs = []
for line in inputFile:
    inputs.append(int(line.strip()));
    
a = 0
for n in inputs:
    a = a + math.floor(n/3)-2

print(a)
