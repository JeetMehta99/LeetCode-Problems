class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(N) Time
        # O(1) Space
        
        if len(nums) == 1:
            return nums
        
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        
        # index which would represent my first non ascending index
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1 # keep going left
        self.reverse(nums, dec+1, len(nums)-1) # reverse everything after that
        if dec == -1: # list in ascending order
            return 
        
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap(nums, next_num, dec)
        
    def swap(self, nums, int1, int2):
        temp = nums[int1]
        nums[int1] = nums[int2]
        nums[int2] = temp
    
    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1