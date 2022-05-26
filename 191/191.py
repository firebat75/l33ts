class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        output = 0
        for char in n:
            if char == "1":
                output += 1
        
        return output