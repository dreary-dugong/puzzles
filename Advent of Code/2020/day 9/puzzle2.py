import math

preamble = 25
nums = []

with open("input1.txt") as f:
    for line in f:
        nums.append(int(line))

for i in range(preamble, len(nums)): #loop through every number after preamble

    found = False; #have we found two numbers that add to this yet
    
    for j in range(i-preamble, i): #loop through every number before to search
        
        #is there a match?
        if nums[i] - nums[j] in nums[i - preamble : i]:
            found = True;
            break

    #find number that breaks the pattern
    if not found:
        target = nums[i]
        break


#search through every set of contiguous numbers until we find the sequence
found = False
for start in range(len(nums)):
    end = start + 1
    while end < len(nums) and (not found) and sum(nums[start:end]) < target:
        end += 1
        if sum(nums[start:end]) == target:
            found = True
            print(max(nums[start:end]) + min(nums[start:end]))
