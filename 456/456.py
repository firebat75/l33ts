def solution(nums):
    if len(nums) < 3:
        return False

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                # print("pos: ", i, j, k)
                # print("num: ", nums[i], nums[k], nums[j])
                if nums[i] < nums[k] < nums[j]:
                    return True

    return False


print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
print(solution([3, 1, 4, 2]))
print(solution([-1, 3, 2, 0]))
