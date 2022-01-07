import re

numcorrect = 0
with open("input1.txt") as file:
    for line in file:

        policy, pw = line.split(": "); #separate policy and password
        pos1, pos2, letter = re.split("-| ", policy); #parse policy
        pos1, pos2 = int(pos1), int(pos2)

        #check correctness
        if (pw[pos1 -1] == letter) != (pw[pos2-1] == letter): # != acts as xor here
            numcorrect += 1;

print(numcorrect)
