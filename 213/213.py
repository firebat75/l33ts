def solution(nums):

    # length = len(nums)
    # if length == 0:
    #     return 0
    # if length == 1:
    #     return nums[0]
    # if length == 2:
    #     return max(nums)

    # dp = [0] * length  # assign dp array
    # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    # first = False
    # first2 = False
    # last = False
    # if dp[0] + nums[2] > dp[1]:
    #     first = True
    # for i in range(2, length):

    #     dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    #     if i == 3 and first and dp[i - 2] + nums[i] > dp[i - 1]:
    #         first2 = True

    #     if i == length - 1 and dp[i - 2] + nums[i] > dp[i - 1]:  # if nums[-1] is added
    #         last = True

    # print(dp)

    # if len(nums) <= 3 and (first and last):
    #     dp[-1] -= nums[0]
    # elif len(nums) > 3 and (first2 and last):
    #     print("SO TRUE")
    #     if nums[0] < nums[-1]:
    #         dp[-1] -= nums[0]
    #     else:
    #         dp[-1] -= nums[-1]

    # print(first, first2, last, dp)

    # return max(dp)

    def rob(nums):
        now = prev = 0
        for n in nums:
            now, prev = max(now, prev + n), now
        return now

    return max(rob(nums[len(nums) != 1 :]), rob(nums[:-1]))


print(solution([2, 3, 2]))
print(solution([1, 2, 3, 1]))
print(solution([1, 2, 3]))
print(solution([1, 1, 1, 2]))
print(solution([200, 3, 140, 20, 10]))
