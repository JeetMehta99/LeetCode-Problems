class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # pair of values: char, count
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][-1] += 1
            else:
                stack.append([i,1])
            
            if stack[-1][1] == k:
                stack.pop()
            
        res = ""
        for ch, cnt in stack:
            res += (ch*cnt)
        
        return res
        
        
         