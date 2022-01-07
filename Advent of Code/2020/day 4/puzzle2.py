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

    #then all fields are present but we need to validate them. re would've been useful here but I'm stubborn
    if  isValid:
        if not(parsedPort["byr"].isnumeric() and 1920 <= int(parsedPort["byr"]) <= 2002):
               isValid = False;
               print("invalid byr")
        if not(parsedPort["iyr"].isnumeric() and 2010 <= int(parsedPort["iyr"]) <= 2020):
               isValid = False;
               print("invalid iyr")
        if not(parsedPort["eyr"].isnumeric() and 2020 <= int(parsedPort["eyr"]) <= 2030):
               isValid = False;
               print("invalid eyr")
               
        if not(parsedPort["hgt"][0:-2].isnumeric() and (parsedPort["hgt"][-2:] in ("cm", "in"))):
               isValid = False;
               print("invalid hgt")
        elif parsedPort["hgt"][-2:] == "in":
            if not(59 <= int(parsedPort["hgt"][0:-2]) <=76):
                   isValid = False;
                   print("invalid hgt")
        else:
            if not(150 <= int(parsedPort["hgt"][0:-2]) <= 193):
                   isValid = False;
                   print("invalid hgt")

        if not(parsedPort["hcl"][0]=="#" and len(parsedPort["hcl"]) == 7):
               isValid = False
               print("invalid hcl")
        else:
            for c in parsedPort["hcl"][-6:]:
                if not( (65 <= ord(c) <=90) or (97 <= ord(c) <= 122) or c.isnumeric()):
                    isValid = False;
                    print("invalid hcl")

        if not(parsedPort["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")):
               isValid = False;
               print("invalid ecl")

        if not(parsedPort["pid"].isnumeric() and len(parsedPort["pid"]) == 9):
               isValid = False;
               print("invalid pid")


        if isValid:
               numValid += 1;
    
print(numValid)
