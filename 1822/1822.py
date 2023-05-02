class Solution:
    def arraySign(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] * nums[i]

        if nums[-1] == 0:
            return 0
        elif nums[-1] < 0:
            return -1
        else:
            return 1