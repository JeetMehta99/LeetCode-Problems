class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def getPrefix(nums):
            stack = []
            foundInt = False # the number that is greater than TOS
            for i in nums:  
    
                if len(stack) > 0 and i < stack[-1]:
                    foundInt = True
                    
                if foundInt:
                    while len(stack) >= 1 and i < stack[-1]:
                        stack.pop()
                else:
                    stack.append(i)
            return len(stack)
        
        prefix = getPrefix(nums)
        if prefix == len(nums):
            return 0
        
        suffix = getPrefix(list(-i for i in nums[::-1])) # converting it backwards & get greater numbers towards the end
        return len(nums)-prefix-suffix