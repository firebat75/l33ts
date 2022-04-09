def solution(nums):
    # def backtracking(path, nums):
    #     print(path, nums)
    #     if not nums and path > sum(output[0]):
    #         print("appended")
    #         output[0] = [path]
    #     else:
    #         for i in range(len(nums)):
    #             print(i, path, nums)
    #             if len(nums) > 1:
    #                 backtracking(path + nums[i], nums[i + 2 :])
    #             else:
    #                 backtracking(path + nums[i], [])

    # output = [[0]]
    # backtracking(0, nums)
    # return output[0][0]

    length = len(nums)
    if length == 0:
        return 0
    if length == 1:
        return nums[0]
    if length == 2:
        return max(nums)

    dp = [0] * length  # assign dp array
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, length):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]


print(solution([90, 2, 3, 90]))
print(solution([2, 7, 9, 3, 1]))
print(solution([2, 7, 9, 3, 1]))
