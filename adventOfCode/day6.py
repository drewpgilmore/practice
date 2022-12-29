#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs

inputs = readInputs(6)
#print(len(inputs))

def solve(input:list) -> int: 
    
    
    def containsDupes(str) -> bool: 
        i = 0
        while i < len(str): 
            if str[i] in str[i+1:]:
                return True
            else: 
                i += 1
                containsDupes(str[i:])

        return False
    
    
    index = 4
    data = input[0]
    for i in range(index - 1, len(data)):
        prevFour = data[i-3:i+1]
        if containsDupes(prevFour):
            index += 1
            continue
        else:
            return index

    return None

sample = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']

solution = solve(inputs)
print(solution)