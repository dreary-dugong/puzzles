
times_increased = 0
with open("input.txt") as f:
    curr = int(f.readline())
    for line in f:
        if int(line) > curr:
            times_increased += 1
        curr = int(line)


print(times_increased)
    
