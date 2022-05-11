class Solution:
    def countVowelStrings(self, n: int) -> int:
        def recursion(n, k): # k: what val we are at inside of our string
            if n == 0:
                return 1
            
            cnt = 0
            for i in range(k, 5):
                cnt += recursion(n-1, i) # avoid doing anything from before coz lexicography
                
            return cnt
        return recursion(n, 0)
                
                
           