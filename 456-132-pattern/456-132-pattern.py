class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        final_num = float("-inf")
        for i in range(n-1,-1,-1):
            if nums[i]<final_num:
                return True
            while stack and stack[-1] < nums[i]:
                final_num = stack.pop()
            stack.append(nums[i])
        return False
        
                             
                