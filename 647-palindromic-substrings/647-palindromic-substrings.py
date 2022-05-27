class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        
        if n == 0:
            return 0

        for i in range(n): 
            count += 1 
            right = i + 1 
            left = i - 1 
            # print(left)
            while right < n and s[right] == s[i]: 
                right+=1
                count+=1
                
            while right < n and left >= 0 and s[left] == s[right]: 
                count += 1
                left -= 1
                right += 1
            
        return count