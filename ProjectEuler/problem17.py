def getLetters(number):
    digits = list(str(number))
    ones = int(digits[len(digits)-1])
    letters = 0
    if number > 10:
        tens = digits[len(digits)-2]
    else:
        tens = 0
    tenOne = int(str(tens) + str(ones))
    if tenOne < 10 or tenOne > 20:
        if ones == 1 or ones == 2 or ones == 6:
            letters += 3
        elif ones == 3 or ones == 7 or ones == 8:
            letters += 5
        elif ones == 4 or ones == 5 or ones == 9:
            letters += 4
    if tenOne > 10 and tenOne < 20:
        if tenOne == 11 or tenOne == 12:
            letters += 6
        elif tenOne == 13 or tenOne == 14 or tenOne == 19:
            letters += 8
        elif tenOne == 15 or tenOne == 16:
            letters += 7
        elif tenOne == 17 or tenOne ==18:
            letters += 9
    tens = int(tens)
    if tens > 1:
        if tens == 2 or tens == 3 or tens == 9 or tens == 8:
            letters += 6
        elif tens == 4 or tens == 5 or tens == 6:
            letters += 5
        elif tens == 7:
            letters += 7
    if number > 100:
        hundreds = int(digits[len(digits)-3])
        if hundreds == 1 or hundreds == 2 or hundreds == 6:
            letters += 3
        elif hundreds == 3 or hundreds == 7 or hundreds == 8:
            letters += 5
        elif hundreds == 4 or hundreds == 5 or hundreds == 9:
            letters += 4
        letters += 7
        if tens > 0 or ones > 0:
            letters += 3
    return letters

def main():
    total = 0
    for i in range(0, 1000, 1):
        total += getLetters(i)
    print(str(total))
    
def debug():
    test = int(input("Enter a number to test: "))
    print(getLetters(test))
main()
