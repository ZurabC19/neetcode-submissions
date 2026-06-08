class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)

        l = 1

        for i in range(len(nums)):
            output[i] = l
            l *= nums[i]

        r = 1

        for i in range(len(nums)-1,-1,-1):
            output[i]=r *output[i]
            r = nums[i]*r

        return output
