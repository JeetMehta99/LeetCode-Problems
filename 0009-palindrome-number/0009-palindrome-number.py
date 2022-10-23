class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == -1:
            return False
        if x[:len(x)] == x[::-1]:
            return True
        else:
            return False