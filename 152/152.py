def solution(nums):
    # O(n^2) solution (gets tle)
    # if len(nums) == 1:
    #     return nums[0]
    # biggest = max(nums)
    # if len(nums) == 2:
    #     return max(biggest, nums[0] * nums[1])

    # for i in range(len(nums)):
    #     temp = nums[i:]
    #     for e in range(i, len(nums) - 1):
    #         temp = [temp[0] * temp[1]] + temp[2:]

    #         if temp[0] > biggest:
    #             biggest = temp[0]

    # return biggest

    prev_max = nums[0]
    prev_min = nums[0]
    max_to_n = nums[0]
    min_to_n = nums[0]
    ans = nums[0]

    for i in nums[1:]:
        max_to_n = max(max(prev_max * i, prev_min * i), i)
        min_to_n = min(min(prev_max * i, prev_min * i), i)
        prev_max = max_to_n
        prev_min = min_to_n
        if max_to_n > ans:
            ans = max_to_n
    return ans


print(solution([2, 3, -2, 4]))
print(solution([-2, 0, -1]))
print(solution([0, 2]))
