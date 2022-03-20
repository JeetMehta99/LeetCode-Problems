class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        for num in nums:
            if i == num:
                i += 1
        
        return i
        