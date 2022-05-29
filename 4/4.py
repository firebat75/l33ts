def solution(nums1: list[int], nums2: list[int]):
    full = nums1 + nums2
    full.sort()
    print(full)
    if len(full)%2 == 0:
        print(full[(len(full)//2)-1], full[len(full)//2])
        return (full[(len(full)//2)-1] + full[len(full)//2]) / 2
    else:
        print(full[len(full)//2])
        return full[len(full)//2]


print(solution(nums1 = [1,3], nums2 = [2]))
print(solution(nums1 = [1,2], nums2 = [3,4]))