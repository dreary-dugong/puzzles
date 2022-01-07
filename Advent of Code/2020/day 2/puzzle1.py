import re

numcorrect = 0
with open("input1.txt") as file:
    for line in file:

        policy, pw = line.split(": "); #separate policy and password
        mini, maxi, letter = re.split("-| ", policy); #parse policy
        mini, maxi = int(mini), int(maxi)

        #check correctness
        counter = 0
        for l in pw:
            if l == letter:
                counter += 1
        if counter >= mini and counter <= maxi:
            numcorrect += 1

print(numcorrect)
