from copy import copy
from collections import defaultdict
def main():

    #load file into dictionary
    fish = defaultdict(lambda: 0) 
    with open("input.txt") as f:
        for num in f.readline().split(","):
            fish[int(num)] += 1
    
    #simulate for 256 days
    for _ in range(256):
        copyfish = copy(fish)
        for i in range(8, 0, -1):
            fish[i-1] = copyfish[i]
        fish[8] = copyfish[0]
        fish[6] += copyfish[0]


    print(sum(fish.values()))


if __name__ == "__main__":
    main()
