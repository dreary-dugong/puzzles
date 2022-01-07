#! /bin/python
#main.py


unparsedProblems = input()
numProblems = 0

pranges = unparsedProblems.split(";")

for prange in pranges:
    if "-" not in prange:
        numProblems += 1
    else:
        start, end = [int(n) for n in prange.split("-")]
        numProblems += end-start + 1

print(numProblems)
