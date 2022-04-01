class Solution:
    def reverseString(self, s: List[str]) -> None:            
        
		# one points to head position, the other points to tail position
        left, right = 0, len(s)-1
        
		# reverse string by two pointers
        while left < right:
            
            s[left], s[right] = s[right], s[left]
            
            left,right = left+1, right-1
        