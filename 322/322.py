def solution(coins, amount):
    if amount == 0:
        return 0
    value1 = [0]
    value2 = []
    nc = 0
    visited = [False] * (amount + 1)
    visited[0] = True
    while value1:
        print(f"value1: {value1}")
        print(f"value2: {value2}")
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
                print(f"nc:{nc}-coin:{coin}-newval:{newval}-value2:{value2}")
        value1, value2 = value2, []
    return -1


print(solution([1, 2, 5], 11))
print(solution([2], 3))
print(solution([1], 0))
# print(solution([186, 419, 83, 408], 6249))
