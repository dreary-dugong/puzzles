def main():

    with open("input.txt") as f:
        nums = []
        for line in f:
            nums.append(list(map(int, list(line.replace("\n","")))))
    print(nums[-1])

    
    risksum = 0
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            adjacent = []
            if i > 0:
                adjacent.append(nums[i-1][j])
            if i < len(nums) - 1:
                adjacent.append(nums[i+1][j])
            if j > 0:
                adjacent.append(nums[i][j-1])
            if j < len(nums[0]) - 1:
                adjacent.append(nums[i][j+1])
            if nums[i][j] < min(adjacent): 
                risksum += nums[i][j] + 1

    print(risksum)

if __name__ == "__main__":
    main()
