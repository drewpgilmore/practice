#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs


def solve(input:list, part:int) -> str:
    answer = ''


    def height(input:list) -> int:
        '''Get height of tallest stack of crates'''
        i = 0
        while i >= 0:
            if input[i][1] == '1':
                return i
            else: 
                #print(input[i])
                i += 1

    h = height(input)
    crates = input[:h]
    crateLine = input[h]
    crateNumbers = [crateLine[i] for i in range(1,len(crateLine),4)]
    crateDict = {crate: [] for crate in crateNumbers}

    # pivot crates to dict
    for i in range(1,len(crateLine)-1,4): 
        c = crateLine[i]
        for j in range(h):
            thing = crates[j][i]
            if thing != ' ':
                crateDict[c].insert(0,thing)
            else:
                continue
    
    instructions = input[h + 2:]
    
    
    def followInstruction(crateDict, instruction, part): 
        '''Performs action on crateDict from instructions'''
        steps = instruction.split(' ')
        num = int(steps[1])
        fromCrate = steps[3]
        toCrate = steps[5]

        if part == 1:
            for i in range(num): 
                item = crateDict[fromCrate].pop(-1)
                crateDict[toCrate].append(item)
        else: 
            l = len(crateDict[fromCrate])
            items = crateDict[fromCrate][(l - num):]
            print(items)
            crateDict[fromCrate] = crateDict[fromCrate][:l - num]
            crateDict[toCrate] = crateDict[toCrate] + items

        return crateDict


    # read and execute all instructions
    for instruction in instructions: 
        crateDict = followInstruction(crateDict, instruction, part)
    
    # make return string
    for i in range(1,len(crateDict)+1):
        answer += crateDict[str(i)][-1]
    
    return answer


inputs = readInputs(5)

partOne = solve(input=inputs, part=1)
partTwo = solve(input=inputs, part=2)
print(f'''
Part 1: {partOne}
Part 2: {partTwo}
''')