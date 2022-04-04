def solution(n, k):
    nums = []
    for i in range(1, n + 1):
        nums.append(i)

    print(nums)

    output = []

    def backtracking(k2, path, nums, index):
        path.sort()
        print(k2, path, nums)

        if k2 > len(nums) - index + 1:
            pass

        elif not k2:
            if path not in output:
                output.append(path)
                print("APPENDING-----------------")

        else:
            for i in range(len(nums)):
                backtracking(k2 - 1, path + [nums[i]], nums[:i] + nums[i + 1 :], i + 1)

    backtracking(k, [], nums, 0)
    print("==============================================")
    return output


# print(solution(16, 12))
print(solution(4, 2))
print(solution(4, 3))
print(solution(4, 4))
print(solution(5, 3))

q = ([6, 1], len(solution(6, 1)))
a = ([6, 2], len(solution(6, 2)))
b = ([6, 3], len(solution(6, 3)))
c = ([6, 4], len(solution(6, 4)))
d = ([6, 5], len(solution(6, 5)))
e = ([6, 6], len(solution(6, 6)))

print(q)
print(a)
print(b)
print(c)
print(d)
print(e)
