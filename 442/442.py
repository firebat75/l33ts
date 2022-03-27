def solution(nums):
    output = []
    for item in nums:
        i = abs(item) - 1
        if nums[i] > 0:
            nums[i] *= -1
        else:
            output.append(abs(item))

    return output


print(solution([4, 3, 2, 7, 8, 2, 3, 1]))
print(solution([1, 1, 2]))
print(solution([1]))
