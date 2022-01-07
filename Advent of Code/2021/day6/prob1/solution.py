from copy import deepcopy

def main():

    #load file into dictionary
    fish = dict()
    for i in range(9):
        fish[i] = 0
    with open("input.txt") as f:
        for num in f.read().replace("\n", "").split(","):
            fish[int(num)] = fish[int(num)] + 1
    print(fish)
    
    #simulate for 80 days
    for _ in range(80):
        copyfish = deepcopy(fish)
        for i in range(8, 0, -1):
            fish[i-1] = copyfish[i]
        fish[8] = copyfish[0]
        fish[6] = fish[6] + copyfish[0]

    print(fish)

    print(sum(fish.values()))


if __name__ == "__main__":
    main()
