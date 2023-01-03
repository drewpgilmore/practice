#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs

inputs = readInputs(6)
#print(len(inputs))

def solve(input:list, numDistinct:int) -> int: 
    
    
    def containsDupes(str) -> bool: 
        i = 0
        while i < len(str): 
            if str[i] in str[i+1:]:
                return True
            else: 
                i += 1
                containsDupes(str[i:])

        return False
    
    
    index = numDistinct
    data = input[0]
    for i in range(index - 1, len(data)):
        prev = data[i - (numDistinct - 1):i + 1]
        if containsDupes(prev):
            index += 1
            continue
        else:
            return index

    return None

sample = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']

#assert solve(sample, 4) == 5
#assert solve(sample, 14) == 29

partOne = solve(inputs, 4)
partTwo = solve(inputs, 14)

print(partOne)
print(partTwo)