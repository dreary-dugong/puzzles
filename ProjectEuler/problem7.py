import math

goal = int(input("Enter the nth prime:"))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
test = 23
while len(primes) < goal:
    test += 1
    isPrime = True
    prime = primes[0]
    yes = -1
    while prime < int(math.sqrt(test)):
        prime = primes[yes+1]
        if test%prime == 0:
            isPrime = False
    if isPrime == True:
        primes.append(test)
        print(test)
print("Goal: " + str(primes[goal-1]))
