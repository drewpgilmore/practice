inputs = 'inputs/day1.txt'

with open(inputs, 'r') as f:
    lines = f.readlines()

elves = {}
currentElf = 0
currentCals = 0
largest = 0

for i in range(len(lines)):
    #calories = int(lines[i])
    if lines[i] == '\n':
        if currentCals > largest:
            largest = currentCals
        elves[currentElf] = currentCals
        currentElf += 1
        currentCals = 0
    else: 
        currentCals += int(lines[i])


print(largest)