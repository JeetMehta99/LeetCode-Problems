class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for ch in s:
            if stack == []:
                stack.append(ch)
            else:
                if ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif ch == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif ch == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(ch)
        
        if stack == []:
            return True
        else:
            return False