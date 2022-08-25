import sys 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        for i in range(1, len(nums)): # L->R
            arr[i] = arr[i-1] * nums[i-1]
        tmp = 1
        for i in range(len(nums)-2, -1, -1): # R->L
            tmp *= nums[i+1]
            arr[i] *= tmp
        return arr