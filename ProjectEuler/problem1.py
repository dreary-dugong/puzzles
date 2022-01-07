#!/usr/env/python 3
#3and5Sum
#finds the sum of the multiples of 3 and 5 under 1000
import math
total = 0
for x in range(1000):
    if math.floor(x/3) == x/3:
        total += x
    elif math.floor(x/5) == x/5:
        total += x
print(str(total))
