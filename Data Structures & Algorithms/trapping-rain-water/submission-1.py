class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0 

        l = 0
        r = len(height)-1


        mL = height[l]
        mR = height[r]

        while l<r:

            if mL < mR:
                l+=1
                mL = max(mL,height[l])

                res+=mL - height[l]
            else:
                r-=1
                mR = max(mR,height[r])

                res+=mR - height[r]
        
        return res