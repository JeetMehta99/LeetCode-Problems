class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
                
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1 # left subarray
                else:
                    r = m - 1 # right subarray
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # right subarray
                else:
                    l = m + 1 # left subarray
        return -1