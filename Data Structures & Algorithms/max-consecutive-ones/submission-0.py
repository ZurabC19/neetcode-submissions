class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0; 
        m = 0;       
        for x in nums:
            if x == 0:
                a = 0
            else: 
                a += 1
                m = max(m, a)
        return m