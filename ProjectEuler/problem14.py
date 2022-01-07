Max = 0
answer = 0
for i in range(1, 1000000, 1):
    print(str(i))
    p = i
    n = i
    length = 0
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        length += 1
    if length > Max:
        Max = length
        answer = p

print("Answer: " + str(answer))
