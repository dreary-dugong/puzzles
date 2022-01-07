

def main():

    #load input into a list
    with open("input.txt") as f:
        report = f.readlines()
    report = [n.replace("\n", "") for n in report]

    digitcount = len(report[0]) 
    #take column totals
    counts = [sum([int(n[i]) for n in report]) for i in range(digitcount)]

    #calculate gamma
    gamma = 0
    for i in range(digitcount):
        gamma += 2**i * (counts[digitcount-i-1] > len(report)//2)

    #epsilon is gamma xor 111111...
    epsilon = gamma ^ 2**digitcount-1 
    energy = gamma*epsilon
    print(counts)
    print(f"{gamma=} {epsilon=} {energy=}")

if __name__ == "__main__":
    main()
