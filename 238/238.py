def solution(nums):
    p = 1
    n = len(nums)
    output = []
    print(output, p)
    print("first loop")
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
        print(output, p)
    p = 1
    print("second loop")
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
        print(output, p)
    return output


print("SOLUTION: ", solution([1, 2, 3, 4]))
print("SOLUTION: ", solution([-1, 1, 0, -3, 3]))
