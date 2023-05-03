class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a, b = [], []
        for item in nums1:
            if item not in nums2:
                a.append(item)

        for item in nums2:
            if item not in nums1:
                b.append(item)

        return [list(set(a)), list(set(b))] 