class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, i = 0, 0
        while i<len(nums):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
            i += 1
        return nums
        