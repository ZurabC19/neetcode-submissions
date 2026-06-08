class Solution:
    def simplifyPath(self, path: str) -> str:

        lst = path.split("/")
        stack = []


        for p in lst:
            if p =="..":
                if stack:
                    stack.pop()

            elif p != "." and p != "":
                stack.append(p)
        
        return "/"+ "/".join(stack)

