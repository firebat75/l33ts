def solution(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            print(nums[i], nums[j])
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
            print(dp)

    return str(max(dp))


print("S: " + solution([10, 9, 2, 5, 3, 7, 101, 18]))
print("S: " + solution([0, 1, 0, 3, 2, 3]))
print("S: " + solution([7, 7, 7, 7, 7, 7, 7]))
