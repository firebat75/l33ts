def solution(nums):
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
