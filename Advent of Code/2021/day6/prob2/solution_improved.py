def main():

    #load file into dictionary
    with open("input.txt") as f:
        data = f.readline().replace("\n", "").split(",")
        fish = [data.count(str(i)) for i in range(9)]
    
    #simulate fish with rotating stack
    for _ in range(256):
        reproduce = fish.pop(0)
        fish.append(reproduce) #new fish have a 9 day cooldown
        fish[6] += reproduce #parents have a 7 day cooldown
    print(sum(fish))

if __name__ == "__main__":
    main()
