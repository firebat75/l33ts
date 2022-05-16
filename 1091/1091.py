import pandas

def solution(grid):

    if len(grid) == 1:
        return 1
    elif grid[0][0] == 1:
        return -1
    elif grid[-1][-1] == 1:
        return -1

    def findValidPaths(grid, pos):
        valid = []
        for i in range(pos[0]-1, pos[0]+2):
            for e in range(pos[1]-1, pos[1]+2):
                if (i < 0 or e < 0) or (i > len(grid)-1 or e > len(grid[0])-1) or (i == pos[0] and e == pos[1]): # invalid position
                    pass
                elif grid[i][e] == 0:
                    valid.append([i, e])



        return valid


    output = -1
    pathfound = False


    def dfs(path, temp):
        temp = [row[:] for row in grid]
        for item in path:
            temp[item[0]][item[1]] = "x"
        nonlocal output
        nonlocal pathfound
        pos = [path[-1][0], path[-1][1]]
        temp[pos[0]][pos[1]] = "o"
        if pos == [len(temp)-1, len(temp[0])-1]:
            print(f"PATH FOUND: {len(path)}, curr: {output}")
            print(pandas.DataFrame(temp))
            if pathfound == False:
                output = len(path)
                pathfound = True
            else:
                output = min(output, len(path))

        else:
            validMoves = findValidPaths(temp, pos)
            if (pathfound and len(path) < output) or not pathfound:
                for move in validMoves:
                    dfs(path + [move], temp)

    temp = [row[:] for row in grid]

    dfs([[0, 0]], temp)

    return output


# print(solution([[0,1],[1,0]]))
# print(solution([[0,0,0],[1,1,0],[1,1,0]]))
print(solution([[0,1,0,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,0,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))