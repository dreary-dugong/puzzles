nums = {}
found = False
with open("input1.txt") as file:
    for line in file:
        nums[int(line)] = 0

for one in nums:
    for two in nums:
        three = 2020 - one - two
        if three in nums:
            print(one * two * three)
            found = True
            break
    if found:
         break

