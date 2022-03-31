def solution(nums):
    def permute(nums):
        res = []
        dfs(nums, [], res)
        return res

    def dfs(nums, path, res):
        if not nums and path not in res:
            res.append(path)

        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)

    return permute(nums)


print(solution([1, 1, 2]))
print(solution([1, 2, 3]))
