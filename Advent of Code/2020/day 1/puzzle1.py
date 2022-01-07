nums = {}
with open("input1.txt") as file:
    for line in file:
        nums[int(line)] = 0

for num in nums:
    if (2020 - num) in nums:
        print(num * (2020-num))
        break
