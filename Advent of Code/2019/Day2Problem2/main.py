
#get input
inputFile = open("input.txt",  "r");
initial = list(inputFile.readline().strip().split(","))
for i in range(len(initial)):
    initial[i] = int(initial[i]);

#opcode functions
def add(a,b):
    return a+b;
def multiply(a,b):
    return a*b;

#returns number of arguments for a function
def getArgs(func):
    pass;

#returns basic debug info about variables in human-readable format
def getDebug(*args):
    string = "";
    for arg in args:
        string += f"""
                        Name: {arg.__name__}
                        Value: {arg}
                """
        

#process list
def compute(noun, verb, memory):
    opcodes = {1:add, 2:multiply};

    memory[1] = noun;
    memory[2] = verb;
    
    index = 0
    opcode = memory[index]
    while opcode != 99:

        try:
            operation = opcodes[opcode];
        except:
            print(noun, verb, memory, index, opcode);

        memory[memory[index+3]] = operation(memory[memory[index+1]],memory[memory[index+2]]);

        index += 4;
        opcode = memory[index];

    return memory[0]



#find value
def main():
    for noun in range(100):
        for verb in range(100):
            copy = initial + [];
            if compute(noun,verb,copy) == 19690720:
                print(noun*100+verb);

if __name__ == "__main__":
    main();
