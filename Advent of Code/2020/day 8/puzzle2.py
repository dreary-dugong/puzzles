import copy


def execute(program):
    ran = [] #instructions that have been run
    acc = 0;
    looped = False; #has the program looped yet
    currIndex = 0; #index of the current instruction

    while currIndex != len(program) and not looped:

        #decode instruction
        currInst = program[currIndex]
        command = currInst.split(" ")[0]
        arg = int(currInst.split(" ")[1])

        #add to the list of ran instructions
        ran.append(currIndex)
        
        if command == "acc":
            acc += arg

        #what's the next instruction
        if command == "jmp":
            currIndex += arg
        else:
            currIndex += 1

        #check if we've already run the next inst
        if currIndex in ran:
            looped = True

    return acc, not looped, ran



def main():
    #put instructions into the list
    program = []
    with open("input1.txt") as f:
        for line in f:
            program.append(line.replace("\n", ""))


    #run the program once to see which instructions execute
    _, __, testPool = execute(program)

    testIndex = 0
    found = False

    #try replacing every jmp and nop that ran until we find it
    while testIndex < len(testPool) and not found:
        
        action = program[testPool[testIndex]].split(" ")[0]
        if action in ("jmp", "nop"):

            testProgram = copy.deepcopy(program)

            if (action == "jmp"):
                testProgram[testPool[testIndex]] = testProgram[testPool[testIndex]].replace("jmp", "nop")
            else:
                testProgram[testPool[testIndex]] = testProgram[testPool[testIndex]].replace("nop", "jmp")
                      
            acc, found, __ = execute(testProgram)
        testIndex += 1

    if found:
        print(acc)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
