#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs

inputs = readInputs(9)

sample_in = [
    '......',
    '......',
    '......',
    '......',
    'H.....'
]

sample = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'
]


def moveKnot(coord, dir) -> list: 
    if dir == 'R':
        return [coord[0], coord[1] + 1]
    elif dir == 'L':
        return [coord[0], coord[1] - 1]
    elif dir == 'U':
        return [coord[0] - 1, coord[1]]   
    else: 
        return [coord[0] + 1, coord[1]]


def show(visited:list) -> None: 
    grid = []
    left, right, up, down = 0, 0, 0, 0
    down  = min([coord[0] for coord in visited])
    up    = max([coord[0] for coord in visited])
    left  = min([coord[1] for coord in visited])
    right = max([coord[1] for coord in visited])

    width = right - left
    height = up - down
    print(f'Printing {width} x {height} grid')

    for i in range(height): 
        for j in range(width): 
            print(".", end="")
        print("\n")
    
    return None


def sampleGrid(head, tails): 
    for i in range(len(sample_in)): 
        for j in range(len(sample_in[0])):
            if [i, j] == head: 
                print("H",end="")
            elif [i, j] not in tails: 
                print(".",end="")
            else: 
                print("#",end="")
                # for i in range(1,len(tails) + 1): 
                #     if [i, j] == tails[i - 1]: 
                #         print(f'{i}', end="")
        print("\n")
    print("\n")

def moveTail(head, tail, dir):
    
    def isTouching(head, tail): 
        lr = abs(head[1] - tail[1])
        ud = abs(head[0] - tail[0])
        if lr <= 1 and ud <= 1: 
            return True 
        else: 
            return False

    def follow(head, dir): 
        if dir == 'R': 
            return [head[0], head[1] - 1]
        elif dir == 'L': 
            return [head[0], head[1] + 1]
        elif dir == 'U': 
            return [head[0] + 1, head[1]]
        else: 
            return [head[0] - 1, head[1]]
        
    if isTouching(head, tail) is False:
        tail = follow(head, dir)
    
    return tail





def solve(input):
    head = [4, 0]
    tail = head

    tails = [head for _ in range(8)]
    visited = [head]
    count = 0 

    for instruction in input: 
        moves = instruction.split(' ')
        dir = moves[0]
        steps = int(moves[1])
        for i in range(1, steps + 1): 
            count += 1
            #print(f'{instruction}: Step {i} -- ', end="")
            head = moveKnot(head, dir)
            #tail = moveTail(head, tail, dir)
            tempHead = head
            for i in range(8): 
                tails[i] = moveTail(tempHead, tails[i], dir)
                tempHead = tails[i]
                
            t = tails[-1]
            #print(f'Head={head} Tail={tail}')
            if t not in visited: 
                visited.append(t)
            
            sampleGrid(head, tails)

    return len(visited)


print(solve(sample))
#print(f'Visited coords: {visited}')