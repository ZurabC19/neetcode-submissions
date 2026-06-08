class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        r = len(heights)-1
        l=0
        most = 0
        area = 0
        while l<r:
            area=(min(heights[l],heights[r])*(r-l))
            if heights[l]>heights[r]:
                r-=1
            else: 
                l+=1
            most=max(area,most)
        return most
