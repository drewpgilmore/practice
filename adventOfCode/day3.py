

def compartments(items:str) -> tuple:
    """Takes string input and splits in half
    Returns tuple of first and second compartment
    """
    i = items.strip()
    half = len(i) // 2
    first = i[:half]
    second = i[half:]
    return (first, second)


def getCommonChars(str1:str, str2:str) -> list:
    """Returns list of chars in common between 2 lists""" 
    inCommon = []
    for char in str1:
        if char in str2 and char not in inCommon: 
            inCommon.append(char)
        else: 
            continue
    
    return inCommon


def getPriority(char:str) -> int: 
    """Returns priority for each letter"""

    value = ord(char)

    if char.islower():
        # base for lower 'a' is 97 -- want to return 1
        return value - 96
    else: 
        # base for upper 'A' is 65 -- want to return 27
        return value - 64 + 26


inputs = 'inputs/day3.txt'

with open(inputs, 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    c = compartments(line)
    first = c[0]
    second = c[1]
    inCommon = getCommonChars(first, second)
    print(inCommon)
    priorities = list(map(getPriority, inCommon))
    subTotal = sum(priorities)
    total += subTotal
    inCommon = []
    subTotal = 0

print(f'Total for Part 1: {total}')

# part 2

def getBage(first, second, third) -> str:
    """Looks at 3 packs, returns common char"""
    inCommon = None
    for char in first: 
        if char in second and char in third: 
            inCommon = char
            return inCommon

group = []
total = 0
for i in range(len(lines)):
    # look at every 3 rows
    items = lines[i].strip()
    group.append(items)
    if (i + 1) % 3 == 0: 
        print(f'{items} -> Full Group!')
        # check for badge
        badge = getBage(group[0], group[1], group[2])
        priority = getPriority(badge)
        print(f'Adding {priority}')
        total += priority
        group = []
    else: 
        print(f'{items}')
        
print(f'Total for part 2: {total}')
    # get their common letter (badge)
    
    # determine it's priority, add it to list