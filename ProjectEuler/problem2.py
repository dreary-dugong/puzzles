a = 0
b = 1
c = 0
total = 0
import math
while c < 4000000:
    c = b + a
    a = b
    b = c
    if c/2 == math.floor(c/2):
        total += c

print(str(total))
