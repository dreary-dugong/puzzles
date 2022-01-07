def find_expression(s, start):
    """find the ending index to a parenthesized expression in a string"""
    numLeft = 1
    
    i = start
    while numLeft != 0:
        i += 1
        c = s[i]
        if c == "(":
            numLeft += 1
        elif c == ")":
            numLeft -= 1

    return i

def evaluate(s):
    """evaluate these strange expressions"""

    value = 0
    i = 0
    
    curr_operator = "+"
    
    while i + 1 < len(s):

        i += 2
        
        if s[i] == "(":
            curr_operand = evaluate(s[i+1:find_expression(s, i)])
        else:
            curr_operand =  int(s[i])

        if curr_operator == "+":
            value += curr_operand
        else:
            value *= curr_operand

        curr_operator = s[i+1]

    return value

def read_input(file_name):
    """return expression strings from file"""
    with open(file_name) as f:
        for line in f:
            yield line.replace(" ", "")

def main():
    input_file = "testInput1.txt"
    total = 0
    for expression in read_input(input_file):
        print("\nCurrent expression: " + expression)
        curr_evaluation = evaluate(expression)
        print("Evaluation: " + curr_evaluation)
        total += curr_evaluation

    print("=====================================")
    print("\nTotal of expressions: " + str(total))
    

if __name__ == "__main__":
    main()
