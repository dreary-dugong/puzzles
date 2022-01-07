ans = 0
with open("testInput.txt") as f:

    groups = f.read().split("\n\n")

    for group in groups:

        possChars = []
        accChars = []
        
        for line in group:
            for char in line:
                if char not in possChars:
                    possChars.append(char)
        accChars = possChars
        for line in group:
            for char in accChars:
                if char not in line:
                    accChars.remove(char)

        ans += len(accChars)

print(ans)
