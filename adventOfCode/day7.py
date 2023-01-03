#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs

inputs = readInputs(7)


def getPath(dirs:list) -> str: 
    path = ''
    for dir in dirs: 
        if dir == '~' or dir == '/':
            path += dir
        else: 
            path += f'{dir}/'

    return path


def solve(input:str) -> int: 
    currentDir = ['~']
    root = {}
    for line in input: 
        cwd = currentDir[-1]
        things = line.strip().split(' ')
        path = getPath(currentDir)
        #print(path)
        if things[0] == '$': # process command
            command = things[1]
            if command == 'cd': 
                if things[2] == '..': 
                    currentDir.pop(-1) # remove most recent dir
                else:
                    cwd = things[2]
                    currentDir.append(cwd)
                    path = getPath(currentDir)
                    root[path] = 0
            elif command == 'ls':
                continue
        else: 
            if things[0] != 'dir': 
                size = int(things[0])
                for i in range(1,len(currentDir)):
                    path = getPath(currentDir[:i+1])
                    #print(path)
                    root[path] += size

    maxSize = 100_000
    total = 0
    for size in root.values(): 
        if size <= maxSize: 
            total += size


    # find smallest dir to delete that 
    # will free up enough space for update 
    totalSpace = 70_000_000
    reqSpace = 30_000_000
    usedSpace = root['~/']
    spaceAvailable = totalSpace - usedSpace
    spaceNeeded = reqSpace - spaceAvailable

    deleteDir = ''
    deleteDirSize = usedSpace

    if spaceAvailable >= reqSpace: 
        print("Enough space already available!")
    else: 
        for dir, size in root.items(): 
            if size >= spaceNeeded and size < deleteDirSize:
                deleteDir = dir
                deleteDirSize = size
            else: 
                continue

    return deleteDirSize

sample = [
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k'
]
#sampleSolution = solve(sample)
solution = solve(inputs)
print(solution)