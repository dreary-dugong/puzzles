#read file
fileName = "input.txt"
numDoubles = 0;
numTriples = 0;

with  open(fileName, 'r') as f:
    
    for word in f:
        hasDouble = False;
        hasTriple = False;
        
        for i in range(97, 123):
            counter = 0;
            
            for letter in word:
                if letter == chr(i):
                    counter+=1;
                    
            if counter == 2:
                hasDouble = True;
            elif counter == 3:
                hasTriple = True;
    
        if hasDouble:
            numDoubles += 1;
        if hasTriple:
            numTriples += 1;
            
print("Checksum: " + str(numDoubles * numTriples))
        
