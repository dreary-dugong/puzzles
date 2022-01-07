
#get input
inputFile = open("input.txt",  "r");
l = list(inputFile.readline().strip().split(","))
for i in range(len(l)):
    l[i] = int(l[i]);

#opcode functions
def add(a,b):
    return a+b;
def multiply(a,b):
    return a*b;

#Problem 1 change these
l[1] = 12;
l[2] = 2;

#process list
index = 0
opcode = l[index]
while opcode != 99:
    
    if opcode == 1:
        operation = add;
    elif opcode == 2:
        operation = multiply;

    l[l[index+3]] = operation(l[l[index+1]],l[l[index+2]]);

    index += 4;
    opcode = l[index];


print(l[0]);
