def solution(nums):
    slow = fast = check = 0

    while True:

        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    while True:

        slow = nums[slow]
        check = nums[check]

        if slow == check:
            break

    return check


print(solution([1, 3, 4, 2, 2]))
print(solution([3, 1, 3, 4, 2]))
