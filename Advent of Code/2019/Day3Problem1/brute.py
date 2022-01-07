#parse input
inputFile = open("testInput.txt","r");
wires =[]
for line in inputFile:
    wires.append(line.strip().split(","));


positionSets = []
for wire in wires:
    steps = 0;
    x = 0;
    y = 0;
    positions = []
    for instruction in wire:
        instructionLen = int(instruction[1::]);
        
        for i in range(instructionLen):
            if instruction[0] == "U":
                y +=1;
            elif instruction[0] == "D":
                y-=1;
            elif instruction[0] == "R":
                x+=1;
            elif instruction[0] == "L":
                x-=1;
            steps+=1

            positions.append((x,y));

        positionSets.append(positions);

for position in positionSets[0]:
    if position in positionSets[1]:
        print(position);
