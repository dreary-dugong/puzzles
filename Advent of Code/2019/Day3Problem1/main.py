#parse input
inputFile = open("input.txt","r");
wires =[]
for line in inputFile:
    wires.append(line.strip().split(","));

class position(object):
    def __init__(self, x, y, steps):
        self.x = x;
        self.y = y;
        self.steps = steps;
    def __eq__(self, other):
        assert type(other) == type(self);
        if self.x == other.x and self.y == other.y:
            return True;
        return False;
    def __lt__(self, other):
        assert type(other) == type(self);
        if self.x < other.x:
            return True
        if self.x == other.x and self.y < other.y:
            return True;
        return False;
    def __gt__(self, other):
        assert type(other) == type(self);
        if self.x > other.x:
            return True;
        if self.x == other.x and self.y > other.y:
            return True;
        return False;
    def __ge__(self,other):
        if self == other or self > other:
            return True;
        return False;
    def __le__(self,other):
        if self == other or self < other:
            return True;
        return False;
    def __str__(self):
        return f"""x:{self.x}, y:{self.y}, steps:{self.steps}"""

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

            #binary search for position in list
            currentPos = position(x,y,steps)
            
            if len(positions) == 0:
                positions.append(currentPos);
            elif currentPos > positions[-1]:
                positions.append(currentPos);
            elif currentPos < positions[0]:
                positions.insert(0, currentPos);
            else:

                divisor = 2
                found = False;
                mid = (len(positions)-1)//divisor+1
                
                while not found:
                    divisor *= 2;
                    lower = positions[mid];
                    upper = positions[mid+1];
                    increment = len(positions) // divisor;
                    if increment == 0:
                        increment = 1;

                    if currentPos > upper:
                        mid = mid + increment;
                        next;
                    elif currentPos < lower:
                        mid = mid - increment;
                        next;
                    elif currentPos == upper or currentPos == lower:
                        found = True;
                        next;
                    else:
                        positions.insert(mid, currentPos);
                        found = True;
                        
    positionSets.append(positions);
    print("Wire done.");




#restructure with binary search
intersections = [];
for i in range(len(positionSets[0])):
    position = positionSets[0][i];
    if i%1000 == 0:
        print(int((i/len(positionSets[0]))*100))

    divisor = 2;
    mid = len(positionSets[1])//divisor
    if  position == positionSets[1][0]:
        intersections.append(position);
    elif position == positionSets[1][-1]:
        intersections.append(position);

    for j in range(len(positionSets[1])):
        if position == positionSets[1][j]:
            position.steps += positionSets[1][j].steps
            intersections.append(position);
"""        
    while True:       
        divisor *= 2
        increment = len(positionSets[1])//divisor
        if increment == 0:
            increment = 1;
            
        #not in list
        if (positionSets[1][mid] == positionSets[1][0] or
            positionSets[1][mid] == positionSets[1][-1] or
            (position > positionSets[1][mid] and position < positionSets[1][mid+1])):
            break
        
        elif position == positionSets[1][mid]:
            position.steps += positionSets[1][mid].steps;
            intersections.append(position);
            print("Intersection found.");
            break;
        
        elif position > positionSets[1][mid]:
            mid += increment;
        else:
            mid -= increment;
        
    
"""
    
steps = [];
for intersection in intersections:
    print(str(intersection));
    steps.append(intersection.steps);

    
print(min(steps));
    
            
        

