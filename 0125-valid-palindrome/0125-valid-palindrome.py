class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        rev_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()[::-1]
        
        if s == rev_s:
            return True
        else:
            return False