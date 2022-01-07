import math
answer = 0
def isPalindrome(number):
    if str(number) == (number)[::-1]:
        return True
    return False

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        print("i: "+ str(i))
        print("j: " + str(j))
        if isPalindrome(i*j):
            answer = i*j
        print("Answer: " + str(answer))
	if answer != 0:
            break
print("Answer: " + str(answer))

i: 245
j: 532
Answer: 227722
