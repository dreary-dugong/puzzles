

pattern = input()
lineNum = 1
while pattern != "END":

    if(pattern == pattern[::-1]):
        print(str(lineNum) + " EVEN")
    else:
        print(str(lineNum) + " NOT EVEN")

    pattern = input()
    lineNum += 1
