#put instructions into the list
program = []
with open("input1.txt") as f:
    for line in f:
        program.append(line.replace("\n", ""))


#run the program
ran = [] #list of lines that have run already

acc = 0;
looped = False; #has the program looped yet
currIndex = 0; #index of the current instruction

while not looped:

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

print("Number of instructions run: " + str(len(ran)))
print(acc)
    
