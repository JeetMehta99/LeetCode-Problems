class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        if not s:
            return 0

        count = 0
        stack_Arr = []
        ptr = 0
        for i in range(len(s)):
            if s[i] == "(":
                ptr = 1
                stack_Arr.append("(")
            if s[i] == ")":
                if ptr == 1:
                    count += 2**(len(stack_Arr)-1)
                    ptr = 0                
                stack_Arr.pop()
        return count
                
        