class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.reverse()
        for i in range(len(nums1)-m):
            del nums1[0]
            
        nums1 += nums2
        
        nums1.sort()