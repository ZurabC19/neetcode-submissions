class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums)*2)
        s = len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
        for i in range(len(nums)):
            ans[s+i] = nums[i]
        
        return ans