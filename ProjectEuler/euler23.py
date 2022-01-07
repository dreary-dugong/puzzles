import math;
def isAbundant(n):
    total = n;
    for i in range(1, int(math.sqrt(n+1))):
        if n % i == 0:
            total += i + (n//i)
    if total > n:
        return True;
    return False;

total = 0;
abundants = [12];
for i in range(1, 28123):
    for j in range(abundants[-1]+1, i):
        if isAbundant(j):
            abundants.append(j);
    isSum = False;
    for abundant in abundants:
        if i-abundant in abundants:
            isSum = True;
            break;
    if isSum:
        total += i;
print(total);
