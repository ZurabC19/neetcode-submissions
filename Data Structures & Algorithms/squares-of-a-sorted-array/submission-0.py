class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for n in range(len(nums)):
            nums[n]=abs(nums[n])**2
        nums.sort()
        return nums