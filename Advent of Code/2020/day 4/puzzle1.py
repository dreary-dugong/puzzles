import re

#constants
necessaryFields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

#read file
with open("input1.txt") as f:
    raw = f.read();

#split on double enter to separate passsports
pp = raw.split("\n\n")

numValid = 0

#separate fields with re
for passport in pp:
    fields = re.split(" |\n", passport)

    #finish parsing field info
    parsedPort = {}
    for field in fields:
        currField = field.split(":")
        if len(currField) > 1: #handle empty input
            parsedPort[currField[0]] = currField[1]

    #check for missing fields
    isValid = True
    for field in necessaryFields:
        if field not in parsedPort:
            isValid = False
    if  isValid:
        numValid += 1
    
print(numValid)
