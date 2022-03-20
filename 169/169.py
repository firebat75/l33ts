def majorityElement(nums):
    x = {}

    for num in nums:

        if num not in x:
            x[num] = 1
        else:
            x[num] += 1

        if x[num] > len(nums) / 2:
            return num


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
