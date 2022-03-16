class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_Arr = []
        s = list(s)
        # print(s)
        for idx, char in enumerate(s):
            if char == '(':
                stack_Arr.append(idx)
            elif char == ')':
                if stack_Arr:
                    stack_Arr.pop()
                else:
                    s[idx] = ''
        while stack_Arr:
                s[stack_Arr.pop()] = ''
        
        return "".join(s)
                
        