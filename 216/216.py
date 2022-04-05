def solution(k, n):
    def backtracking(path, nums, k, n):
        path.sort()

        if k == 0 and n == 0 and path not in output:
            output.append(path)
        elif k < 0 or n < 0:
            pass
        else:
            for i in range(len(nums)):
                if nums[i] + (k - 1) > n:
                    break
                backtracking(
                    path + [nums[i]], nums[:i] + nums[i + 1 :], k - 1, n - nums[i]
                )

    output = []
    backtracking([], list(range(1, 9)), k, n)

    return output


print(solution(3, 7))
print(solution(3, 9))
print(solution(4, 1))
