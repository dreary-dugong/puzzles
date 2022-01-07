import fuzzCreator

def stringDiff(s1, s2):
    for i in range(min(len(s1),len(s2))):
        if s1[i]!=s2[i]:
            print("Diff found at index: " + str(i))
            print("String 1: "  + s1[i] + "\tString 2: " + s2[i])
    if len(s1) > len(s2):
        print("String 1 has an extra '" + s1[len(s2):] + "' at the end.")
    elif len(s2) > len(s1):
        print("String 2 has an extra '" + s2[len(s2):] + "' at the end.")

def collide(char1, char2):
    if (char1.upper() == char2 and char2.lower() == char1) or (char2.upper() == char1 and char1.lower() == char2):
        return True
    return False


def react(polymer):

    copy = polymer
    polymer = list(polymer)
    MAX_PRINT_LEN = 0;
    polymerIds = [i for i in range(len(polymer))]

    if len(polymer) < MAX_PRINT_LEN:
        print("\n============================")
        print("Starting Polymer: " + "".join(polymer))
        

    #find initial collision points (by checking every letter)
    i = 0
    collisionIndices = []
    while i < len(polymer) - 1:
                
        if collide(polymer[i], polymer[i+1]):
            collisionIndices.append(i)
            complete = False
            i += 2
        else:
            i += 1
            
    #repeat until no collisions remain
    while len(collisionIndices) > 0:
            
        #remove collisions
        for offset, index in enumerate(collisionIndices):

                
            trueIndex = index - 2*offset
            #print("\nReacted '" + "".join(polymer[trueIndex:trueIndex+2]) + "' at index " + str(trueIndex))
                
            polymer = polymer[:trueIndex] + polymer[trueIndex+2:]
            polymerIds = polymerIds[:trueIndex] + polymerIds[trueIndex+2:]

            if len(polymer) < MAX_PRINT_LEN:
                print("After replace: ")
                print("".join(polymer))

        #determine which indices to check for subsequent collisions
        indicesToCheck = []
        for i, index in enumerate(collisionIndices):
            possibleIndex = index - 1 - 2*i
          
            if 0<= possibleIndex <= len(polymer)-2: #ensure it's a real index
                #prevent double checking
                if len(indicesToCheck) == 0:
                    indicesToCheck.append(possibleIndex)
                elif indicesToCheck[-1] != possibleIndex:
                    indicesToCheck.append(possibleIndex)


        #check for collisions only at these new points
        collisionIndices = []
        for i in indicesToCheck:
            if collide(polymer[i], polymer[i+1]):
                collisionIndices.append(i)
        #print("GOT HERE")

                
    #find overlooked collisions and print them
    for i in range(len(polymer)-2):
        if collide(polymer[i], polymer[i+1]):
            print(polymer[i] + polymer[i+1])
            print(polymerIds[i], polymerIds[i+1])
            print(copy[polymerIds[i]:polymerIds[i+1]])
                    
    return len(polymer), polymer

def brute(polymer):
    polymer = list(polymer)

    complete = False
    while not complete:
        complete = True
        for i in range(len(polymer)-1):
            if collide(polymer[i], polymer[i+1]):
                polymer = polymer[:i] + polymer[i+2:]
                complete = False
                break
    return len(polymer), polymer

def fuzz():

    for i in range(100):
        testPolymer = fuzzCreator.create_fuzz(50000)
        #testPolymer = open("input.txt", "r").read()
        algoLen = react(testPolymer)
        bruteLen = brute(testPolymer)
        if algoLen != bruteLen:
            print("\nAlgo: " + str(algoLen) + "\tBrute: " + str(bruteLen))
            print(testPolymer)

def compound(polymer):

    polymer = list(polymer)
    i = 0
    while i < len(polymer)-1:
        if not collide(polymer[i], polymer[i+1]):
            i += 1
        else:
            polymer = polymer[:i] + polymer[i+2:]
            i = max(i-1, 0)
    return len(polymer)
            
def debug():
    filename = "test1.txt"
    with open(filename, 'r') as f:
        testPolymer = f.read()
    algoLen, algoPoly = react(testPolymer)
    bruteLen, brutePoly = brute(testPolymer)
    print("\nAlgo: " + str(algoLen) + "\tBrute: " + str(bruteLen))
    stringDiff(algoPoly, brutePoly)

def main():
    with open("input.txt", "r") as f:
        polymer = f.read()
            
    minLen = len(polymer)
    for i in range(26):
        testLen = compound(polymer.replace(chr(i+97), "").replace(chr(i+65),""))
        if  testLen < minLen:
            minLen = testLen
            minLetter = chr(i+65)
    print(minLetter, minLen)
    
if __name__ == "__main__":
    main();


    
    
