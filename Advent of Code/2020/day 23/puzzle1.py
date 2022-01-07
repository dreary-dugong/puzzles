from collections import deque

INP = "389125467"
NUM_ROUNDS = 100
NUM_TO_MOVE = 3

cups = [int(c) for c in INP]
MIN_CUP = min(cups)
MAX_CUP = max(cups)

curr_cup = len(cups) - 1
for __ in range(NUM_ROUNDS):

    curr_cup = (curr_cup + 1) % len(cups)

    print(cups, curr_cup)

    target = cups[curr_cup] - 1

    to_add = []
    for i in range(1, NUM_TO_MOVE + 1):
        to_add.append(cups.pop((curr_cup + 1) % len(cups)))
        
    while target not in cups:
        target -= 1
        if target < MIN_CUP:
            target = MAX_CUP

        
    for i, item in enumerate(to_add):
        cups.insert(cups.index(target) + i + 1, item)

    if cups.index(target) < curr_cup:
        print("kms")
        for i in range(3):
            cups.append(cups.pop(0))
