def solution(stones):
    while len(stones) > 1:
        stones.sort()
        if stones[-1] == stones[-2]:
            stones = stones[:-2]
        else:
            stones = stones[:-2] + [stones[-1] - stones[-2]]

    if not stones:
        return 0
    return stones[0]


print(solution([2, 7, 4, 1, 8, 1]))
print(solution([1]))
