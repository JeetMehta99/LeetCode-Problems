class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for ch in s:
            if ch == '#':
                if s1:
                    s1.pop()
            else:
                s1.append(ch)
        for ch in t:
            if ch == '#':
                if t1:
                    t1.pop()
            else:
                t1.append(ch)
        if s1 == t1:
            return True
        return False
  
    
    