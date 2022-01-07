from collections import Counter
def main():


    #read input
    codes = []
    with open("input.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            codes = codes + line.split(" | ")[1].split(" ")
    
    counts = Counter(map(len, codes))
    print(counts[2] + counts[4] + counts[3] + counts[7])

if __name__ == "__main__":
    main()
