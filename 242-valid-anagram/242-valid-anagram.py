class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = sorted(list(s))
        k = sorted(list(t))
        
        if(len(r) != len(k)):
            return False
        
        for i in range(len(r)):
            if(r[i] != k[i]):
                return False
            
        return True
            
        
            