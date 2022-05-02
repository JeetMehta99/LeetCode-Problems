class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = [] # list
        stack =[] 
        for i, ch in enumerate(s):
            stack.append(i+1)
            
            if ch == "I":
                while stack:
                    res.append(stack.pop()) 
        stack.append(len(s)+1) # last number to append
        while stack:
            res.append(stack.pop()) 
        return res 
        