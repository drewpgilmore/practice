#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs


def parseLine(line:list) -> list:
    """Returns clean line"""
    line = line.strip() # remove \n
    line = line.split(',') 
    line = [list(map(int, l.split('-'))) for l in line]
    return line


# part 1: how many assignment pairs have one fully contain the other
def partOne(input:list) -> int:
    iterations = 0
    answer = 0


    def contains(first:list, second:list) -> int: 
        """Checks for one assignment fully containing the other"""
        if first[0] >= second[0] and first[1] <= second[1]:
            return 1
        elif second[0] >= first[0] and second[1] <= first[1]:
            return 1
        else:
            return 0 


    for line in input:
        iterations += 1
        l = parseLine(line)
        #print(l)
        result = contains(l[0], l[1])
        answer += result

    return answer

# part 2: how many assignment pairs have any overlap
def partTwo(input:list) -> int:
    iterations = 0
    answer = 0 

    def overlap(first:list, second:list) -> int:
        # [[2-6], [4-8]]
        # [[4-8], [2-6]]
        if second[0] <= first[0] <= second[1]:
            return 1
        elif first[0] <= second[0] <= first[1]:
            return 1 
        else:
            return 0

    for line in input: 
        iterations += 1
        l = parseLine(line)
        result = overlap(l[0], l[1])
        answer += result

    return answer


sample = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]

# test sample input         
test1 = partOne(sample)
try: 
    assert test1 == 2
    print("Test 1 Passed")
except AssertionError:
    print(f'Test 1 returned: {test1}')

test2 = partTwo(sample)
try:
    assert test2 == 4
    print("Test 2 Passed")
except AssertionError:
    print(f'Test 2 returned: {test2}')

# final solution
print('Final Solution:')
inputs = readInputs(4)
print(f'Part 1: {partOne(inputs)}')
print(f'Part 2: {partTwo(inputs)}')