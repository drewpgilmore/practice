inputs = 'inputs/day2.txt'

with open(inputs, 'r') as f:
    lines = f.readlines()

game = {
    'rock': {
        'bonus': 1, 
        'beats': 'scissors',
        'losesTo': 'paper'
    },
    'paper': {
        'bonus': 2, 
        'beats': 'rock',
        'losesTo': 'scissors'
    },
    'scissors': {
        'bonus': 3,
        'beats': 'paper',
        'losesTo': 'rock'
    }
}

aliases = {
    'A': ['rock', None], 
    'B': ['paper', None],
    'C': ['scissors', None], 
    'X': ['rock', 'lose'],
    'Y': ['paper', 'draw'],
    'Z': ['scissors', 'win']
}


myScore = 0

for line in lines: 
    moves = line.split(' ')
    oppMove = aliases[moves[0][0]]
    myMove = aliases[moves[1][0]]
    
    

    bonus = bonusPoints(moves[1][0])
    myScore += bonus
    print(myScore)

print(f"Final answer: {myScore}")


# part 2
    
myScore = 0

for line in lines: 
    moves = line.split(' ')
    oppMove = aliases[moves[0]][0]
    targetResult = aliases[moves[1][0]][1]
    if targetResult == 'draw': 
        myMove = oppMove
        points = 3
    elif targetResult == 'win': 
        myMove = game[oppMove]['losesTo']
        points = 6
    else: 
        myMove = game[oppMove]['beats']
        points = 0
    bonus = game[myMove]['bonus']
    myScore += points
    myScore += bonus
    #print(f'{targetResult} -> {oppMove}:{myMove} Points {points} Bonus {bonus}')

print(f"Final for round 2: {myScore}")