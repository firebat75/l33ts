def solution(nums):
    nums.sort()

    def backtracking(temp=[], i=0):
        temp.sort()
        if temp not in output:
            output.append(temp)

        if i < len(nums):
            backtracking(temp + [nums[i]], i + 1)
            backtracking(temp, i + 1)

    output = []
    backtracking()
    return output


print(solution([1, 2, 3]))
print(solution([0]))
print(solution([4, 4, 4, 1, 4]))
