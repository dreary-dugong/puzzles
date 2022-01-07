import math
for i in range(999, 1, -1):
    print(str(i))
    attempt = (1000*(i-500))/(i-1000)
    print("Attempt: " + str(attempt))
    if math.sqrt(attempt**2 + i**2) + i + attempt == 1000:
        print("a, b, c = " + str(i), str(attempt), str(math.sqrt(attempt**2+i**2)))
