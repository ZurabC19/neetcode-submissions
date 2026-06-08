class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0 
        l = 0 
        r=1
        charSet=set()


        for r in range(len(s)):
            

            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
                

            
            res=max(r-l+1,res)
            charSet.add(s[r])
            
    
        return res