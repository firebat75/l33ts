def solution(coins, amount):
    # def backtracking(path):
    #     if sum(path) == amount:
    #         output.append(len(path))
    #     elif sum(path) > amount:
    #         pass
    #     else:
    #         for coin in coins:
    #             backtracking(path + [coin])

    # output = []
    # backtracking([])
    # if not output:
    #     return -1
    # return min(output)
    if amount == 0:
        return 0
    value1 = [0]
    value2 = []
    nc = 0
    visited = [False] * (amount + 1)
    visited[0] = True
    while value1:
        nc += 1
        for v in value1:
            for coin in coins:
                newval = v + coin
                if newval == amount:
                    return nc
                elif newval > amount:
                    continue
                elif not visited[newval]:
                    visited[newval] = True
                    value2.append(newval)
        value1, value2 = value2, []
    return -1


print(solution([1, 2, 5], 11))
print(solution([2], 3))
print(solution([1], 0))
print(solution([186, 419, 83, 408], 6249))
