class Step():
    def __init__(self, name):
        self.name = name;
        self.preReqs = []
    

steps = []

#read text file
filename = "input.txt"
with open(filename, "r") as f:
    for line in f:

        tokens = line.split(" ")
        pre = tokens[1]
        post = tokens[-3]

        preFound = False;
        postFound = False
        for step in steps:
            if step.name == post:
                step.preReqs.append(pre)
                postFound = True;
            elif step.name == pre:
                preFound = True;

        if not postFound:
            newStep = Step(post)
            newStep.preReqs.append(pre)
            steps.append(newStep)
        if not  preFound:
            steps.append(Step(pre))

#search through list to find steps that can be performed
order = ""
complete = []
ready = []
toRemove = []
for step in steps:
    if len(step.preReqs) == 0:
        ready.append(step.name)
        toRemove.append(step)
        
for step in toRemove:
    steps.remove(step)
toRemove = []

#repeat until no steps remain
while len(ready) > 0:
    #perform first step alphabetically
    ready.sort()
    complete.append(ready[0])
    order = order + ready[0]
    ready = ready[1:]

    #update ready list
    toRemove = []
    for step in steps:
        isReady = True
        for r in step.preReqs:
            if r not in complete:
                isReady = False;
        if isReady:
            toRemove.append(step)
            ready.append(step.name)
    for step in toRemove:
        steps.remove(step)
    toRemove = [];
            
print(order)

            
        
