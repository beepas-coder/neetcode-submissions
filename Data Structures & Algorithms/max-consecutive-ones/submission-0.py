class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        big = []
        strek = 0
        for i in nums:
            if i == 1:
                strek +=1
            else:
                big.append(strek)
                strek = 0
        big.append(strek)
        return max(big)
            
        