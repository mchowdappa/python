# List
players = [10,20, 30, 40, 50, 40, 30, 45]

print players

print players[2]

# Update

players[3] = 99

print players

print players[:2]

print players[-2]
print players[2:-9]
print players[2:-6]
print players[2:-5]

print players[2:6]
players[2:6] = [0,0,0,0]

print players

print "Are appended? "+ str(players)+ str([100])
print players
players.append(100)

print players


## Clear list

players = []

print players
