#! /usr/bin/python3
# dayX.py -- solution for advent of code

from inputs import readInputs

inputs = readInputs(8)
sample = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390'
]


def countEdges(height, width): 
    edges = (height * 2) + ((width - 2) * 2)
    return edges


def solve(input:list[str]) -> int: 
    height = len(input)
    width = len(input[0])
    visible = countEdges(height, width)
    maxScore = 1

    def isEdge(i, j): 
        '''Checks if coordinate is on edge of grid'''
        if i == 0 or i == height - 1: 
            return True
        elif j == 0 or j == width - 1: 
            return True
        else:
            return False


    def neighbor(dir, i, j) -> int:
        '''Gets neighbor coordinates
        dir: 'up', 'down', 'left', 'right'
        '''
        if dir == 'up': 
            return (i - 1, j)
        elif dir == 'down': 
            return (i + 1, j)
        elif dir == 'left': 
            return (i, j - 1)
        else:
            return (i, j + 1)


    def search(tree, dir, i, j): 
        '''Traverses grid along vector of given direction (dir)
        part one: returns 1 if origin tree is visible along vector
        part two: returns count of trees visible from origin along vector
        '''
        view = 0 
        while not isEdge(i, j):
            newCoords = neighbor(dir, i, j)
            i, j = newCoords[0], newCoords[1]
            nextTree = int(input[i][j])
            view += 1
            # # part one
            # if nextTree >= tree: 
            #     return 0
            # else:
            #     continue

            # part two
            if isEdge(i, j) or nextTree >= tree: 
                return view
            else: 
                continue

        #part one 
        #return 1

        # part two
        return view

    def searchOrder(i, j) -> list: 
        '''Return list of directions in 
        ascending order of distance to edge
        '''
        orderDict = {
            'up': i, 
            'down': height - i,
            'left': j,
            'right': width - j
        }
        sortedOrder = dict(sorted(orderDict.items(), key=lambda x:x[1]))
        return sortedOrder


    for i in range(1,height-1):
        for j in range(1,width-1):
            tree = int(input[i][j])
            order = searchOrder(i, j)
            views = []
            # part one 
            #order = order.keys()
            # part two
            order = ['up', 'left', 'down', 'right']
            #print(f'({i},{j}) {tree}')
            for searchDir in order: 
                result = search(tree, searchDir, i, j)
                # part one
                # if result == 0: 
                #     continue
                # else: 
                #     visible += 1
                #     break

                # part two
                views.append(result)
            
            scenicScore = 1
            for view in views:
                scenicScore = scenicScore * view

            if scenicScore > maxScore: 
                maxScore = scenicScore

    return maxScore
    

solution = solve(inputs)
print(solution)