def solution(nums):
    def permute(nums):
        res = []
        dfs(nums, [], res)
        return res

    def dfs(nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)

    return permute(nums)


print(solution([1, 2, 3]))
print(solution([0, 1]))
print(solution([1]))
