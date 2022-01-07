def indexExists(i,l):
    """returns true if index i exists for indexable l"""
    if i >=0:
        if i >= len(l):
            return False;
    if i<0:
        if abs(i) > len(l):
            return False;
    return True;
        
def getProgram(inputFile):
    """Takes file name and returns program object decoded from text in that file"""
    file = open(inputFile,"r");
    line = file.readline();
    strings = list(line.strip().split(","))
    program = [];
    for string in strings:
        program.append(int(string));
    return program;

def add(a,b,dest,mem):
    """adds a and b, stores the result at dest in mem"""
    print(dest);
    mem[dest] = a+b;
    return mem;

def multiply(a,b,dest,mem):
    """multiplies a and b, stores the result at dest in mem"""
    mem[dest] = a*b;
    return mem;

def takeInput(dest,mem):
    """takes input from user and stores it at dest in mem"""
    i = int(input("The program requests input: "));
    mem[dest] = i;
    return mem;

def giveOutput(a, mem):
    """outputs value of address a in mem"""
    print("The program gives output: ", str(a));
    return mem;

def executeProgram(p):
    """takes program as input and executes it"""
    #constants:
    opcodes = {1:{"function":add,"params":3}, 
               2:{"function":multiply,"params":3},
               3:{"function":takeInput,"params":1},
               4:{"function":giveOutput,"params":1}
               } #store data about non-halt opcodes used to run the program


    #dynamic variables:
    memory = p; #store memory addresses used in the program
    opPointer = 0; #points to current opcode being executed

    #execute program
    while True:
        lead = str(memory[opPointer])
        if indexExists(-2, lead):
            opcode = int(lead[-2]+lead[-1]); #get opcode
        else:
            opcode = int(lead);

        if opcode == 99: #check for halt
            break;

        operation = opcodes[opcode];
        args = [] #keeps track of args to be passed to operation
        
        for i in range(1,operation["params"]):
            paramMode = 0;
            if indexExists(-(i+2),lead): #check param mode
                paramMode = int(lead[-(i+2)]);

            if paramMode == 0:
                args.append(memory[memory[opPointer+i]]); #address mode
            elif paramMode == 1:
                args.append(memory[opPointer+i]); #value mode

            args.append(memory[opPointer+operation["params"]]);

        #final argument is always an address
        
        if opCode == 4:
            operation["function"](memor[opPointer+1], opPointer);
        else:
            operation["function"](*args, memory); #perform operation on memory
        opPointer += operation["params"] +1 #update opPointer






def main():
    program = getProgram("input.txt");
    executeProgram(program);


if __name__ == "__main__":
    main();

