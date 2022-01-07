#! /bin/python
#quadrantSelction.py

#determine which quadrant on the cartesian plane each point lies in


x = int(input())
y = int(input())

if x > 0 and y > 0:
    quad = 1
elif x < 0 and y > 0:
    quad = 2
elif x < 0 and y < 0:
    quad = 3
else:
    quad = 4
print(quad)
