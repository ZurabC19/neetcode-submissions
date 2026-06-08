class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        
        for n in range(min(len(str1),len(str2)), 0, -1):
            if (len(str1) % n == 0 and 
                len(str2) % n == 0 and
                str1[:n]*((len(str1))//n) == str1 and 
                str1[:n]*((len(str2))//n) == str2):
                return str1[:n]
        return ""

