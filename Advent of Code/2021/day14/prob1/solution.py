from collections import Counter
from collections import deque

class Node():
    def __init__(self, value=None):
        self.next = None 
        self.value = value

def get_polymer(infile):
    with open(infile) as f:
        polymer = f.readline().strip()
    return polymer

def get_rules(infile):
    rules = dict()
    with open(infile) as f:
        ruleData = f.read().split("\n\n")[1]
    for ruleDatum in ruleData.strip().split("\n"):
        pair = ruleDatum[0:2]
        rep = ruleDatum[6]
        rules[tuple(pair)] = rep
    return rules

def linked_listify(s):
    fakeHead = Node()
    curr = fakeHead
    for c in s:
        curr.next = Node(c)
        curr = curr.next
    return fakeHead.next

def stringify(ll):
    out = []
    while ll.next:
        out.append(ll.value)
        ll = ll.next
    out.append(ll.value)
    return "".join(out)

def apply_rules(polymer, rules, numReps):
    head = linked_listify(polymer) 
    polymerLength = len(polymer)

    toCheck = deque()
    node = head
    while node.next:
        toCheck.append(node)
        node = node.next

    for _ in range(numReps):


        nextToCheck = deque()
        for node in toCheck:
            after = node.next
            pair = (node.value, after.value)
            if pair in rules:
                innerNode = Node(rules[pair])
                node.next = innerNode
                innerNode.next = after
                polymerLength += 1
                nextToCheck.append(node) 
                nextToCheck.append(innerNode)

        toCheck = nextToCheck

    polymerString = stringify(head)
    return polymerString

def main():
    infile = "input.txt"
    polymer = get_polymer(infile)
    rules = get_rules(infile)
    num_reps = 10 

    polymer = apply_rules(polymer, rules, num_reps)
    
    charCounts = Counter(polymer)
    mostCount = charCounts.most_common(1)[0][1]
    leastCount = charCounts.most_common()[-1][1]
    print(mostCount-leastCount)
    

if __name__ == "__main__":
    main()
        

