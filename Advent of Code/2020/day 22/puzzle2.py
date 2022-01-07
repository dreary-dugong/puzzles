from collections import deque
from itertools import islice


#read input
with open("input1.txt") as f:

    players = f.read().split("\n\n")
    p1_deck = deque([int(n) for n in players[0].split("\n")[1:]])
    p2_deck = deque([int(n) for n in players[1].split("\n")[1:]])
        #deques here for O(1) add/remove


#play ball
def combat(p1, p2):
    """perform a game of recursive combat and return the winner."""

    old_rounds = set() #infinite loop prevention
    winner = 0
    while len(p1) > 0 and len(p2) > 0:
        
        #prevent loop
        if (tuple(p1), tuple(p2)) in old_rounds:
            winner = 1

            #draw cards
            c1, c2 = p1.popleft(), p2.popleft()
            
        else:

            #add this state to the set
            old_rounds.add((tuple(p1), tuple(p2)))

            #draw cards
            c1, c2 = p1.popleft(), p2.popleft()
            
            
            #can this round be resolved via recursion?
            if c1 <= len(p1) and c2 < len(p2):
                sub_p1 = deque(islice(p1, c1))
                sub_p2 = deque(islice(p2, c2))
                winner, sub_deck = combat(sub_p1, sub_p2)

            #otherwise, play the game normally
            elif c1 > c2:
                winner = 1
            else:
                winner = 2

        #add cards to winner's deck
        if winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    
    #whoever won the last round is overall winner
    if winner == 1:
        return 1, p1
    elif winner == 2:
        return 2, p2
    else:
        print("ERROROROEROEROEROEROEOREOROER")
        return 0, deque()
        

winner, win_deck = combat(p1_deck, p2_deck)

#print final score
score = 0
for i, c in enumerate(win_deck):
    score += (len(win_deck) - i) * c

print("\n\nFinal Score: " + str(score))
        
