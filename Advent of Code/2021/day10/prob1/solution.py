from collections import deque

def get_syntax(infile):
    syntax = []
    with open(infile) as f:
        for line in f:
            syntax.append(line.strip(" \n"))
    return syntax

def main():
    infile = "input.txt"

    OPEN = {"{":"}", "(":")", "[":"]", "<":">"}
    SCORE = {")":3, "]":57, "}":1197, ">":25137}

    syntax = get_syntax(infile)
    cumScore = 0
    
    for line in syntax:
        stack = deque()
        validLine = True

        for char in line:

            #put opening brace on the stack
            if char in OPEN:
                stack.appendleft(char)
            else:
                
                #otherwise it's a closing brace
                if OPEN[stack[0]] == char:
                    stack.popleft()
                else:
                    cumScore += SCORE[char]
                    validLine = False
                    break

                        
    print(cumScore)


if __name__ == "__main__":
    main()

                    

