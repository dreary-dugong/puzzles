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

    if not found:
        print("Number " + str(nums[i]) + " at position " +
              str(i) + ".")
        print("Cannot find " + str(nums[i]) + "-" + str(nums[j]) +
              " in " + str(nums[i-preamble : i]) + "\n")
        break







#kattis
#do a trivial problem
#maybe push yourself to do more
#(easy or medium)
#personally, maybe read the Java API
    #-learn about data structures at least
    #java regex maybe
    #lambda?
