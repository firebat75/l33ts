def solution(nums, k):

    temp = nums[:]

    i = 0

    output = 0

    while i < len(nums):
        print(len(nums), nums, i)
        print(len(nums), nums, i, nums[i])
        found = False
        e = i + 1
        while not found and e < len(nums):
            print(i, nums[i], e, nums[e])
            if nums[i] + nums[e] == k:
                del nums[e]
                del nums[i]
                output += 1
                found = True
            else:
                e += 1

        if not found:
            i += 1
            

    return output

print(solution([1,2,3,4], 5))
print(solution([3,1,3,4,3], 6))
