class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        m = arr[len(arr)-1]
        for r in range (len(arr)-1,-1,-1):
            
            if arr[r] >= m:
                temp = arr[r]
                arr[r]=m
                m=temp
            else:
                arr[r]=m
            
        arr[len(arr)-1] = -1
        return arr
