

#read input file
increments = [];
previousFrequencies = [];
with open("input.txt") as f:
    for line in f:
        increments.append(int(line));

frequency = 0;
numRepeats = 0;
#repeat changes until a frequency repeats
index = 0;
while frequency not in previousFrequencies:
    previousFrequencies.append(frequency);
    frequency += increments[index];
    index += 1;
    if index >= len(increments):
        index = 0;
        numRepeats += 1;
        if numRepeats % 100 == 0 and numRepeats != 0:
            print("\nNumber of times through the increments: " + str(numRepeats))
            print("Number of unique frequencies: " + str(len(previousFrequencies)));
print("First frequency to repeat: " + str(frequency));
    
