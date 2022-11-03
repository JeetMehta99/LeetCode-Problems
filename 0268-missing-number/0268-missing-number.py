class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if i != nums[i]:
                return i
        return i+1