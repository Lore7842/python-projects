# 1 if there is a room, 0 otherwise

rooms = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

i = int(input('How many players? '))

steps = []

# First player, second player, etc..

for player in range(0, i):
    steps.append({
        'num': player,
        'finished': False,
        'numeroMosse': 0,
        'posizione-x': 0,
        'posizione-y': 0
    })

finished = False
currentPlayer = 0

while(finished == False):
    finished = True
    if (currentPlayer % i == 0):
        currentPlayer = 0

    if (steps[currentPlayer]['finished'] == True):
        currentPlayer = currentPlayer + 1

    move = input(str(currentPlayer+1) +
                 ' plays: choose the move(s = sotto, w = sopra, d = destra, a = sinistra)\n')

    if (move == 's'):
        if (steps[currentPlayer]['posizione-y'] == 4 or rooms[steps[currentPlayer]['posizione-x']+1][steps[currentPlayer]['posizione-y']] == 0):
            steps[currentPlayer]['finished'] = True
            steps[currentPlayer]['numeroMosse'] += 1

        else:
            steps[currentPlayer]['posizione-x'] += 1
            steps[currentPlayer]['numeroMosse'] += 1

    if (move == 'w'):
        if (steps[currentPlayer]['posizione-x'] == -1 or rooms[steps[currentPlayer]['posizione-x']-1][steps[currentPlayer]['posizione-y']] == 0):
            steps[currentPlayer]['finished'] = True
            steps[currentPlayer]['numeroMosse'] += 1

        else:
            steps[currentPlayer]['posizione-x'] -= 1
            steps[currentPlayer]['numeroMosse'] += 1

    if (move == 'd'):
        if (steps[currentPlayer]['posizione-y'] == 4 or rooms[steps[currentPlayer]['posizione-x']][steps[currentPlayer]['posizione-y']+1] == 0):
            steps[currentPlayer]['finished'] = True
            steps[currentPlayer]['numeroMosse'] += 1

        else:
            steps[currentPlayer]['posizione-y'] += 1
            steps[currentPlayer]['numeroMosse'] += 1

    if (move == 'a'):
        if (steps[currentPlayer]['posizione-x'] == 0 or rooms[steps[currentPlayer]['posizione-x']][steps[currentPlayer]['posizione-y']-1] == 0):
            steps[currentPlayer]['finished'] = True
            steps[currentPlayer]['numeroMosse'] += 1

        else:
            steps[currentPlayer]['posizione-y'] += 1
            steps[currentPlayer]['numeroMosse'] += 1

    currentPlayer += 1
    for index in range(0, i):
        if (steps[index]['finished'] == False):
            finished = False

for indexF in range(0, i):
    print('Giocatore ' + str(indexF) + '\nNumero mosse: ' + str(steps[indexF]['numeroMosse']) + '\nPosizione finale (ultima stanza valida visitata) (x,y):  (' + str(
        steps[indexF]['posizione-x']) + ', ' + str(steps[indexF]['posizione-y']) + ')\n')
