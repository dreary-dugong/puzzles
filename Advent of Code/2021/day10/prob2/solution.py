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
    SCORE = {"(":1, "[":2, "{":3, "<":4}

    syntax = get_syntax(infile)
    lineScores = [] 
    
    for line in syntax:
        stack = deque()
        isCorrupt=False

        for char in line:

            #put opening brace on the stack
            if char in OPEN:
                stack.appendleft(char)
            else:
                
                #otherwise it's a closing brace
                if OPEN[stack[0]] == char:
                    stack.popleft()
                else:
                    break

        #only unclosed open braces are left on the stack
        else:
            score = 0
            for char in stack:
                score *= 5
                score += SCORE[char]
            lineScores.append(score)


    #get median line score
    scores = sorted(lineScores)
    print(scores[len(scores)//2])



if __name__ == "__main__":
    main()

                    

