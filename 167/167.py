class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        x = list(set(numbers))
        x.sort()
        
        for i in range(len(x)):
            y = target - x[i]
            
            if y in x[i+1:]:
                return [numbers.index(x[i]) + 1, numbers.index(y) + 1]
            elif y == x[i]:
                return [numbers.index(x[i]) + 1, numbers.index(x[i]) + 2]   