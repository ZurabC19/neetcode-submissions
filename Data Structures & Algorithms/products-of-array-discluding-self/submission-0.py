class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0]*len(nums)

        i = 0
        for i in range(n):
            output[i]=1
            for j in range(n):
                if i == j:
                    continue
                output[i]*=nums[j]
        return output