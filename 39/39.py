def solution(candidates, target):
    def backtracking(path):
        path.sort()
        if sum(path) == target and path not in output:
            output.append(path)
        elif sum(path) > target:
            pass
        else:
            for i in range(len(candidates)):
                backtracking(path + [candidates[i]])

    output = []
    backtracking([])

    return output


print(solution([2, 3, 6, 7], 7))
print(solution([2, 3, 5], 8))
print(solution([2], 1))
