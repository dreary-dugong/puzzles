#read input
with open("input1.txt") as f:

    players = f.read().split("\n\n")
    p1 = [int(n) for n in players[0].split("\n")[1:]]
    p2 = [int(n) for n in players[1].split("\n")[1:]]


#play ball
curr_round = 0
while len(p1) > 0 and len(p2) > 0:
    curr_round += 1

    print("\n-- Round " + str(curr_round) + " --")
    print("Player 1's deck: " + str(p1))
    print("Player 2's deck: " + str(p2))
    

    c1, c2 = p1.pop(0), p2.pop(0)

    print("Player 1 plays: " + str(c1))
    print("Player 2 plays: " + str(c2))
    if c1 > c2:
        winner = p1
        print("Player 1 wins the round!")
    else: #we don't account for draws yet
        winner = p2
        print("Player 2 wins the round!")

    winner.append(max(c1, c2))
    winner.append(min(c1, c2))


#print final score
score = 0
for i, c in enumerate(winner):
    score += (len(winner) - i) * c

print("\n\nFinal Score: " + str(score))
        
