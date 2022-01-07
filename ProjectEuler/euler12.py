import math;
n = 0;
triangleNum = 0;
while True:
    n+= 1;
    triangleNum += n;
    print(triangleNum);

    divisors = 0;
    for i in range(1, int(math.sqrt(triangleNum)+1)):
        if triangleNum % i == 0:
            divisors += 2;
    if divisors >= 500:
        break
print(triangleNum);
    
