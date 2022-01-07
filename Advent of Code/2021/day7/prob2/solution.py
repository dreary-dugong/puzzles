def main():
    with open("input.txt") as f:
        nums = list(map(int, f.readline().split(",")))

    lower, upper = min(nums), max(nums) 
    bestcost = 999999999999
    for i in range(lower, upper+1):
        cost = 0
        for num in nums:
            dist = abs(num - i)
            cost += (dist**2 + dist)/2
        bestcost = min(bestcost, cost)

    print(bestcost)


if __name__ == "__main__":
    main()
