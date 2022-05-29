def solution(nums: list[int]) -> int:
    print(nums)

    output = 0
    rems = []

    for e in range(len(nums)):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rems.append(i)

        if not rems:
            return output

        rems.reverse()
        for item in rems:
            del nums[item]

        print(nums)

        rems = []
        output += 1

    return output

    highest = 0
    curr = 0
    index = 0
    for i in range(1, len(nums)):
        print(nums[index], nums[i], curr, highest)

        if nums[i] < nums[index]:

            if curr > 0:
                if nums[i] >= nums[i-1]:
                    curr += 1
                    
                else:
                    pass
            
            else:
                curr += 1
            highest = max(highest, curr)
        else:
            index = i
            curr = 0


    return highest

print(solution([5,3,4,4,7,3,6,11,8,5,11]))
print(solution([10,1,2,3,4,5,6,1,2,3]))
print(solution([7,14,4,14,13,2,6,13]))